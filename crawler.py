import urllib.request
from bs4 import BeautifulSoup
import queue
q =  queue.Queue()
visited = []
def crawl(x):
    response = urllib.request.Request(x)
    html=urllib.request.urlopen(response).read()
    soup = BeautifulSoup(html,'html.parser')
    s = soup.prettify()
    for link in soup.find_all('a'):
            try:
                check = link.get('href')[0:4]
            except TypeError:
                check = 'No link'
            if(check == "http"):
          #      if(not(link.get('href') in visited)):
                    q.put(link.get('href'))

x = "https://www.polygon.com"
crawl(x)
visited.append(x)
#print(visited)
counter = 1
while(counter<=10):
    x = q.get()
    visited.append(x)
    print(visited)
    print(x)
    #crawl(x)
    counter += 1
