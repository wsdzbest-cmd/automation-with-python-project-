
import requests 
from bs4 import BeautifulSoup
import csv 


date = input("Please enter a date in the format MM/DD/YYYY: ")

page = requests.get(f"https://www.yallakora.com/matches-center/?date={date}")

def main (page) :
    #byte page string with method content 
    source = page.content

    #parsing the page using lxml parser , turn the byte into normal code html knowing 
    soup = BeautifulSoup(source, 'lxml')

    matches_details = []
    championships= soup.find_all("div", {'class':'matchCard'})

    def get_matches_info (championship):
       
       championship_title =championship.contents[1].find("h2").text.strip()

       #all matches is list, where each element is dev class item finish liItem, and each element is a match
       all_matches = championship.contents[3].find_all("div", {'class':'item finish liItem'})


       number_of_matches = len(all_matches)

       for i in range (number_of_matches):
          #get match names 
          team_a = all_matches[i].find("div", {'class':'teamA'}).text.strip()
          team_b = all_matches[i].find("div", {'class':'teamB'}).text.strip()

          #get the match score 
          result = all_matches[i].find("div",{'class':'MResult'}).find_all('span',{'class':"score"})
          score = f"{result[0].text.strip()} - {result[1].text.strip()}"

          #get match time 
          time_match = all_matches[i].find("div",{'class':'MResult'}).find('span', {'class':'time'}).text.strip()

          #append match details to the list 
          matches_details.append({
              'champion name': championship_title,
              'Team A': team_a,
              'Team B': team_b,
              "Time": time_match,
              "Score":score
          })
    for championship in championships:
       get_matches_info(championship)

   #get the keys of the list 
    keys = matches_details[0].keys()
    

    #open the csv file and write the header and rows into it   
    with open ("C:/Users/DELL/Documents/yallakora/yallkora.csv",'w',encoding='utf-8-sig') as output_file:
     
     #write the keys as headers and the element as row yalllacora-scarping 
     dict_writer = csv.DictWriter(output_file,keys)

     dict_writer.writeheader()

     dict_writer.writerows(matches_details)

    
    print("created csv completed")

main (page)