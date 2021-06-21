
dict={}
num = int(input("Enter no of elements : "))
for i in range(0,num):
    key=input("Enter Key : ")
    Value=input("Enter Value : ")
    dict[key]=Value
print("Dictionary :",dict)

ch=""
while ch!='quit':
    print("1.Insert/Update Item in Dictionary")
    print("2.Get Value of Item in Dictionary")
    print("3.Get All Keys ")
    print("4.Pop the Key:Value")
    print("5.Get All Values")
    

    ch=input("Enter your choice : ")

    if ch=='1':
        key=input("Enter Key : ")
        Value=input("Enter Value : ")
        dict.update({key:Value})
        print("Dictionary :",dict)

    elif ch=='2':
        key=input("Enter Key : ")
        x = dict.get(key)
        print(" Value is :",x)

    elif ch=='3':
        x = dict.keys()
        print("Keys : ",x)

    elif ch=='4':
        ele=input("Enter the key: ")
        dict.pop(ele)
        print("Dictionary :",dict)

    elif ch=='5':
        x = dict.values()
        print("Values : ",x)

    elif ch=='quit':
        break


