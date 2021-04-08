import requests
import pandas as pd
from PIL import Image

image_new = pd.read_csv("cleaned_complete.csv")
image_unique = image_new.drop_duplicates("ActorName")
image_unique.ActorName = image_unique.ActorName.str.replace(' ', '_')
female = image_unique[image_unique.Gender == "Female"]
male = image_unique[image_unique.Gender == "Male"]
halfF = female['ActorName'].values
namefileF = ['/Users/valencialie/Desktop/CZ1016_DS2/kdrama/Images/Female/' + i for i in halfF +".png"]
newF = ['/Users/valencialie/Desktop/CZ1016_DS2/kdrama/Images/Female/' + i for i in halfF +".jpeg"]
halfM = male['ActorName'].values
namefileM = ['/Users/valencialie/Desktop/CZ1016_DS2/kdrama/Images/Male/' + i for i in halfM +".png"]
newM = ['/Users/valencialie/Desktop/CZ1016_DS2/kdrama/Images/Male/' + i for i in halfM +".jpeg"]


list1 = list(female.Image) #URL 
list2 = list(namefileF) #FILE NAME
list3 = list(male.Image) #URL 
list4 = list(namefileM) #FILE NAME

b =0
for a in list1:
    url = a
    r = requests.get(url)
    with open(list2[b], 'wb') as f:
        f.write(r.content)
    b+=1

 # Retrieve HTTP meta-data
    print(r.status_code)
    print(r.headers['content-type'])
    print(r.encoding)

b =0
a=0
for a in list3:
    url = a
    r = requests.get(url)
    with open(list4[b], 'wb') as f:
        f.write(r.content)
    b+=1

 # Retrieve HTTP meta-data
    print(r.status_code)
    print(r.headers['content-type'])
    print(r.encoding)

c = 0
e = 0
for c in list4:
    img = Image.open(c).convert('LA').convert('RGB')
    img.save(newM[e])
    e+=1

d = 0
f = 0
for d in list2:
    img = Image.open(d).convert('LA').convert('RGB')
    img.save(newF[f])
    f+=1
