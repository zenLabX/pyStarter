# while + break 會結束整個迴圈
# n=1
# while n<5:
#     if n==3:
#         break
#     else:
#         n+=1
#         print('break',n)

# while + else 在迴圈結束前，else 執行某動作
n=1
while n<5:
    print('n is:', n)
    n+=1
else:
    print('before leaving the loop', n)


# continue 會不執行接下來的程式碼，但繼續執行下一輪迴圈
n=0
for x in [0,1,2,3]:
    if x%2==0:
        continue
    n+=1
    print('continue',n)


# for + else 在迴圈結束前，else 執行某動作
for f in 'Fried Chicken':
    print('f is', f)
else:
    print('before leaving the loop', f)