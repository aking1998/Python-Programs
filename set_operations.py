
myset = {'mango','apple','banana','orange'}
ch='y'
while ch!='quit':
    print("1.Add Item ")
    print("2.Clear Set ")
    print("3.Remove Item ")
    print("4.Copy Set ")
    print("5.Pop Item ")
    print("6.Print Sets")
    print("7.Quit Program (type'quit')")

    ch=input("enter your choice : ")

    if ch=='1':
        ele=input("Enter the element : ")
        myset.add(ele)
        print("My Set : ",myset)
    

    elif ch=='2':
        myset.clear()
        print("My Set : ",myset)
        

    elif ch=='3':
        ele=input("Enter the element you wanna remove : ")
        myset.remove(ele)
        print("My Set : ",myset)
        

    elif ch=='4':
        yourset = myset.copy()
        print("New Set : ",yourset)
        print("My Set : ",myset)
        

    elif ch=='5':
        myset.pop()
        print("My Set : ",myset)

    elif ch=='6':
        print("New Set : ",yourset)
        print("My Set : ",myset)
        
    elif ch=='quit':
        break


    
    

    
