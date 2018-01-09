# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 17:03:51 2018

@author: jjvmak
"""

import urllib, json
from sklearn.svm import LinearSVC
from sklearn.datasets import make_classification
import codecs
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

with urllib.request.urlopen("https://api.turku.fi/feedback/v1/requests.json") as url:
    data = json.loads(url.read())
     
#kaikki palautteet 
print(len(data))

asd = []
for i in range(0, len(data)):
    asd.append(data[i]['service_name'])
    
#uniikit luokat 
asdSet = set(asd)
print(len(asdSet))

#yleisin luokka 
print(max(set(asd), key=asd.count)) 

#harvinaisin luokka 
print(min(set(asd), key=asd.count)) 

sixtyPercent = int(round(len(data)*0.6))
twentyPercent = int(round(len(data)*0.2))

#train data 
trainData = []
trainStr = []
for i in range(0, sixtyPercent):
    trainData.append(data[i])
    trainStr.append(data[i]['description'])

#deval data
devalData = []
devalStr = []
for i in range(sixtyPercent, sixtyPercent+twentyPercent):
    devalData.append(data[i])
    devalStr.append(data[i]['description'])
    
#test data
testData = []
testStr = []
for i in range(sixtyPercent+twentyPercent, len(data)):
    testData.append(data[i])
    testStr.append(data[i]['description'])
    

asdList = list(asdSet)
features = []
for i in range(0, len(trainData)):
    tmp = trainData[i]['service_name']
    for n in range(0, len(asdList)):
        if (tmp == asdList[n]):
            features.append(n)
            
deval_features = []
for i in range(0, len(devalData)):
    tmp = devalData[i]['service_name']
    for n in range(0, len(asdList)):
        if (tmp == asdList[n]):
            deval_features.append(n)
            
            
test_features = []
for i in range(0, len(testData)):
    tmp = testData[i]['service_name']
    for n in range(0, len(asdList)):
        if (tmp == asdList[n]):
            test_features.append(n)
        
        
vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(1,2), use_idf=False, norm='l2')
vectorizer.fit(trainStr)

train_vectors = vectorizer.transform(trainStr).toarray()
devel_vectors = vectorizer.transform(devalStr).toarray()
test_vectors = vectorizer.transform(testStr).toarray()

classifier = SVC(kernel='linear', C=1.3)

classifier.fit(train_vectors, features)

lol = (classifier.predict(vectorizer.transform(['Hei! Edesmennyt äitini osti aikoinaan Turusta huutokaupasta vanhan nuken, joka ilmeisesti on Martta-nukke. Olen kiinnostunut tietämään mm. sen, kuinka vanha se on. Onko museokeskuksessa henkilöä, joka on perehtynyt nukkeihin?.']).toarray())[0])
print(asdList[lol])
#print(asdList[])

#devel_predictions = classifier.predict(devel_vectors)

#print("Devel set accuracy: %s" % accuracy_score(deval_features, devel_predictions))
#print ("Test set accuracy: %s" % accuracy_score(test_features, classifier.predict(test_vectors)))






            