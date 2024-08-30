import os 
import termios
import sys


def myGetch():
    prompt = "Enter key: "
    fd = sys.stdin.fileno()

    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, new)

    try:
        termios.tcsetattr(fd, termios.TCSADRAIN, new)
        print(prompt)
        
        # Leer el primer carácter
        char = sys.stdin.read(1)
        
        # Si es un carácter de escape, leer los siguientes dos caracteres
        if char == '\x1b':
            char += sys.stdin.read(2)
        
        # Interpretar la secuencia de escape
        print(f"char gotten: {char}")
        
        return char

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)




def listCCvalues():
    for name in dir(termios):
        if name.startswith('V'):
            print(name)

def getpass(prompt="Password: "):
    fd = sys.stdin.fileno() # descripto de archivo
    print(type(fd))
    idn = sys.stdout.fileno()
    print(idn)
    old = termios.tcgetattr(fd)
    print(old)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~termios.ECHO          # lflags
    print(new)
    try:
        termios.tcsetattr(fd, termios.TCSADRAIN, new)
        passwd = input(prompt)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
    return passwd


def main():
    while True:
        key = myGetch()
        print(f"Lenght of key {len(key)}")
        if len(key)<2:
            print(f"Tecla presionada: {key}")
            print(f"chars in {key}")
            print(f"ordinals {ord(key)}")
            print(f"hexadecimals {hex(ord(key))}") 
        else:
            char = ''
            ordinals = ''
            hexadecimal = ''
            for i,k in enumerate(key):
                print(f"{i}")
                char += k
                ordinals += f"{ord(k)},"    
                hexadecimal += f"{hex(ord(k))},"

            print(f"chars in {char}")
            print(f"ordinals {ordinals}")
            print(f"hexadecimals {hexadecimal}")    

        if key == '\x1b[A':
            print('UP')
        elif key == '\x1b[B':
            print('DOWN')
        elif key == '\x1b[C':
            print('RIGHT')
        elif key == '\x1b[D':
            print('LEFT')
        elif key == 'q':
            break

    

if __name__ == "__main__":
    main()