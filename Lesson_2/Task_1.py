# Необходимо собрать информацию о вакансиях на вводимую должность (используем input или через аргументы получаем должность) с сайтов HH(обязательно) и/или Superjob(по желанию). Приложение должно анализировать несколько страниц сайта (также вводим через input или аргументы). Получившийся список должен содержать в себе минимум:

import requests
from bs4 import BeautifulSoup
import pandas as pd
url = 'https://hh.ru/search/vacancy'

params = {
    'salary': '',
    'text': '',
    'page': '0'
}

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.116 YaBrowser/22.1.1.1543 Yowser/2.5 Safari/537.36'
}
dom = BeautifulSoup(requests.get(url, headers=headers, params=params).text, 'html.parser')
job_list = dom.find_all('div', {'class': ['vacancy-serp-item', 'vacancy-serp-item_redesigned']})
jobs = []
page_num = 0

response = requests.get(url)
dom = BeautifulSoup(response.text, 'html.parser')
while job_list:
    for job in job_list:
        title = job.find('a', {'data-qa': 'vacancy-serp__vacancy-title'})
        job_dict = {'title' : title.text.replace(',', ';')}
        job_dict['link'] = title.get('href').split('?')[0]
        salary = job.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'})

        if salary:
            salary = salary.getText().replace('\u202f', '').replace('\xa0', '')
            salary_list = salary.split()
            if salary_list[0].isalpha():
                job_dict['salary_min'] = None
                job_dict['salary_max'] = int(salary_list[1])
                job_dict['salary_currency'] = salary_list[-1]
            else:
                job_dict['salary_min'] = int(salary_list[0])
                job_dict['salary_max'] = int(salary_list[2])
                job_dict['salary_currency'] = salary_list[-1]

        else:
            job_dict['salary_min'] = None
            job_dict['salary_max'] = None
            job_dict['salary_currency'] = None

        job_dict['source'] = 'hh.ru'
        jobs.append(job_dict)

    page_num += 1
    params['page'] = str(page_num)
    dom = BeautifulSoup(requests.get(url, headers=headers, params=params).text, 'html.parser')
    job_list = dom.find_all('div', {'class': ['vacancy-serp-item', 'vacancy-serp-item_redesigned']})


df = pd.DataFrame(jobs)
print(df.to_string())
df.to_csv('output.csv', sep='\t', encoding='utf-8')