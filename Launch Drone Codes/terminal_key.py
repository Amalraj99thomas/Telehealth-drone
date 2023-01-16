from __future__ import print_function

import threading

import sys, select, termios, tty


msg = """
Reading from the keyboard  and Publishing to Twist!
---------------------------
Moving around:
   u    i    o
   j    k    l
   m    ,    .
For Holonomic mode (strafing), hold down the shift key:
---------------------------
   U    I    O
   J    K    L
   M    <    >
t : up (+z)
b : down (-z)
anything else : stop
q/z : increase/decrease max speeds by 10%
w/x : increase/decrease only linear speed by 10%
e/c : increase/decrease only angular speed by 10%
CTRL-C to quit
"""




def getKey(key_timeout):
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], key_timeout)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    print("in function", key)
    return key



class PublishThread(threading.Thread):
    def __init__(self, rate):
        super(PublishThread, self).__init__()
        self.condition = threading.Condition()
        self.done = False

        # Set timeout to None if rate is 0 (causes new_message to wait forever
        # for new data to publish)
        if rate != 0.0:
            self.timeout = 1.0 / rate
        else:
            self.timeout = None

        self.start()

    def update(self):
        print("Update")
        self.condition.acquire()
        # Notify publish thread that we have a new message.
        self.condition.notify()
        self.condition.release()

    def stop(self):
        self.done = True
        self.join()

    def run(self):
        while not self.done:
            print("run")
            self.condition.acquire()
            # Wait for a new message or timeout.
            self.condition.wait(self.timeout)

            self.condition.release()


if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)
    repeat = 0.0
    pub_thread = PublishThread(repeat)
    i = 0
    
    
    key_timeout=0.0
    try:

        pub_thread.update()

        print(msg)
        
        while i < 8:
            key = getKey(key_timeout)
            print("key", key)
  
            pub_thread.update()
            i = i+1

    except Exception as e:
        print(e)

    finally:
        pub_thread.stop()

        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)