__author__ = 'Harsh'
import requests
import neo4j_integration
from lxml import etree
import pickle

url=requests.get('https://oceana.ca/en/marine-life/canadian-marine-life-encyclopedia','html.parser')
data=etree.HTML(url.text)

urls=[]
a=data.xpath("/html/body/main/div/section/article")
for i in a:
    urls.append(i.xpath('.//a')[0].get('href'))

print(urls)
print(len(urls))
main_list=[]
for url_link in urls:
    dict={}
    url=requests.get("https://oceana.ca"+url_link)
    data=etree.HTML(url.text)

    name=data.xpath("/html/body/article/div[2]/section[1]/section/div//h1/text()")
    bio=data.xpath("/html/body/article/div[2]/section[1]/section/div//p/text()")
    dict["Name"]=name[0]
    dict["Bio-name"]=bio[0]
    print(name)
    headings=data.xpath("/html/body/article/div[2]/section[3]/div/div[2]/div[2]//h2//text()")  # scraping headings
    headings=headings[0:-1]
    values=data.xpath("/html/body/article/div[2]/section[3]/div/div[2]/div[2]//p//text()")   # scraping its values

    for i in range(len(headings)):                                                                  # putting both in dict
        dict[headings[i]]=values[i].replace('\t','').replace('\n','')
    print(dict)
    main_list.append(dict)

print(main_list)

f=open("scraped_data.json","wb")
pickle.dump(main_list,f)
f.close()


neo4j_integration.run()