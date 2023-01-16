import readchar

def main():
        for i in range(0,10):
            #c = readchar.readchar()
            key = readchar.readkey()
            if key =='\x1b[A':
                print("Key: ","up")
            elif key =='\x1b[B':
                    print("Key: ","down")
            elif key=='\x1b[C':
                    print("Key: ","right")
            elif key =='\x1b[D':
                    print("Key: ","left")
            else:
                 print("Key: ", key)
        

if __name__=='__main__':
        main()