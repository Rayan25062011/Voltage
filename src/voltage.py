import os
import sys
import time
import urllib
import urllib.request

end = '\033[0m'
black = '\033[30m'
red = '\033[31m'
green = '\033[32m'
orange = '\033[33m'
blue = '\033[34m'
purple = '\033[35m'
cyan = '\033[36m'
lightgrey = '\033[37m'
darkgrey = '\033[90m'
lightred = '\033[91m'
lightgreen = '\033[92m'
yellow = '\033[93m'
lightblue = '\033[94m'
pink = '\033[95m'
lightcyan = '\033[96m'

def load_animation():
  
    # String to be displayed when the application is loading
    load_str = "preparing for instalation..."
    ls_len = len(load_str)
  
  
    # String for creating the rotating line
    animation = "|/-\\"
    anicount = 0
      
    # used to keep the track of
    # the duration of animation
    counttime = 0        
      
    # pointer for travelling the loading string
    i = 0                     
  
    while (counttime != 100):
          
        # used to change the animation speed
        # smaller the value, faster will be the animation
        time.sleep(0.075) 
                              
        # converting the string to list
        # as string is immutable
        load_str_list = list(load_str) 
          
        # x->obtaining the ASCII code
        x = ord(load_str_list[i])
          
        # y->for storing altered ASCII code
        y = 0                             
  
        # if the character is "." or " ", keep it unaltered
        # switch uppercase to lowercase and vice-versa 
        if x != 32 and x != 46:             
            if x>90:
                y = x-32
            else:
                y = x + 32
            load_str_list[i]= chr(y)
          
        # for storing the resultant string
        res =''             
        for j in range(ls_len):
            res = res + load_str_list[j]
              
        # displaying the resultant string
        sys.stdout.write("\r"+res + animation[anicount])
        sys.stdout.flush()
  
        # Assigning loading string
        # to the resultant string
        load_str = res
  
          
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len
        counttime = counttime + 1
      
    # for windows OS
    if os.name =="nt":
        os.system("cls")
          
    # for linux / Mac OS
    else:
        os.system("clear")


def installAnimation():
    load_str = "packaging in progress..."
    ls_len = len(load_str)
  
  
    # String for creating the rotating line
    animation = "|/-\\"
    anicount = 0
      
    # used to keep the track of
    # the duration of animation
    counttime = 0        
      
    # pointer for travelling the loading string
    i = 0                     
  
    while (counttime != 100):
          
        # used to change the animation speed
        # smaller the value, faster will be the animation
        time.sleep(0.075) 
                              
        # converting the string to list
        # as string is immutable
        load_str_list = list(load_str) 
          
        # x->obtaining the ASCII code
        x = ord(load_str_list[i])
          
        # y->for storing altered ASCII code
        y = 0                             
  
        # if the character is "." or " ", keep it unaltered
        # switch uppercase to lowercase and vice-versa 
        if x != 32 and x != 46:             
            if x>90:
                y = x-32
            else:
                y = x + 32
            load_str_list[i]= chr(y)
          
        # for storing the resultant string
        res =''             
        for j in range(ls_len):
            res = res + load_str_list[j]
              
        # displaying the resultant string
        sys.stdout.write("\r"+res + animation[anicount])
        sys.stdout.flush()
  
        # Assigning loading string
        # to the resultant string
        load_str = res
  
          
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len
        counttime = counttime + 1
      
    # for windows OS
    if os.name =="nt":
        os.system("cls")
          
    # for linux / Mac OS
    else:
        os.system("clear")


def prepare():
    load_str = "installing requested package..."
    ls_len = len(load_str)
  
  
    # String for creating the rotating line
    animation = "|/-\\"
    anicount = 0
      
    # used to keep the track of
    # the duration of animation
    counttime = 0        
      
    # pointer for travelling the loading string
    i = 0                     
  
    while (counttime != 100):
          
        # used to change the animation speed
        # smaller the value, faster will be the animation
        time.sleep(0.075) 
                              
        # converting the string to list
        # as string is immutable
        load_str_list = list(load_str) 
          
        # x->obtaining the ASCII code
        x = ord(load_str_list[i])
          
        # y->for storing altered ASCII code
        y = 0                             
  
        # if the character is "." or " ", keep it unaltered
        # switch uppercase to lowercase and vice-versa 
        if x != 32 and x != 46:             
            if x>90:
                y = x-32
            else:
                y = x + 32
            load_str_list[i]= chr(y)
          
        # for storing the resultant string
        res =''             
        for j in range(ls_len):
            res = res + load_str_list[j]
              
        # displaying the resultant string
        sys.stdout.write("\r"+res + animation[anicount])
        sys.stdout.flush()
  
        # Assigning loading string
        # to the resultant string
        load_str = res
  
          
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len
        counttime = counttime + 1
      
    # for windows OS
    if os.name =="nt":
        os.system("cls")
          
    # for linux / Mac OS
    else:
        os.system("clear")

def package():
    url = input(f"[{yellow}info{end}] Enter the repository url: ")
    if '/package.toml' in url:
        installAnimation()
        os.system("git clone " + url)
        f = open("package.toml", 'x')
        f.write(f'''
[packaging]
repo = "{url}"
        ''')
    else:
        print(f'[{red}error{end}] Could not find file: package.json')

def install():
    load_animation()
    url = input(f"[{yellow}info{end}] Enter the repository url: ")
    gurl = f"{url}/blob/main/package.toml"
    try:
        urllib.request.urlopen(gurl)
        print(f"{green}Repository found{end}")
        return True
    except:
        return False
        print(f"[{red}error{end}] File or repository not found.")
        sys.exit(0)

    prepare()
    os.system("git clone "+gurl)
    



choice = input(f"[{yellow}info{end}] Package or install? ")
if choice == 'package':
    package()
if choice == 'install':
    install()
