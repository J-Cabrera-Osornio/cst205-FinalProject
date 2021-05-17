import requests, webbrowser
from bs4 import BeautifulSoup

user_input = input("Say something to search:")
print("searching")

user_search = requests.get("https://google.com/search?q="+user_input)
#user_search = requests.get("https://google.com/search?q=go and ask google")

soup = BeautifulSoup(user_search.text, 'html.parser')

search_results = soup.select('.r a')

for link in search_results[:10]:
    #print(link.get('href'))
    actual_link = link.get('href')
    searching = webbrowser.open('https://google.com/'+actual_link)
    
print(searching)

#It was working fine but now I keep getting en error saying actual_link is not defined.
#After running the code several times I noticed sometimes it works and other times
#it doesn't
