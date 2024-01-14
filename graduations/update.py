# 장고 환경
import os
import sys
import json
import requests
from bs4 import BeautifulSoup as bs
from django.core.wsgi import get_wsgi_application

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)) + '/app')))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
application = get_wsgi_application()

from accounts.models import Department, Year
from graduations.models import Subject, Major, Culture
from config.settings import SUBTYPE_CHOICES_S, SUBTYPE_CHOICES_E


# 과목 업데이트 스크립트
def subjects(file_path):
    with open(file_path, 'r', encoding='UTF-8') as f:
        datas = json.load(f)['dsUcsLectLsnPdoc']
        for data in datas:
            SBJ_NO = data['SBJ_NO']
            sbj = Subject.objects.filter(number=SBJ_NO)
            if not sbj:
                Subject.objects.create(number=SBJ_NO, name=data['SBJ_NM'], credit=data['CDT'], dept=data['EST_DEPT_INFO'], type=data['CMP_DIV_NM'])
            else:
                sbj.update(name=data['SBJ_NM'], credit=data['CDT'], dept=data['EST_DEPT_INFO'], type=data['CMP_DIV_NM'])


# 전공 과목 업데이트 스크립트
def major(dept, url):
    request = requests.get(url)
    source = request.text
    soup = bs(source, "html.parser")
    datas = soup.find_all('tr')[1:]
    for data in datas:
        subject = data.find_all('td')
        number, name = subject[3].text, subject[4].text.split('/')[1]
        credit, type = int(float(subject[5].text)), subject[2].text
        sub, _ = Subject.objects.get_or_create(number=number, defaults={'name': name, 'credit': credit, 'dept': dept.name, 'type': type})
        Major.objects.create(department=dept, subject=sub, grade=subject[0].text, semester=subject[1].text, type=subject[2].text)


# 학년도 업데이트 스크립트
def year():
    datas = [
        {'year': '2017', 'major_i': 15, 'major_s': 45, 'culture': 36, 'culture_cnt': 3, 'all': 130},
        {'year': '2018', 'major_i': 15, 'major_s': 45, 'culture': 33, 'culture_cnt': 3, 'all': 130},
        {'year': '2019', 'major_i': 15, 'major_s': 45, 'culture': 33, 'culture_cnt': 3, 'all': 130},
        {'year': '2020', 'major_i': 15, 'major_s': 45, 'culture': 33, 'culture_cnt': 4, 'all': 130},
        {'year': '2021', 'major_i': 15, 'major_s': 45, 'culture': 33, 'culture_cnt': 4, 'all': 130},
        {'year': '2022', 'major_i': 15, 'major_s': 45, 'culture': 33, 'culture_cnt': 4, 'all': 130},
        {'year': '2023', 'major_i': 15, 'major_s': 60, 'culture': 33, 'culture_cnt': 4, 'all': 130}
    ]
    for data in datas:
        Year.objects.create(year=data['year'], major_i=data['major_i'], major_s=data['major_s'], culture=data['culture'], culture_cnt=data['culture_cnt'], all=data['all'])


