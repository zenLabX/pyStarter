# 集合：沒有順序的概念，一群資料放在一起
# s1={4,8,12}

#查看集合中有沒有這筆資料 (in、not in)
# print(4 in s1)
# print(3 in s1)
# print(3 not in s1)

#查看交集 (交集、聯集、差集、反交集)
s1={3,4,5}
s2={4,5,6,7}
# s3=s1&s2 #交集: 取兩個集合中相同的資料
# s3=s1|s2 #聯集: 取兩個集合中相同的所有資料，！但不重複取
# s3=s1-s2 #差集: 從 s1 中，減去和 s2 重疊的部分
# s3=s2-s1 #差集: 從 s2 中，減去和 s1 重疊的部分
# s3=s1^s2 #反交集: 取兩個集合中，不重疊的部分
# print(s3)

s=set('Hello') #字串可拆解為集合
print(s)
print('A' in s)
print('H' in s)

#字典：key-value 配對 (類似一把鑰匙對一個門)
dictionary = {"apple":"蘋果", "bug":"蟲蟲"}
print(dictionary["apple"]) #用key取到value

dictionary["apple"] = "富士蘋果" #用key變更value
print(dictionary["apple"]) 

print("apple" in dictionary) #判斷對象是key
print("guava" not in dictionary) #判斷對象是key

del dictionary["bug"] #刪除字典中的鍵值對 (key-value pair)
print(dictionary)

dic={x:x*2 for x in [3,4,5]}
print(dic)