from email.message import EmailMessage
from re import T
import requests
from bs4 import BeautifulSoup as BS
import csv


def get_response(url):
    #get respons from url
    resp = requests.get(url) #send requests to url
    return resp.text 

def get_data(html):  # finding tegs in data that we got here up
    soup = BS(html, 'lxml') # initializing object(instance) in Class 'BS' 
    grid = soup.find('div', class_='grid-deputs') #using method "find" on a 'soup' object
    deps = grid.find_all('div', class_ = 'dep-item')
    for dep in deps:
        try:
            image = dep.find('img').get('src')
        except:
            image = ''
        try:
            name = dep.find('a', class_ = 'name').text.strip()
        except:
            name = ''
        try:
            Fraction = dep.find('div', class_ = 'info').text.strip()
        except:
            Fraction = ''
        try:
            tel = dep.find('a', class_ = 'phone-call').text.strip()
        except:
            tel = ''
        try:
            email = dep.find('a', class_ = 'mail').text.strip()
        except:
            email = ''
        
        data = {
            'Image' : image,
            'Name' : name,
            'Fraction' : Fraction,
            'Phone' : tel,
            'Email' : email
        }
        write_to_csv(data)

def write_headers():
    with open("deputies.csv", 'w') as file:
        fieldnames = ['Name', "Fraction", "Phone", 'Email', "Image"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

def write_to_csv(data):
    with open("deputies.csv", 'a') as file:
        fieldnames = ['Name', "Fraction", "Phone", 'Email', "Image"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(data)


            

        


def main():
    write_headers()
    URL = 'http://www.kenesh.kg/ru/deputy/list/35'
    html = get_response(URL) #stores responded data from URL
    get_data(html) #feed html to get_data
main()