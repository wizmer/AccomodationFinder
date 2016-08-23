import re
import utils

def parse(urlname):

    soup=utils.get_soup(urlname)
    if soup is None: return None

    url=soup.find('section', class_='tabsContent').ul.find_all('li')

    res=[]
    for r in url:
        data=dict()
        text=r.find('h2',class_='item_title').get_text()
        data['title']=r.a['title']
        data['url']='https://'+re.search('(www.+)$', r.a['href']).group(1)
        data['price']= re.search('([0-9]+)', r.find('h3', class_='item_price').get_text()).group(1)
        imgTag=r.find('span', class_='lazyload')
        data['img']=''
        if imgTag:
            data['img']=imgTag['data-imgsrc'][2:]

        soup=utils.get_soup(data['url'])
        for r in soup.find_all('h2',class_='clearfix'):
            if r.span.string == 'Surface':
                data['surface']=re.search('[0-9]+,?[0-9]+', r.find('span', class_='value').get_text()).group()
                break

        res.append(data)

    return res
