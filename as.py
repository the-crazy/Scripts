import os
import subprocess

def agdshutdown(agd):
    print("Schedule Shutdown\nby:Clei\ndate:30/07/2018")
    print()
    try:
        hour = int(input("Hour: "))
        minutes = int(input("Minutes: "))
        print("-" * 10)
        agd = os.system('shutdown -h {}:{}'.format(hour, minutes))
        print("-" * 10)
        print("")
        print("{}>> For cancel a scheduling, write 'asc' in command line. <<{}".format('\033[1;32m', '\033[m'))
        pass
    except:
        print()
        print("{}>> Error! <<{}".format('\033[1;91m', '\033[m'))
        pass

agdshutdown('agd')
