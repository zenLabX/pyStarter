#while 的練習題
# n = 0
# while n < 5:
#     if n==3:
#         break
#     print(n) #印出迴圈中的 n
#     n+=1

# print('最後的n: ',n) #印出迴圈結束後的 n

#for 的練習題
# q = 0
# for r in [0,1,2,3]:
#     if r%2==0: #其實就是找偶數，能被2整除的數字
#         continue
#     print(r)
#     q+=1

# print('最後的q: ',q)

#else 的練習題 (迴圈結束前所執行的動作)
#一樣是1~10的累加，有兩種寫法
# sum1 = 0
# for n in range(11):
#     sum1=sum1+n #sum+=n
# else:
#     print('result for sum1:',sum1)


# sum2 = 0
# for u in range(1,11):
#     sum2+=u
# else:
#     print('result for sum2:',sum2)

# 綜合範例：找出整數平方根
# 輸入 9. 得到 3
# 輸入 11. 得到 [沒有] 整數的平方根

# n = input('請輸入一個正整數:')
# n = int(n)
# print('ccc',n)

# for i in range(n):
#     if i*i == n:
#         print('整數平方根為:',i)
#         break # 用 break 強制結束迴圈時，不會執行 else 區塊
# else:
#     print(n,'無法解出平方根!')

#巢狀迴圈
for x in range(1,6):
    for y in range(1,6):
        print(f"{x}*{y}={x*y}",end="\t")
    print()
    