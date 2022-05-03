from audioop import tostereo
from colorama import Fore,Back
from time import sleep 
# ------------------------ 

sleep(1)
print(f"""

 ██      ██  ████  ██     ██         ██████    ██████  ██████████ ██      ██
░██     ░██ █░░░ █░░██   ██         ██░░░░██  ██░░░░██░░░░░██░░░ ░██     ░██
░██     ░██░    ░█ ░░██ ██         ██    ░░  ██    ░░     ░██    ░██     ░██
░██████████   ███   ░░███    █████░██       ░██           ░██    ░░██    ██ 
░██░░░░░░██  ░░░ █   ██░██  ░░░░░ ░██       ░██           ░██     ░░██  ██  
░██     ░██ █   ░█  ██ ░░██       ░░██    ██░░██    ██    ░██      ░░████   
░██     ░██░ ████  ██   ░░██       ░░██████  ░░██████     ░██       ░░██    
░░      ░░  ░░░░  ░░     ░░         ░░░░░░    ░░░░░░      ░░         ░░     


                                                                 {Fore.RED}DEVELOPER: H3X
                                                                 insta : h3x_code
""")


print(Fore.RED+" \t Choose your CCTV model ")

# Options
toshiba = f'paste in browser : {Fore.YELLOW} intitle:”Toshiba Network Camera” user login'
EvoCam = f'paste in browser : {Fore.YELLOW} intitle:”EvoCam” inurl:”webcam.html”'
AXISCam = f'paste in browser : {Fore.YELLOW} \n \n intitle:”Live View / – AXIS ” \n intitle:”Live View / – AXIS 206M” \n intitle:”Live View / – AXIS 206W” \n intitle:”Live View / – AXIS 210?'
sony = f'paste in browser : {Fore.YELLOW} \n intitle:”sony network camera snc-p1? \n intitle:”sony network camera snc-m1?'
other = f"""paste in browser : {Fore.YELLOW} \n 
inurl:”CgiStart?page=”
inurl:/view.shtml
intitle:”Live View / – AXIS
inurl:view/view.shtml
inurl:ViewerFrame?Mode=
inurl:ViewerFrame?Mode=Refresh
inurl:axis-cgi/jpg
inurl:axis-cgi/mjpg (motion-JPEG) (disconnected)
inurl:view/indexFrame.shtml
inurl:view/index.shtml
inurl:view/view.shtml

"""

print(Fore.GREEN+f""" 

[1]-> {Fore.WHITE + "EvoCam" + Fore.GREEN}              [4]-> {Fore.WHITE + "sony" + Fore.GREEN}
[2]-> {Fore.WHITE + "AXIS" + Fore.GREEN}                [5]-> {Fore.WHITE + "other" + Fore.GREEN}
[3]-> {Fore.WHITE + "toshiba" + Fore.GREEN}


""")

option = input("Choose CCTV model : ")


if option == "1":
    print(EvoCam)
elif option == "2":
    print(AXISCam)
elif option == "3":
    print(toshiba)
elif option == "4":
    print(sony)
elif option == "5":
    print(other)