import re
import utils

def parse(urlname):

    soup=utils.get_soup(urlname)
    if soup is None: return None

    url=soup.find_all('div', class_='lazyload_bloc')

    res=[]

    for r in url:
        data=dict()

        try:
            data['img']=r.find('img')['original']
        except KeyError:
            data['img']=''
        data['url']='http://www.paruvendu.fr'+r.a['href']
        data['title']=r.a['title']
        data['price']= re.search('([0-9]+)', r.find('span', class_='price2').get_text()).group(1)

        soup=utils.get_soup(data['url'])

        imdet=soup.find('ul', class_="imdet15-infoscles")
        if imdet is not None:
            for strong in imdet.find_all('strong'):
                if strong.string == 'Surface :':
                    data['surface']=re.search('[0-9]+,?[0-9]+', strong.next_sibling).group()
                    break
            res.append(data)

    return res
