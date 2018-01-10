import requests
import pandas as pd
from bs4 import BeautifulSoup
Coef_pickrate = 0.2
Coef_winrate = 1-Coef_pickrate
res = requests.get('https://www.overbuff.com/heroes')
#用request把網頁的原始碼抓下來存成text檔
#因為這個網頁並沒有Javascript渲染的內容，所以我們這邊沒有使用到Selenium
#print(res.text)



#把text檔以lxml方式解析，優點快 正確率較高
soup = BeautifulSoup(res.text, "lxml")

#怕輸出的字符串中可能包含了很多空格或空行，所以使用stripped_strings而不使用strings
#str()一般是将数值转成字符串。 
#repr()是将一个对象转成字符串显示，注意只是显示用，有些对象转成字符串没有直接的意思。
#如list,dict使用str()是无效的，但使用repr可以，这是为了看它们都有哪些值，为了显示之用。 
this_month=[]
Hero = []
PickRate =[]
WinRate = []
for string in soup.tbody.stripped_strings:
    this_month.append(str(string).strip('%'))
print (this_month)

this_month_array = [ [] * 3 for i in range(26) ]

for k in range(len(this_month)):
    if (k%6) == 0:
        Hero.append(this_month[k])
    elif (k%6) == 2:
        PickRate.append(this_month[k])
    elif (k%6) == 3:
        WinRate.append(this_month[k])

for i in range(len(soup.tbody.contents)):
    this_month_array[i].append(Hero[i])
    this_month_array[i].append(PickRate[i])
    this_month_array[i].append(WinRate[i])

df =  pd.DataFrame(this_month_array, columns = ["Hero", "Pick_Rate", "Win_Rate"]) # 指定欄標籤名稱


EngName = ["Doomfist","Genji","McCree","Pharah","Reaper","Soldier: 76",
"Sombra","Tracer","Bastion","Hanzo","Junkrat","Mei",
"Torbjörn","Widowmaker","D.Va","Orisa","Reinhardt",
"Roadhog","Winston","Zarya","Ana","Lúcio","Mercy","Symmetra","Zenyatta","Moira"]
ChiName = ["毀滅拳王","源氏","麥卡利","法拉","死神",
"士兵76","駭影","閃光","壁壘機兵","半藏","炸彈鼠","小美"
,"托比昂","奪命女","D.VA","歐瑞莎","萊茵哈特","攔路豬",
"溫斯頓","札莉雅","安娜","路西歐","慈悲","辛梅塔","禪亞塔","莫伊拉"]
nChiName = []
for k in range(len(df)):
    for i in range(len(EngName)):
        if df.Hero[k]==EngName[i]:
            nChiName.append(ChiName[i])
#for i in range(len(nChiName)):
 #   print(str(i)+nChiName[i])
df.insert(3, "中文名", nChiName)
print (df)

Score = []

for i in range(len(df)):
    Score.append( Coef_pickrate*float(df.Pick_Rate[i]) + Coef_winrate*float(df.Win_Rate[i]))
df.insert(3, 'Score', Score)
df = df.sort_values(by = 'Score',ascending = False) #透過指定欄位的數值排序 
print (df)

print("要增強之英雄(Buff)\n"+str(df.tail(2)["中文名"]))
print("\n要減弱之英雄(Nerf)\n"+str(df.head(3)["中文名"]))