# 학과 업데이트 스크립트
def departments():
    datas = [
        {'college': '융합공과대학', 'name': '컴퓨터과학전공', 'type': '공학', 'url': 'https://cs.smu.ac.kr/cs/admission/curriculum.do?&srYear=2023&srShyr=all&srSust=03005'},
        {'college': '융합공과대학', 'name': '전기공학전공', 'type': '자연', 'url': 'https://electric.smu.ac.kr/electric/admissions/curriculum.do?&srYear=2023&srShyr=all&srSust=03208'},
        {'college': '융합공과대학', 'name': '지능IOT융합전공', 'type': '공학', 'url': 'https://www.smu.ac.kr/aiot/admission/curriculum.do?&srYear=2023&srShyr=all&srSust=03209'},
        {'college': '융합공과대학', 'name': '게임전공', 'type': '공학', 'url': 'https://game.smu.ac.kr/game01/admission/curriculum.do?&srYear=2023&srShyr=all&srSust=03006'},
        {'college': '융합공과대학', 'name': '애니메이션전공', 'type': '예술', 'url': 'https://animation.smu.ac.kr/animation/admission/curriculum.do?&srYear=2023&srShyr=all&srSust=03007'},
        {'college': '융합공과대학', 'name': '휴먼지능정보공학전공', 'type': '공학', 'url': 'https://hi.smu.ac.kr/hi/admissions/curriculum.do?&srYear=2023&srShyr=all&srSust=03204'},
        {'college': '융합공과대학', 'name': '핀테크전공', 'type': '공학', 'url': 'https://fbs.smu.ac.kr/fbs/admission/curriculum.do?&srYear=2023&srShyr=all&srSust=03205'},
        {'college': '융합공과대학', 'name': '빅데이터융합전공', 'type': '공학', 'url': 'https://fbs.smu.ac.kr/fbs/admission/curriculum_big.do?&srYear=2023&srShyr=all&srSust=03206'},
        {'college': '융합공과대학', 'name': '스마트생산전공', 'type': '공학', 'url': 'https://fbs.smu.ac.kr/fbs/admission/curriculum_smart.do?&srYear=2023&srShyr=all&srSust=03207'},
        {'college': '융합공과대학', 'name': '생명공학전공', 'type': '자연', 'url': 'https://biotechnology.smu.ac.kr/biotechnology/admission/curriculum.do?&srYear=2023&srShyr=all&srSust=0300'},
        {'college': '융합공과대학', 'name': '화학에너지공학전공', 'type': '자연', 'url': 'https://energy.smu.ac.kr/cee/admission/curriculum.do?&srYear=2023&srShyr=all&srSust=03001'},
        {'college': '융합공과대학', 'name': '화공신소재전공', 'type': '자연', 'url': 'https://ichem.smu.ac.kr/ichemistry/admission/curriculum.do?&srYear=2023&srShyr=all&srSust=03002'},
        {'college': '융합공과대학', 'name': '한일문화콘텐츠전공', 'type': '인문', 'url': None},
        {'college': '인문사회과학대학', 'name': '역사콘텐츠전공', 'type': '인문', 'url': 'https://history.smu.ac.kr/history/admission/curriculum.do?&srYear=2023&srShyr=all&srSust=02988'},
        {'college': '인문사회과학대학', 'name': '지적재산권전공', 'type': '사회', 'url': 'https://cr.smu.ac.kr/cc/admission/curriculum.do?&srYear=2023&srShyr=all&srSust=02989'},
        {'college': '인문사회과학대학', 'name': '문헌정보학전공', 'type': '사회', 'url': 'https://libinfo.smu.ac.kr/libinfo/admission/curriculum.do?&srYear=2023&srShyr=all&srSust=02990'},
        {'college': '인문사회과학대학', 'name': '공간환경학부', 'type': '사회', 'url': 'https://space.smu.ac.kr/space/admission/curriculum.do?&srYear=2023&srShyr=all&srSust=00962'},
        {'college': '인문사회과학대학', 'name': '행정학부', 'type': '사회', 'url': 'https://public.smu.ac.kr/public/admission/curriculum.do?&srYear=2023&srShyr=all&srSust=03183'},
        {'college': '인문사회과학대학', 'name': '가족복지학과', 'type': '사회', 'url': 'https://smfamily.smu.ac.kr/smfamily/admission/curriculum.do?&srYear=2023&srShyr=all&srSust=00951'},
        {'college': '인문사회과학대학', 'name': '국가안보학과', 'type': '인문', 'url': 'https://ns.smu.ac.kr/sdms/admission/curriculum.do?&srYear=2023&srShyr=all&srSust=00964'},
        {'college': '사범대학', 'name': '국어교육과', 'type': '인문', 'url': 'https://koredu.smu.ac.kr/koredu/admission/curriculum.do?&srYear=2023&srShyr=all&srSust=00971'},
        {'college': '사범대학', 'name': '영어교육과', 'type': '인문', 'url': 'https://engedu.smu.ac.kr/engedu/admission/curriculum.do?&srYear=2023&srShyr=all&srSust=00972'},
        {'college': '사범대학', 'name': '교육학과', 'type': '인문', 'url': 'https://learning.smu.ac.kr/peda/admission/curriculum.do?&srYear=2023&srShyr=all&srSust=00975'},
        {'college': '사범대학', 'name': '수학교육과', 'type': '자연', 'url': 'https://mathed.smu.ac.kr/mathedu/admission/curriculum.do?&srYear=2023&srShyr=all&srSust=00976'},
        {'college': '경영경제대학', 'name': '경제금융학부', 'type': '사회', 'url': 'https://econo.smu.ac.kr/economic/admission/curriculum.do?&srYear=2023&srShyr=all&srSust=01178'},
        {'college': '경영경제대학', 'name': '경영학부', 'type': '사회', 'url': None},
        {'college': '경영경제대학', 'name': '글로벌경영학과', 'type': '사회', 'url': None},
        {'college': '경영경제대학', 'name': '융합경영학과', 'type': '사회', 'url': 'https://imgmt.smu.ac.kr/cm/admission/curriculum.do?&srYear=2023&srShyr=all&srSust=01181'},
        {'college': '문화예술대학', 'name': '식품영양학전공', 'type': '자연', 'url': 'https://food.smu.ac.kr/foodnutrition/admission/curriculum.do?&srYear=2023&srShyr=all&srSust=02994'},
        {'college': '문화예술대학', 'name': '의류학전공', 'type': '자연', 'url': 'https://fashionindustry.smu.ac.kr/clothing2/admission/curriculum.do?srYear=2023&srSust=02995&srShyr=all'},
        {'college': '문화예술대학', 'name': '스포츠건강관리전공', 'type': '예술', 'url': 'https://smpe.smu.ac.kr/smpe/admission/curriculum.do?srYear=2023&srSust=02997&srShyr=all'},
        {'college': '문화예술대학', 'name': '무용예술전공', 'type': '예술', 'url': 'https://dance.smu.ac.kr/dance/undergraduate/undergraduate_curriculum.do?&srYear=2023&srShyr=all&srSust=02998'},
        {'college': '문화예술대학', 'name': '조형예술전공', 'type': '예술', 'url': 'https://finearts.smu.ac.kr/finearts/admission/curriculum.do?&srYear=2023&srShyr=all&srSust=02991'},
        {'college': '문화예술대학', 'name': '생활예술전공', 'type': '예술', 'url': 'https://smulad.smu.ac.kr/smulad/admission/curriculum.do?&srYear=2023&srShyr=all&srSust=02992'},
        {'college': '문화예술대학', 'name': '음악학부', 'type': '예술', 'url': 'https://music.smu.ac.kr/music/admission/curriculum.do?&srYear=2023&srShyr=all&srSust=01132'},
    ]
    for data in datas:
        Department.objects.create(college=data['college'], name=data['name'], type=data['type'], url=data['url'])


