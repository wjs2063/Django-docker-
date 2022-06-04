from html.parser import HTMLParser
import requests
from bs4 import BeautifulSoup
from random import choices,sample
import pymysql

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='Gusdl7797@',
                       charset='utf8')

with conn:
    with conn.cursor() as cur:
            cur.execute('CREATE DATABASE IF NOT EXISTS testdb')
        
url="https://www.dhlottery.co.kr/gameResult.do?method=statByNumber"

def crawling(url:str)->tuple:
    #해당 url 의 모든 html 정보를 가져옴
    response = requests.get(url)
    html=response.text
    html=BeautifulSoup(html,'html.parser')

    htmls=html.find_all(attrs={'class':'tbl_data tbl_data_col'})
    htmls=htmls[0].select("tbody>tr>td")

    #number->{0,3,6,9 . . .} 빈도-->{2,5,8,11. . .}
    lottotable=dict()
    for i in range(0,len(htmls),3):
        lottotable[htmls[i].text]=int(htmls[i+2].text)
    cnt=sum(lottotable.values())

    for key in lottotable.keys():
        lottotable[key]=lottotable[key]/cnt
    lottonumber=[i for i in range(1,45+1)]
    weights=lottotable.values()
    return lottonumber,weights
lottolist=[]

lottonumber,weights=crawling(url)

n=int(input().strip())

while n>1:
    arr=choices(lottonumber,weights=weights,k=6)
    # 중복확인
    if len(arr)-len(list(set(arr)))>=1:
        continue
    lottolist.append(sorted(arr))
    n-=1