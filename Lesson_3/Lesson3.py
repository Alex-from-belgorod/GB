# 1. Развернуть у себя на компьютере/виртуальной машине/хостинге MongoDB и реализовать функцию, которая будет
# добавлять только новые вакансии в вашу базу.
# 2. Написать функцию, которая производит поиск и выводит на экран
# вакансии с заработной платой больше введённой суммы (необходимо анализировать оба поля зарплаты). То есть цифра
# вводится одна, а запрос проверяет оба поля

from pymongo import MongoClient  # подключаем необходимые библиотеки
import parser_ls2 as pars   # Переносим со воторого урока парсер hh.ru
import pprint as pp


def init_db():
    global parse_string
    global db
    parse_string = '2d 3d artist'
    client = MongoClient('127.0.0.1', 27017)
    db = client[parse_string.replace(' ', '_')]


def update_db():
    if db.jobs is None:
        db.jobs.insert_many(pars.parse_jobs(parse_string))
    else:
        for job in pars.parse_jobs(parse_string):
            if not db.jobs.find_one({'link': job['link']}):
                db.jobs.insert_one(job)


def expected_cash(db, alot=50000):
    for job in db.jobs.find({'$and':
                                 [{'salary_currency': "руб."},
                                  {'$or':
                                       [{'salary_min': {'$gt': alot}}, {'salary_max': {'$gt': alot}}
                                        ]}]}):
        pp.print(job)


init_db()
update_db()
expected_cash(db)

