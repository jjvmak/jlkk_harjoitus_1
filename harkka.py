# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 17:03:51 2018

@author: jjvmak
"""

import urllib, json
with urllib.request.urlopen("https://api.turku.fi/feedback/v1/requests.json") as url:
    data = json.loads(url.read())
     
#kaikki palautteet 2890
print(len(data))

asd = []
for i in range(0, len(data)):
    asd.append(data[i]['service_name'])
    
#uniikit luokat 112
asdSet = set(asd)
print(len(asdSet))

#yleisin luokka 'Kadut ajoradat'
print(max(set(asd), key=asd.count)) 

#harvinaisin luokka 'Kirjastopalvelut, tapahtumat ja näyttelyt'
print(min(set(asd), key=asd.count)) 


    

    



    
