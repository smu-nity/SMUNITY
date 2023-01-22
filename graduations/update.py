# 장고 환경
import os
import json
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
application = get_wsgi_application()

from graduations.models import Subject, Major
from accounts.models import Department


def main(year, semester):
    print(f'{year}-{semester}')
    file_path = f'dataset/{year}_{semester}.json'
    with open(file_path, 'r') as f:
        datas = json.load(f)['dsUcsLectLsnPdoc']
        for data in datas:
            SBJ_NO = data['SBJ_NO']
            if not Subject.objects.filter(number=SBJ_NO):
                Subject.objects.create(number=SBJ_NO, name=data['SBJ_NM'], credit=data['CDT'], dept=data['EST_DEPT_INFO'], type=data['CMP_DIV_NM'])

def major(dept, subjects, type):
    for subject in subjects:
        Major.objects.create(department=dept, subject=subject, type=type)


if __name__ == '__main__':
    # data = [['2017', '10'], ['2017', '11'], ['2017', '20'], ['2017', '21'], ['2018', '10'], ['2018', '11'], ['2018', '20'], ['2018', '21'], ['2019', '10'], ['2019', '11'], ['2019', '20'], ['2019', '21'], ['2020', '10'], ['2020', '11'], ['2020', '20'], ['2020', '21'], ['2021', '10'], ['2021', '11'], ['2021', '20'], ['2021', '21'], ['2022', '10'], ['2022', '11'], ['2022', '20'], ['2022', '21'], ['2023', '10']]
    # for d in data:
    #     main(d[0], d[1])
    numbers = ['HASW0001', 'HAEA9225', 'HAEA9237', 'HAFL7001', 'HAEA0001', 'HAEA0017', 'HAEA0027', 'HAEA9236', 'HAEA9241', 'HAFL0002', 'HAEA0005', 'HAEA9239', 'HAEA9243', 'HAEA0020', 'HAEA9229', 'HAEA9240']
    dept, subjects = Department.objects.get(name='컴퓨터과학전공'), Subject.objects.filter(number__in=numbers)
    major(dept, subjects, '1전선')
    numbers = ['HAEA0004', 'HAEA0008', 'HAEA0012', 'HAEZ0003']
    dept, subjects = Department.objects.get(name='컴퓨터과학전공'), Subject.objects.filter(number__in=numbers)
    major(dept, subjects, '1전심')
