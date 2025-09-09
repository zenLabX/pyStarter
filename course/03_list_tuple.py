# python 之中有兩種有序列表型態，一種是 List，另一種 Tuple

# 有序可變動列表 List
grades = [12,50,32,48,11]

grades[0]=33 #List列表可以被更動

print(grades[1:4]) #從index 1開始取到不包含index 4的數字

# grades[1:4]=[] #有刪除列表中資料的意味在

grades = grades+[88,99,100] #列表的串接

length = len(grades) #列表的長度
print(length)

data = [[3,4,5], [6,7,8]] #巢狀列表
print(data[0][1])

# 有序不可變動列表 Tuple
data=(8,9,7)
print(data[0:2])

# data[2]=15 # 'tuple' object does not support item assignment

