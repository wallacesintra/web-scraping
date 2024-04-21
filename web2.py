#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests

def extract_details(details):
    job_title = details[0].split('\n')[5].strip()
    company = details[0].split('\n')[8].strip()
    location = details[0].split('\n')[11].strip()
    job_type = details[0].split('\n')[13].strip()
    salaryy = details[0].split('\n')[15].strip()
    job_function = details[0].split('\n')[20].strip()

    return {
        "job_title": job_title,
        "company": company,
        "location": location,
        "job_type": job_type,
        "salary": salaryy,
        "job_function": job_function
    }

def url_to_soup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # container = soup.find('div', class_= 'w-full')
    # container = soup.select_one('.w-full .flex items-center .text-sm text-link-500 .text-loading-animate text-loading-animate-link')
    container = soup.find('div',class_='w-full')
    print(container.findChild('p', class_='text-sm text-gray-500 text-loading-animate inline-block'))

    child = soup.find('.relative mb-3 text-lg font-medium break-words focus:outline-none metrics-apply-now text-link-500 text-loading-animate')
    child2 = soup.find('a', class_='relative mb-3 text-lg font-medium break-words focus:outline-none metrics-apply-now text-link-500 text-loading-animate')
    # print(container)
    # print(child2.findChild('p', class_='text-lg font-medium break-words text-link-500').text)

    # job title
    job_title = child2.findChildren('p', class_='text-lg font-medium break-words text-link-500')[0].text

    # print(job_title)
    # print(child.parent)


    job_container = soup.find('div', class_= 'flex flex-wrap mt-3 text-sm text-gray-500 md:py-0')
    location = job_container.findChildren('span', class_='mb-3 px-3 py-1 rounded bg-brand-secondary-100 mr-2 text-loading-hide')[0].text
    job_type = job_container.findChildren('span', class_='mb-3 px-3 py-1 rounded bg-brand-secondary-100 mr-2 text-loading-hide')[1].text
    salary = job_container.findChildren('span', class_='mb-3 px-3 py-1 rounded bg-brand-secondary-100 mr-2 text-loading-hide')[2].text
    # print(location)
    # print(job_type)
    # print(salary)

    # job function
    # kazi = soup.find('p', class_='text-sm text-gray-500 text-loading-animate inline-block')
    # print(kazi.parent.text)
    # print(kazi.parent.text.split('•'))

    # details_array = kazi.parent.text.split('•')
    # print(details_array)
    # print(extract_details(details_array))
    # print(details_array.index('Job Function'))
    # print(job_function)


url_to_soup("https://www.brightermonday.co.ke/jobs/accounting-auditing-finance")

