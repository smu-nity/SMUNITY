import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

def test():

    # 테스트 내용
    from ecampus import ecampus, subjects, createCourse
    session = ecampus('201911022', 'tpgjs7532#')
    print(subjects(session, 2019, 2022))
    createCourse('201911022', subjects(session, 2019, 2022))


if __name__ == '__main__':
    test()