# 상명핵심역량교양 과목 업데이트 스크립트
def culture_e():
    dic = {
        '전문지식탐구역량': ['HALF9398', 'HALF9408', 'HALR1269'],   # HALF9425, HALF9426
        '창의적문제해결역량': ['HALF9427', 'HALR1040', 'HALR1230'],  # HALF9428
        '융복합역량': ['HALF9429', 'HALF9432', 'HALR1271'],  # HALF9430, HALF9431
        '다양성존중역량': ['HALF9435'],    # HALF9433, HALF9434, HALF9436
        '윤리실천역량': ['HALF9404', 'HALF9438', 'HALR1038']  # HALF9437
    }
    types = list(map((lambda x: x[0]), SUBTYPE_CHOICES_E))
    for type in types:
        numbers = dic[type]
        for number in numbers:
            try:
                subject = Subject.objects.get(number=number)
                Culture.objects.create(subject=subject, type='교필', domain='핵심', subdomain=type)
            except:
                print(number)


# 균형교양 과목 업데이트 스크립트
def culture_s():
    dic = {
        '인문': ['HALF0102', 'HALF0122', 'HALF0202', 'HALF0302', 'HALF9013', 'HALF9014', 'HALF9015', 'HALF9302', 'HALF9305', 'HALF9338', 'HALF9358', 'HALF9374'],     # HALF9439
        '사회': ['HALF4033', 'HALF5013', 'HALF9030', 'HALF9031', 'HALF9245', 'HALF9266', 'HALF9280', 'HALF9320', 'HALF9343', 'HALF9440', 'HALR1041', 'HALR1235'],     # HALF0447, HALF9037, HALF9326, HALF9379, HALF9421
        '자연': ['HALF0502', 'HALF0537', 'HALF9041', 'HALF9239', 'HALF9252', 'HALF9362', 'HALF9403'],     # HALF9321, HALF9378
        '공학': ['HALF6024', 'HALF9319', 'HALF9329', 'HALF9405', 'HALF9420', 'HALF9441'],
        '예술': ['HALF0601', 'HALF6071', 'HALF6072', 'HALF7023', 'HALF9061', 'HALF9356']      # HALF0628
    }
    types = list(map((lambda x: x[0]), SUBTYPE_CHOICES_S))
    for type in types:
        numbers = dic[type]
        for number in numbers:
            try:
                subject = Subject.objects.get(number=number)
                Culture.objects.create(subject=subject, type='교선', domain='균형', subdomain=type)
            except:
                print(number)


# 전공 과목 업데이트 스크립트
def majors():
    departments = Department.objects.all()
    for department in departments:
        print(department)
        if department.url:
            major(department, department.url)


# 전체 업데이트 스크립트 (17학년도 ~ 22학년도)
def subjects_all():
    path = 'dataset'
    files = os.listdir(path)
    files = sorted(files, key=lambda x: int(x.split('.')[0]))
    for file in files:
        print(file)
        file_path = f'{path}/{file}'
        subjects(file_path)


if __name__ == '__main__':
    # subjects_all()
    # year()
    # departments()
    majors()
    # culture_e()
    # culture_s()
