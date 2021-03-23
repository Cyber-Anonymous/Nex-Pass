#!/use/bin/env python3
#Coded by Sajjad.
#https://github.com/Cyber-Anonymous

import os
import sys

change=(("S","$"),("a","@"),("s","5"),("j","J"),("i","!"),("and","&"),("123","321"),("y","Y"),("o","0"),("(","["),(")","]"),("[","{"),("]","}"),("A","4"),("T","7"),(" ","_"),("e","E"),("I","!!"),(".","?"),("E","3"))

os.system("clear") 
print("""\033[1;0;92m


███╗   ██╗███████╗██╗  ██╗     ██████╗  █████╗ ███████╗███████╗
████╗  ██║██╔════╝╚██╗██╔╝     ██╔══██╗██╔══██╗██╔════╝██╔════╝
██╔██╗ ██║█████╗   ╚███╔╝█████╗██████╔╝███████║███████╗███████╗
██║╚██╗██║██╔══╝   ██╔██╗╚════╝██╔═══╝ ██╔══██║╚════██║╚════██║
██║ ╚████║███████╗██╔╝ ██╗     ██║     ██║  ██║███████║███████║
╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝     ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝
                           \033[1;97mCoded by Sajjad  | Cyber Anonymous |
""")
  
print("""\033[0;92m""")
print("")
print("")
while(True):
    def secure(password):
        for a,b in change:
            password=password.replace(a,b)
            
        return password
    if __name__=="__main__":
         password=input("\n\033[1;0;92mEnter the password:\033[0;0m ")
         print(" ")
         print(" ")
         password=secure(password)
         print("\n\033[1;0;92m------------------------------")
         print("\n\033[1;0;0m"+password+"\033[1;0;0m")
         print("\n\033[1;0;92m------------------------------")
         print(" ")
         a=input("\n\033[1;94mDo you want to continue [y/n]: \033[0;0m").lower()
         print("\033[0m")
         if(a!="y"):
             sys.exit()
             break