# 數字運算
x=3*6
y=7/2 #浮點數除法
z=7//2 #整數除法
print("乘與除法:",x,y,z)

a=2**3 #次方
b=2**0.5 #開根號
print("次方與開根號:",a,b)

c=13%5 #餘數
print("取餘數:",c)

d=3
d*=3 #d=d*3
print('d:',d)

e=4
e-=3 #e=e-3
print('e:',e)

f=5
f+=2 #f=f+2
print('f:',f)

g=9
g/=3 #g=g/3
print('g:',g)


#字串運算

#字串宣告
string = "hello,'wao',ok"
print(string)

#跳脫字元：雙引號在字串中可被顯示
jump = "quo\"tation"
print(jump)

#字串串接：多一個空白鍵即可
j="Lunch"+"Time"
k="BreakFast" "Time" 
print(j,k)

 #字串斷行的兩種方法
firstWayToCutTheString="品名:舒潔衛生紙\n製造日期:2024.03.11"
print(firstWayToCutTheString)

secondWayToCutTheString="""在\"""裡面  
我就可以
任意做
換行了""" #可透過 """ 斷行
print(secondWayToCutTheString)

#字串切割
job = "professor"
print("字首:",job[0:3])

job2 = "babysitter"
print("取字尾:",job2[4:])
print("取字首:",job2[:4])