
from bs4 import BeautifulSoup
import urllib2

def get_soup(urlname):
    opener = urllib2.build_opener()
    # opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11')]
    # opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/51.0.2704.79 Chrome/51.0.2704.79 Safari/537.36')]

    opener.addheaders.append(('Cookie', 'SearchAnnDep=06; __uzma=mac27c0003-3bf1-48e6-b5e8-b4f7ff1340139021; __uzmb=1471610349; __uzmc=177921346134; __uzmd=1471610349; dtCookie=|U2VMb2dlcnww'))

    response = opener.open(urlname)
    page = response.read()

    soup=BeautifulSoup(page,"html.parser")
    error=any(msg.get_text()=="Une erreur s'est produite" for msg in soup.find_all('span', class_="fil_1"))

    if error: return None
    return soup
