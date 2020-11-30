#!/usr/bin/python
from colorama import Fore
import random 
from faker import Faker

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
if choice == 1:
    fake = Faker('hi_IN')
    print(' ')
    india = fake.profile()
    print(w + '     [+] ' + w + y + 'Name: ' + y + g + india['name'] + g)
    print(w + '     [+] ' + w + y + 'Username: ' + y + g + india['username'] + g)
    print(w + '     [+] ' + w + y + 'Sex: ' + y + g + india['sex'] + g)
    print(w + '     [+] ' + w + y + 'Date of birth: ' + y + g + str(india['birthdate']) + g)
    print(w + '     [+] ' + w + y + 'Address: ' + y + g + india['address'] + g)
    print(w + '     [+] ' + w + y + 'Email: ' + y + g + india['mail'] + g)
    print(w + '     [+] ' + w + y + 'Blood Group: ' + y + g + india['blood_group'] + g)
    print(w + '     [+] ' + w + y + 'Website: ' + y + g + india['website'][0] + g)
    print(w + '     [+] ' + w + y + 'Residence: ' + y + g + india['residence'] + g)
    print(w + '     [+] ' + w + y + 'Job: ' + y + g + india['job'] + g)
    print(w + '     [+] ' + w + y + 'Company: ' + y + g + india['company'] + g)
    print(w + '     [+] ' + w + y + 'SSN: ' + y + g + india['ssn'] + g)
elif choice == 2:
    fake = Faker('en_US')
    print(' ')
    us = fake.profile()
    print(w + '     [+] ' + w + y + 'Name: ' + y + g + us['name'] + g)
    print(w + '     [+] ' + w + y + 'Username: ' + y + g + us['username'] + g)
    print(w + '     [+] ' + w + y + 'Sex: ' + y + g + us['sex'] + g)
    print(w + '     [+] ' + w + y + 'Date of birth: ' + y + g + str(us['birthdate']) + g)
    print(w + '     [+] ' + w + y + 'Address: ' + y + g + us['address'] + g)
    print(w + '     [+] ' + w + y + 'Email: ' + y + g + us['mail'] + g)
    print(w + '     [+] ' + w + y + 'Blood Group: ' + y + g + us['blood_group'] + g)
    print(w + '     [+] ' + w + y + 'Website: ' + y + g + us['website'][0] + g)
    print(w + '     [+] ' + w + y + 'Residence: ' + y + g + us['residence'] + g)
    print(w + '     [+] ' + w + y + 'Job: ' + y + g + us['job'] + g)
    print(w + '     [+] ' + w + y + 'Company: ' + y + g + us['company'] + g)
    print(w + '     [+] ' + w + y + 'SSN: ' + y + g + us['ssn'] + g)

elif choice == 3:
    fake = Faker('ja_JP')
    print(' ')
    japan = fake.profile()
    print(w + '     [+] ' + w + y + 'Name: ' + y + g + japan['name'] + g)
    print(w + '     [+] ' + w + y + 'Username: ' + y + g + japan['username'] + g)
    print(w + '     [+] ' + w + y + 'Sex: ' + y + g + japan['sex'] + g)
    print(w + '     [+] ' + w + y + 'Date of birth: ' + y + g + str(japan['birthdate']) + g)
    print(w + '     [+] ' + w + y + 'Address: ' + y + g + japan['address'] + g)
    print(w + '     [+] ' + w + y + 'Email: ' + y + g + japan['mail'] + g)
    print(w + '     [+] ' + w + y + 'Blood Group: ' + y + g + japan['blood_group'] + g)
    print(w + '     [+] ' + w + y + 'Website: ' + y + g + japan['website'][0] + g)
    print(w + '     [+] ' + w + y + 'Residence: ' + y + g + japan['residence'] + g)
    print(w + '     [+] ' + w + y + 'Job: ' + y + g + japan['job'] + g)
    print(w + '     [+] ' + w + y + 'Company: ' + y + g + japan['company'] + g)
    print(w + '     [+] ' + w + y + 'SSN: ' + y + g + japan['ssn'] + g)
elif choice == 4:
    fake = Faker('it_IT')
    print(' ')
    itlay = fake.profile()
    print(w + '     [+] ' + w + y + 'Name: ' + y + g + itlay['name'] + g)
    print(w + '     [+] ' + w + y + 'Username: ' + y + g + itlay['username'] + g)
    print(w + '     [+] ' + w + y + 'Sex: ' + y + g + itlay['sex'] + g)
    print(w + '     [+] ' + w + y + 'Date of birth: ' + y + g + str(itlay['birthdate']) + g)
    print(w + '     [+] ' + w + y + 'Address: ' + y + g + itlay['address'] + g)
    print(w + '     [+] ' + w + y + 'Email: ' + y + g + itlay['mail'] + g)
    print(w + '     [+] ' + w + y + 'Blood Group: ' + y + g + itlay['blood_group'] + g)
    print(w + '     [+] ' + w + y + 'Website: ' + y + g + itlay['website'][0] + g)
    print(w + '     [+] ' + w + y + 'Residence: ' + y + g + itlay['residence'] + g)
    print(w + '     [+] ' + w + y + 'Job: ' + y + g + itlay['job'] + g)
    print(w + '     [+] ' + w + y + 'Company: ' + y + g + itlay['company'] + g)
    print(w + '     [+] ' + w + y + 'SSN: ' + y + g + itlay['ssn'] + g)
elif choice == 5:
    fake = Faker()
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
elif choice == 6:
    print(w + '     [+] ' + w + r + 'Exiting Ok bye bye' + r)
    exit()
else:
    print(w + '     [+] ' + w + r + ' I do not understand you' + r)
    exit()
