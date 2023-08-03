import json

import requests
from bs4 import BeautifulSoup as bs
from django.test import TestCase

# Create your tests here.

def major(url):
    subjects = []
    request = requests.get(url)
    source = request.text
    soup = bs(source, "html.parser")
    datas = soup.find_all('tr')[1:]
    for data in datas:
        subject = data.find_all('td')[:4]
        subjects.append({'grade': subject[0].text, 'semester': subject[1].text, 'type': subject[2].text, 'numbers': subject[3].text})
    print(subjects)

def subjects(year, semester):
    print(f'{year}-{semester}')
    file_path = f'dataset/{year}_{semester}.json'
    with open(file_path, 'r', encoding='UTF-8') as f:
        datas = json.load(f)['dsUcsLectLsnPdoc']
        print(len(datas))

# major('https://cs.smu.ac.kr/cs/admission/curriculum.do?srYear=2023&srSust=03005&srShyr=all')
# major('https://hi.smu.ac.kr/hi/admissions/curriculum.do?srYear=2022&srSust=03204&srShyr=all')
subjects(2019, 20)