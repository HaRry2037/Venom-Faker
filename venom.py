#!/usr/bin/python
from colorama import Fore
import random 
from faker import Faker
import os

os.system('clear')
r = Fore.RED
g = Fore.GREEN
y = Fore.YELLOW
w = Fore.WHITE
b = Fore.BLUE
c = Fore.CYAN

colors = (r, g, y, w, b, c)
color = random.choice(colors)

banner = '''

██╗   ██╗███████╗███╗   ██╗ ██████╗ ███╗   ███╗      ███████╗ █████╗ ██╗  ██╗███████╗██████╗ 
██║   ██║██╔════╝████╗  ██║██╔═══██╗████╗ ████║      ██╔════╝██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
██║   ██║█████╗  ██╔██╗ ██║██║   ██║██╔████╔██║█████╗█████╗  ███████║█████╔╝ █████╗  ██████╔╝
╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║   ██║██║╚██╔╝██║╚════╝██╔══╝  ██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗  Created By Venom
 ╚████╔╝ ███████╗██║ ╚████║╚██████╔╝██║ ╚═╝ ██║      ██║     ██║  ██║██║  ██╗███████╗██║  ██║  Follow me on insta: i.m.gauravchaudhary
  ╚═══╝  ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝      ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝  Contact: +91 9910332273


     [1] India
     [2] US
     [3] Japan
     [4] Italy
     [5] Random
     [6] Exit

'''
print(color + banner + color)
choice = int(input(w + '     [+] ' + w + color + 'Enter the country you want fake profile of: ' + color))
def id(country):
    fake = Faker(country)
    print(' ')
    profile = fake.profile()
    print(w + '     [+] ' + w + y + 'Name: ' + y + g + profile['name'] + g)
    print(w + '     [+] ' + w + y + 'Username: ' + y + g + profile['username'] + g)
    print(w + '     [+] ' + w + y + 'Sex: ' + y + g + profile['sex'] + g)
    print(w + '     [+] ' + w + y + 'Date of birth: ' + y + g + str(profile['birthdate']) + g)
    print(w + '     [+] ' + w + y + 'Address: ' + y + g + profile['address'] + g)
    print(w + '     [+] ' + w + y + 'Email: ' + y + g + profile['mail'] + g)
    print(w + '     [+] ' + w + y + 'Blood Group: ' + y + g + profile['blood_group'] + g)
    print(w + '     [+] ' + w + y + 'Website: ' + y + g + profile['website'][0] + g)
    print(w + '     [+] ' + w + y + 'Residence: ' + y + g + profile['residence'] + g)
    print(w + '     [+] ' + w + y + 'Job: ' + y + g + profile['job'] + g)
    print(w + '     [+] ' + w + y + 'Company: ' + y + g + profile['company'] + g)
    print(w + '     [+] ' + w + y + 'SSN: ' + y + g + profile['ssn'] + g)
if choice == 1:
    id('hi_IN')
elif choice == 2:
    id('en_US')
elif choice == 3:
    id('ja_JP')
elif choice == 4:
    id('it_IT')
elif choice == 5:
    id(' ')
elif choice == 6:
    exit()
