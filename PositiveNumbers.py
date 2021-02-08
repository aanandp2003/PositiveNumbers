list =[]
n = int(input("Enter number of elements : "))
for i in range(0,n):
    list.append(int(input()))
for i in range(0,n):
    if list[i]>0:
        print(list[i])


