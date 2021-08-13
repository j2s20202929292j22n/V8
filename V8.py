import os, wget
import sys
import time
import requests
os.system("rm -rf .Cheker.py")
os.system("cd .. ;cd home ;rm -rf Cheker.py ;clear")
os.system('clear')
os.system('rm -rf list.txt')
os.system('id -u > list.txt')
uidd = open('list.txt', 'r')
for j in uidd:
    sp = j.split()

def chk(): 
  uuid = str(os.geteuid()) + str(os.getlogin()) 
  id = "-".join(uuid) 
  print("\n\n\x1b[37;1mYour ID : "+id) 
  try: 
    httpCaht = requests.get("https://raw.githubusercontent.com/MrTLYAKI/list.txt/main/list.txt").text 
    if id in httpCaht: 
      print("\033[92mYOUR ID IS ACTIVE.........\033[97m") 
      msg = str(os.geteuid()) 
      time.sleep(1) 
      pass 
    else: 
      print("\x1b[91mID ACTIVE NYa bo kren nama bnera @lililliilliil\033[97m") 
      time.sleep(1) 
      sys.exit() 
  except: 
    sys.exit() 
    if name == '__main__': 
     print logo
     chk() 
    
chk()
print("\033[1;92m ")
logo='''

888888b.  Y88b   d88P 888b    888 
888  "88b  Y88b d88P  8888b   888 
888  .88P   Y88o88P   88888b  888 
8888888K.    Y888P    888Y88b 888 
888  "Y88b   d888b    888 Y88b888 
888    888  d88888b   888  Y88888 
888   d88P d88P Y88b  888   Y8888 
8888888P" d88P   Y88b 888    Y888 
                      
                                                   
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
\033[1;97m
  Author   : TLYAK
  Chanal Tlegram : Team_Codr1
  Telegram : lililliilliil
  Tool =======BNX=========
  Note : 10$     
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1 = Checker Facbook Login Crack Number Free Mod 
   
2 = Checker Inistagram Fast
   
3 = Checker Inistagram Load Combo
   
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
os.system("cd .. ;cd FAST")
print(logo)
def dwbara():
	chs=raw_input("halbzhera : ")
	if chs=='1':
		wget.download("https://raw.githubusercontent.com/j2s20202929292j22n/V1/main/Cheker-FB.py")
		os.system("python2 Cheker-FB.py")
	elif chs=='2':
		wget.download("https://github.com/j2s20202929292j22n/V4/blob/main/Inistav2.py")
		os.system("python Inistav2.py")
	elif chs=='3':
		wget.download("https://raw.githubusercontent.com/j2s20202929292j22n/V3/main/Inistav2.py")
		os.system("python Inistav2.py")
	else:
		print(" Number you made a mistake !")
		dwbara()
dwbara()
