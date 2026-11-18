import requests 
from bs4 import BeautifulSoup
import csv 
date = input("Please enter a date in the format MM/DD/YYYY: ")
page = requests.get(f"https://www.yallakora.com/matches-center/?date={date}")

def main (page):
   #byte page string with method content 
   source = page.content
   #parsing the page using lxml parser , turn the byte into normal code html knowing 
   soup = BeautifulSoup(source, 'lxml')
   print (soup)

main (page)
