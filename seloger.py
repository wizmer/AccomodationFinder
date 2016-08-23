import re
import utils

def parse(urlname):

    soup=utils.get_soup(urlname)
    if soup is None: return None

    url=soup.find_all('article', id=re.compile('annonce-'))

    res=[]
    for r in url:
        infos=r.find('div', class_='listing_infos')

        data=dict()
        text=r.find('a',class_='amount').get_text()
        price=re.search('[0-9]+',text)
        properties=r.find('ul',class_='property_list').find_all('li')
        surface=""
        for prop in properties:
            match=re.search('([0-9]+,?[0-9]+) m',prop.get_text())
            if match is not None:
                surface = match.group(1).replace(',','.')
                break

        data['img']=r.find('div', class_='listing_photo_container').find('img')['src']
        data['price']=price.group(0)
        data['url']=infos.h2.a['href']
        data['title']=infos.h2.a.get_text()
        data['surface']=surface
        res.append(data)

    return res
