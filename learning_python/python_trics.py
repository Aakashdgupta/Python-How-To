# REMOVING DUPLICATES 

# LIST

li = [12,32,12,31,54]
print(li)
li = set(li)
li =list(li)
print(li)

# COLORED OUTPUT USING COLOROMA MODULE 

from colorama import Fore,Back,Style
print(Fore.RED + 'red text ')
print(Back.GREEN + " green text")
print(Style.RESET_ALL)
print(" All Style is reseted now")