p = 0.2
w = 1-p
PickRate = [0.73,4.58,4.38,3.21,2.33,4.72,0.52,3.47,0.67,2.13,5.01,0.55,0.71,2.32,7.96,2.65,6.75,5.26,3.85,4.26,4.46,2.98,13.73,0.91,4.12]
WinRate = [48.92,50.00,48.72,51.24,50.17,50.49,44.82,49.13,50.68,46.12,52.64,48.60,55.45,48.41,52.90,53.30,51.56,50.30,48.95,48.57,45.16,50.20,52.70,59.87,53.19]
ans_Buff = [20]
ans_Nerf = [22]


#PickRate = [0.83,4.88,4.51,3.87,3.15,5.24,0.72,3.20,0.64,2.24,4.15,0.72,1.01,1.94,7.57,1.80,6.08,3.53,5.67,5.07,4.93,5.44,14.04,1.44,5.35]
#WinRate = [49.29,50.44,48.69,51.40,51.00,50.08,44.95,48.63,50.40,46.10,52.47,48.98,56.43,47.46,52.01,52.79,51.86,49.90,50.47,49.28,44.78,50.71,52.18,60.47,52.89]
#ans_Buff = [16,10,15,17,13]
#ans_Nerf = []

max1 = -1 
max2 = -1
max3 = -1

max1Num = -1
max2Num = -1
max3Num = -1

min1 = 101
min2 = 101

min1Num = -1
min2Num = -1

ans_list = []
ans_correct = [0]*21
m = -1
mNum = -1
ans_dis1 = -1
ans_dis2 = -1
for  i  in  range(0,101,5):
    WinRate_weight = (100-i)/100
    PickRate_weight = i/100
    #print("------A B-------")
    #print("WinRate_weight = ",WinRate_weight)
    #print("PickRate_weight = ",PickRate_weight)
    #print("-------PickRate-------")
    #for j in range (0,24,1):
    #    print(PickRate[j]*PickRate_weight)
    #print("----------WinRate--------")
    #for j in range (0,24,1):
    #    print(WinRate[j]*WinRate_weight)
    #print("--------total-------")    
    #for j in range (0,24,1):
    #    total = ((PickRate[j]*PickRate_weight)+(WinRate[j]*WinRate_weight))
    #    print(total)
    
    
    #計算出加權過後前三大的數
    #紀錄加權過後最大的數是哪幾個英雄
    for j in range(0,24,1):
        if j==0:
            max1=((PickRate[j]*PickRate_weight)+(WinRate[j]*WinRate_weight))
            max1Num = j
        elif j==1:
            if ((PickRate[j]*PickRate_weight)+(WinRate[j]*WinRate_weight))>max1:
                max2 = max1
                max2Num = max1Num;
                max1 = ((PickRate[j]*PickRate_weight)+(WinRate[j]*WinRate_weight))
                max1Num = 1
            else :
                max2 = ((PickRate[j]*PickRate_weight)+(WinRate[j]*WinRate_weight))
                max2Num = j
        elif j==2:
            if ((PickRate[j]*PickRate_weight)+(WinRate[j]*WinRate_weight))>max1:
                max3 = max2
                max3Num = max2Num
                max2 = max1
                max2Num = max1Num
                max1 = ((PickRate[j]*PickRate_weight)+(WinRate[j]*WinRate_weight))
                max1Num = j
            elif ((PickRate[j]*PickRate_weight)+(WinRate[j]*WinRate_weight))>max2:
                max3 = max2
                max3Num = max2Num
                max2 = ((PickRate[j]*PickRate_weight)+(WinRate[j]*WinRate_weight))
                max2Num = j
            else:
                max3 = ((PickRate[j]*PickRate_weight)+(WinRate[j]*WinRate_weight))
                max3Num = j
        elif ((PickRate[j]*PickRate_weight)+(WinRate[j]*WinRate_weight))>max1:
            max3 = max2
            max3Num = max2Num
            max2 = max1
            max2Num = max1Num
            max1 = ((PickRate[j]*PickRate_weight)+(WinRate[j]*WinRate_weight))
            max1Num = j
            
        elif ((PickRate[j]*PickRate_weight)+(WinRate[j]*WinRate_weight))>max2:
            max3 = max2
            max3Num = max2Num
            max2 = ((PickRate[j]*PickRate_weight)+(WinRate[j]*WinRate_weight))
            max2Num = j
            
        elif ((PickRate[j]*PickRate_weight)+(WinRate[j]*WinRate_weight))>max3:
            max3 = ((PickRate[j]*PickRate_weight)+(WinRate[j]*WinRate_weight))
            max3Num = j
            
            
    #計算加權過後最小的兩個數
    #記錄加權過後最小的兩個數是哪個英雄
    for k in range(0,24,1):
        if k==0:
            min1 = ((PickRate[k]*PickRate_weight)+(WinRate[k]*WinRate_weight))
        elif k==1:
            if ((PickRate[k]*PickRate_weight)+(WinRate[k]*WinRate_weight))<min1:
                min2 = min1
                min2Num = min1Num;
                min1 = ((PickRate[k]*PickRate_weight)+(WinRate[k]*WinRate_weight))
                min1Num = 1
            else :
                min2 = ((PickRate[k]*PickRate_weight)+(WinRate[k]*WinRate_weight))
                min2Num = k;
        elif k==2:
            if ((PickRate[k]*PickRate_weight)+(WinRate[k]*WinRate_weight))<min1:
                min2 = min1
                min2Num = min1Num
                min1 = ((PickRate[k]*PickRate_weight)+(WinRate[k]*WinRate_weight))
                min1Num = k
            elif ((PickRate[k]*PickRate_weight)+(WinRate[k]*WinRate_weight))<min2:
                min2 = ((PickRate[k]*PickRate_weight)+(WinRate[k]*WinRate_weight))
                min2Num = k        
        elif ((PickRate[k]*PickRate_weight)+(WinRate[k]*WinRate_weight))<min1:
            min2 = min1
            min2Num = min1Num
            min1 = ((PickRate[k]*PickRate_weight)+(WinRate[k]*WinRate_weight))
            min1Num = k
            
        elif ((PickRate[k]*PickRate_weight)+(WinRate[k]*WinRate_weight))<min2:
            min2 = ((PickRate[k]*PickRate_weight)+(WinRate[k]*WinRate_weight))
            min2Num = k
            
          
    #print("--------max-------")            
    #print(max1)
    #print(max2)
    #print(max3)
    #print(max1Num)
    #print(max2Num)
    #print(max3Num)
    #print("--------min--------") 
    #print(min1)
    #print(min2)
    #print(min1Num)
    #print(min2Num)
    
    #將所有測試值的三個大的數及兩個小的數紀錄
    ans_list.extend([max1Num,max2Num,max3Num,min1Num,min2Num])
    
