# 장고 환경
import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
application = get_wsgi_application()

import json
from crawling import getSBJ_ID, login
from graduations.models import Subject, Type



def main(year, semester):
    epoch = 0
    type_dic = {'1전선': Type.objects.get(type='1전선'), '1전심': Type.objects.get(type='1전심'), '1교직': Type.objects.get(type='1교직'), '1전필': Type.objects.get(type='1전필'), '일선': Type.objects.get(type='일선'), '교팔': Type.objects.get(type='기초'), '교선': Type.objects.get(type='일반')}
    session = login('201911019', '1q2w3e4r!')
    file_path = f'dataset/{year}_{semester}.json'
    with open(file_path, 'r') as f:
        SBJS = []
        datas = json.load(f)['dsUcsLectLsnPdoc']
        print(f'데이터: {len(datas)}')
        for data in datas:
            SBJ_NO = data['SBJ_NO']
            if SBJ_NO not in SBJS:
                for id in getSBJ_ID(session, 2019, 10, SBJ_NO):
                    type = data['CMP_DIV_NM']
                    Subject.objects.create(number=SBJ_NO, ecampus=id, name=data['SBJ_NM'], credit=data['CDT'], dept=data['EST_DEPT_INFO'], type=type_dic[type])
                    epoch += 1
                    print(epoch)
                SBJS.append(SBJ_NO)

if __name__ == '__main__':
    main(2019, 10)
