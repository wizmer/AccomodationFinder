import smtplib
import sys
import explorimmo
import seloger
import mailer
import leboncoin
import paruvendu

dicts={
    "explorimmo": 'http://www.explorimmo.com/immobilier-location-appartement-villeneuve+loubet+06270.html?location=biot%20(06410),cagnes%20sur%20mer%20(06800),valbonne%20(06560),la%20colle%20sur%20loup%20(06480)&priceMax=800&areaMin=30&proximityRange=5',
    "seloger": 'http://www.seloger.com/list.htm?ci=60018,60027,60161,60152&org=advanced_search&idtt=1&refannonce=&pxmin=&pxmax=800&surfacemin=30&surfacemax=&idtypebien=1&idtypebien=2&surf_terrainmin=&surf_terrainmax=&etagemin=&etagemax=&idtypechauffage=&idtypecuisine=',
    'leboncoin': 'https://www.leboncoin.fr/locations/offres/rhone_alpes/occasions/?th=1&location=Villeneuve-Loubet%2006270%2CCagnes-sur-Mer%2006800&mre=800&sqs=4',
    'paruvendu': 'http://www.paruvendu.fr/immobilier/annonceimmofo/liste/listeAnnonces?tt=5&tbApp=1&tbDup=1&tbChb=1&tbLof=1&tbAtl=1&tbPla=1&tbMai=1&tbVil=1&tbCha=1&tbPro=1&tbHot=1&tbMou=1&tbFer=1&at=1&nbp0=99&nbp1=99&sur0=30&px1=800&pa=FR&co=1&ddlTri=dateMiseAJour&ddlOrd=desc&ddlFiltres=nofilter&codeINSEE=06161,06027,06018,06152,'
}

banned=[
    'https://www.leboncoin.fr/locations/1008328351.htm?ca=22_s',
    'https://www.leboncoin.fr/locations/950448365.htm?ca=22_s',
    'https://www.leboncoin.fr/locations/1006274094.htm?ca=22_s',
    'https://www.leboncoin.fr/locations/997643130.htm?ca=22_s',
    'https://www.leboncoin.fr/locations/995663879.htm?ca=22_s',
    'https://www.leboncoin.fr/locations/1003044602.htm?ca=22_s',
    'https://www.leboncoin.fr/locations/1003550639.htm?ca=22_s',
    'https://www.leboncoin.fr/locations/1004306753.htm?ca=22_s',
    'http://www.seloger.com/annonces/locations/appartement/cagnes-sur-mer-06/le-cros-de-cagnes/98672799.htm?ci=60018,60027,60152,60161&idtt=1&idtypebien=1,2&org=advanced_search&pxmax=800&surfacemin=35',
    'http://www.seloger.com/annonces/locations/appartement/cagnes-sur-mer-06/le-cros-de-cagnes/98672799.htm?ci=60018,60027,60152,60161&idtt=1&idtypebien=1,2&org=advanced_search&pxmax=800&surfacemin=30'
    'http://www.seloger.com/annonces/locations/appartement/cagnes-sur-mer-06/le-cros-de-cagnes/98672799.htm?ci=60018,60027,60152,60161&idtt=1&idtypebien=1,2&org=advanced_search&pxmax=800&surfacemin=40',
    'https://www.leboncoin.fr/locations/1001732980.htm?ca=22_s',

]

res=[]
for key, urlname in dicts.items():
    result=globals()[key].parse(urlname)
    if result is None:
        msg='Problem with parser: '+d
        mailer.sendmail(msg)
        sys.exit(msg)
    res += result



message=''
for r in res:
    r['price per meter'] = float(r['price'])/float(r['surface'])

res.sort( key=lambda x: x['price per meter'])

def formatMsg(d, hyperlink=False):
    s="<td>"
    if hyperlink: s+= '<a href="'+ r['url'] + '">'
    s+='<font size="5">' + d.encode('ascii','ignore') + '</font>'
    if hyperlink: s+="</a>"
    s += "</td>"
    return s

for r in res:
    if r['url'] in banned:
        continue
    message+= '<tr>' +  \
              formatMsg('%.2f' % r['price per meter']) + \
              formatMsg(r['price']) + \
              formatMsg(r['surface']) + \
              formatMsg(r['title'], hyperlink=True) + \
              '<a href="'+ r['url'] + '"><img src="' + r['img'] + '"></a>' + \
              "</tr>"

mailer.sendmail(message)

