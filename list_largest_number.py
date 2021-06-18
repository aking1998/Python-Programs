# Largest Number From A List

n = int(input("Enter the number of elements in a list : "))
list1=[]
print("Enter List elements : ")
for i in range(0,n):
    ele = int(input())
    list1.append(ele)
print("List : ", list1)


max_num=list1[0]
for num in list1:
    if num > max_num:
        max_num = num
print("Largest Number of the List: ", max_num)
    
