import os
import sys
import time
#=======Color=====#
N = '\033[0m'    # Normal Color
Y = '\033[1;33m' # Yellow Color
R = '\033[1;31m' # Red Color
G = '\033[1;32m' # Green Color
W = '\033[1;37m' # White Color
D = '\033[1;9;31m'  # DelBold Color
#==================#
os.system("clear")
print('''%s
   ▄▄▄▄███▄▄▄▄      ▄████████    ▄████████      
 ▄██▀▀▀███▀▀▀██▄   ███    ███   ███    ███      
 ███   ███   ███   ███    █▀    ███    █▀       
 ███   ███   ███   ███         ▄███▄▄▄          
 ███   ███   ███ ▀███████████ ▀▀███▀▀▀          
 ███   ███   ███          ███   ███             
 ███   ███   ███    ▄█    ███   ███             
  ▀█   ███   █▀   ▄████████▀    ███   
  %s''' % (G,N))
print("%s================================================%s" % (R,N))
print("%s----------Coded By Imperior Hackers-----------%s" % (Y,N))
print("%s================================================%s" % (R,N))
def exit():
  os.system("killall -9 com.termux")
def Install():
  os.system("clear")
  print("%sBefore We Start Please Check the Following Conditions :-   %s" % (R,N))
  print("")
  print("%s[1] Your Phone Must Have Atleast 800 MB of free storage%s" % (Y,N))
  print("")
  print("%s[2] Your Phone Must be Charged upto 90 Percent %s" % (Y,N))
  print("")
  print("%s[3] No Apps is Running in Background Except Termux%s" % (Y,N))
  print("")
  print("%s[4] You Should Ensure that You have enough time as the installation might take 1-2 hours or maybe less%s" % (Y,N))
  print("")
  print("%s[5] You Must Have an Active Internet Connection of atleast 500 Kbps%s" % (Y,N))
  B=input("Press Enter to Continue >> ")
  os.system("pkg install unstable-repo")
  os.system("pkg install metasploit")
  os.system("clear")
  print("%s[+] MetaSploit Successfully Installed :) %s" % (Y,N))
  print("")
  print("TO START METASPLOIT JUST TYPE THE COMMAND 'msfconsole' IN TERMUX")
A=input("%sDo You Want To Install Metasploit In Your Termux [Yes/No] :- %s" % (Y,N))
if A=='Yes' or A=='yes':
  Install()
elif A=='No' or A=='no':
  os.system("clear")
else: print("%sWRONG INPUT %s" % (R,N))
