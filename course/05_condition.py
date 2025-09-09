# x=input("請輸入數字: ") #取得字串形式的使用者輸入
# x=int(x) #將字串轉換成數字型態

# if x > 200:
#     print("大於200")
# elif x > 100:
#     print("大於100, 小於等於 200")
# else:
#     print("小於等於 100")

n1=int(input("請輸入數字一： "))
n2=int(input("請輸入數字二： "))
op=input("請輸入運算 +, -, *, /：")

if op == '+':
    print(n1+n2)
elif op == '-':
    print(n1-n2)
elif op == '*':
    print(n1*n2)
elif op == '/':
    print(n1/n2)
else:
    print("對不起，您輸入的運算子有誤，請查明後再撥，謝謝！")
