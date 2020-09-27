list1 = [3,2,1,4,8,7,5,6]
n = len(list1)
for i in range(n):
    for j in range(0,n-i-1):
        if list1[j]>list1[j+1]:
            list1[j+1],list1[j]=list1[j],list1[j+1]
print(list1)