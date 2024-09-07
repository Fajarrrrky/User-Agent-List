# -*- coding: utf-8 -*-

"""
GitHub: https://github.com/Fajarxyta
Facebook: https://facebook.com/fajarxyta15
Instagram: https://instagram.com/fajarxy_1
"""
P = '\033[0m'
H = "\033[32m"
L =  '\033[4m'
I = '\033[3m'

import os
from Useragents.main import MAIN

def main():
    os.system('clear')
    print(f"\n\t        [{I}{L}User-Agent All Platform {P}]\n\t\t   [{I}{P}Code By {H}@Fajar_kyy{P}]\n\n{H}1{P}) {H}Whatmyuseragent{P}\n{H}2{P}) {H}User_agents_net{P}\n")
    x = input("pilih 1/2: ")
    if x == '1':
        whatmyuseragent()
    else:
        url = 'https://user-agents.net/random'
        limit = input("Limit: ")
        MAIN().user_agents_net(limit, url)

def whatmyuseragent():
    os.system('clear')
    list_brand = MAIN().get_brand()
    for z, brand in list_brand.items():
        print(f'{z}) {brand["nama"]}')
    try:
        chose = input("Pilih: ")
        MAIN().Whatmyuseragent(list_brand[chose])
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()