# import requests
# from bs4 import BeautifulSoup
# from time import sleep
# from random import randint
#
# file = open('football.csv', 'w', newline='\n', encoding='utf-8')
# file.write('Club_Name\n')
#
#
# ind = 1
# while ind<=5:
#     url = 'https://footballdatabase.com/ranking/world/' + str(ind)
#     r = requests.get(url)
#
#     content = r.text
#     soup = BeautifulSoup(content, 'html.parser')
#
#     clubs = soup.find('div', class_='table-responsive')
#     all_clubs = clubs.find_all('td', class_='club text-left')
#
#     for each in all_clubs:
#         Name = each.a.text
#         print(Name)
#         file.write(Name+'\n')
#
#     ind += 1
#     sleep(randint(3, 7))
