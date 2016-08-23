from bs4 import BeautifulSoup
import urllib2
import re

def parse(urlname):

    f=urllib2.urlopen(urlname).read()

    soup = BeautifulSoup(f, 'html.parser')

    url=soup.find_all('div',id=re.compile("bloc-vue"))

    res=[]

    for r in url:
        title=r.find(class_='js-item-title').get_text()
        data=dict()
        text=r.find('span',class_='price-label').get_text()
        price=re.search('[0-9]+',text)
        surface=re.search('([0-9]+,?[0-9]+)\s?m2',title)
        data['surface']=surface.group(1).replace(',','.')
        data['price']=price.group(0)
        data['url']='http://www.explorimmo.com/'+r.find(class_='js-item-title')['href']
        data['img']=r.find('img', itemprop='image')['src']
        data['title']=title
        res.append(data)

    return res