#print(ans_list)    





for i in range(0,105,1):
    #將前三個跟Nerf的角色做比對，若比對成功則+1
    if (i%5<3):
        for k in range(len(ans_Nerf)):
            if (ans_list[i]==ans_Nerf[k]):
                ans_correct[int(i/5)] =  ans_correct[int(i/5)] +1
    #將後兩個跟Buff的角色做比對，若比對成功則+1            
    else:
        for k in range(len(ans_Buff)):
            if (ans_list[i]==ans_Buff[k]):
                ans_correct[int(i/5)] =  ans_correct[int(i/5)] +1
   
    if(i%5==4):  
        #每五個一組印出一次比對成功的次數
        print(ans_correct[int(i/5)])
        #再將比對成功次數一樣的拿來與一開始的PickRate_weight做相減，看哪個較為接近
        if ans_correct[int(i/5)]>m:
            m = ans_correct[int(i/5)]
            mNum = int(i/5)
        elif ans_correct[int(i/5)]==m:
            ans_dis1 = 0.05*(int(i/5))-p
            ans_dis2 = 0.05*mNum-p
            if ans_dis1<0:
                ans_dis1 = ans_dis1+2*p
            if ans_dis2<0:
                ans_dis2 = ans_dis2+2*p
            if ans_dis1<ans_dis2:
                m = ans_correct[int(i/5)]
                mNum = int(i/5)
#print("-------------")    
#print(m)
#print(mNum*0.05)
#print("----------")
#將舊有的PickRate_weight和WinRate_weight數據做更新
p = mNum*0.05*0.85+p*0.15
w = 1-p
print("PickRate_weight = ",p)
print("WinRate_weight = ",w)
ChiName = ["毀滅拳王","源氏","麥卡利","法拉","死神","士兵76","駭影","閃光","壁壘機兵","半藏","炸彈鼠","小美","托比昂","奪命女","D.VA","歐瑞莎","萊茵哈特","攔路豬","溫斯頓","札莉雅","安娜","路西歐","慈悲","辛梅塔","禪亞塔"]
EngName = ["Doomfist","Genji","McCree","Pharah","Reaper","Soldier:76","Sombra","Tracer","Bastion","Hanzo","Junkrat","Mei","Torbjörn","Widownmaker","D.Va","Orisa","Reinhardt","Roadhog","Winston","Zarya","Ana","Lúcio","Mercy","Symmetra","Zenyatta"]