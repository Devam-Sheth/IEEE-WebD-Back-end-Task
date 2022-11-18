ans='y'
dict={}
while(ans=='y'):
    k=input("Key :  ")
    v=input("Value : ")
    ans=input("Continue adding?...(y/n) - ")
    dict.update({k:v})
print("\n",dict)
print("\n Sorting Dictionary by Keys....")
key_sort=sorted(dict.items(),key=lambda x:x[0])
print(key_sort)
print("\n Sorting Dictionary by Values....")
value_sort=sorted(dict.items(),key=lambda x:x[1])
print(value_sort)