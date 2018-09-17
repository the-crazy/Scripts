import os
import subprocess
import datetime

print("Cleaner\nby: Clei\ndate: 16\\07\\18")
print()

def cleaner(a, b, c, d):

    #Log
    data = datetime.datetime.now() # Pega a hora atual do sistema

    def new_line(nw): # Adiciona uma nova linha (conteudo) no log
        log = open('.cleaner.log', 'r') # Abra o arquivo (leitura)
        content = log.readlines()
        content.append(nw)
        #content.append('\n{0} end {0}\n'.format('-' * 10))   # insira seu conteúdo

        log = open('.cleaner.log', 'w') # Abre novamente o arquivo (escrita)
        log.writelines(content)    # escreva o conteúdo criado anteriormente nele.

        log.close()
    def read():
        #cabecalho ------------------
        log = open('.cleaner.log', 'w') # Cria o arquivo de log
        #log.write('Cleaner\nby: Clei\n\n')
        log.write('----- Cleaner Log -----\n')
        log.write('\n>>{}\n\n'.format(data))
        #log.write('{}\n'.format('-' * 10))
        log.close()
        #-----------------------------------

    read() #inicio do log
    print("Choice a option: \n\n1-autoremove \n2-autoclean \n3-clean \n4-all\n")
    try:
        option = int(input("1, 2, 3 or 4? "))
        print()

        print(10 * "-")
        if option == 1:
            a = os.system("sudo apt-get autoremove >> .cleaner.log && clear && cat .cleaner.log")
        elif option == 2:
            b = os.system("sudo apt-get autoclean >> .cleaner.log && clear && cat .cleaner.log")
        elif option == 3:
            c = os.system("sudo apt-get clean >> .cleaner.log && clear && cat .cleaner.log")
        elif option == 4:
            d = os.system("sudo apt-get autoremove >> .cleaner.log && sudo apt autoclean >> .cleaner.log && sudo apt clean >> .cleaner.log && clear && cat .cleaner.log")
            #b = os.system("sudo apt autoclean >> cleanerlog.txt && clear")
            #c = os.system("sudo apt clean >> cleanerlog.txt && clear")
        print(10 * "-")
        print()

        if a or b or c or d == 0:
            print("Cleaner\nby: Clei\ndate: 16\\07\\18")
            print(10 * "-")
            print("{}Completed!{}\n".format('\033[1;32m', '\033[m'))

        new_line('\n{0} end {0}\n'.format('-' * 10)) #- Log final / Ultima linha do log
        pass

    except:
        os.system("clear")
        print()
        print("Cleaner\nby: Clei\ndate: 16\\07\\18")
        print(10 * "-")
        print("{}>> Error! <<{}".format('\033[1;91m', '\033[m'))
        new_line('ERRO\n')
        new_line('\n{0} end {0}\n'.format('-' * 10)) #- Log final / Ultima linha do log
        pass

cleaner('a', 'b', 'c', 'd')




