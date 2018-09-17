import os
import subprocess

def move(a, b, c, d):
    print("options to move: 1-Image files, 2-Audio files, 3-Document files, 4-Video files")
    try:
        choice = int(input("Choice a option [1/2/3/4]: "))
        print("-" * 10)
        if choice == 1:
            a = os.system("mv --verbose ~/Downloads/*.jpg ~/Pictures")
            a = os.system("mv --verbose ~/Downloads/*.png ~/Pictures")
        elif choice == 2:
            b = os.system("mv --verbose ~/Downloads/*.mp3 ~/Music")
        elif choice == 3:
            c = os.system("mv --verbose ~/Downloads/*.pdf ~/Documents")
            c = os.system("mv --verbose ~/Downloads/*.docx ~/Documents")
        elif choice == 4:
            d = os.system("mv --verbose ~/Downloads/*.mp4 ~/Videos")
            d = os.system("mv --verbose ~/Downloads/*.mkv ~/Videos")
        print("-" * 10)
        pass

    except:
        print()
        print("{}>> Error! <<{}".format('\033[1;91m', '\033[m'))
        pass

move('a', 'b', 'c', 'd')
