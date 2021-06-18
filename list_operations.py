n = int(input("enter the number of elements : "))
numbers = []
for i in range(0,n):
    ele = int(input())
    numbers.append(ele)

print("Input List is : ", numbers)

ch = input("Enter the choice : ")
while ch!="quit":
    if ch=="sort":
        numbers.sort()
        print("Sorted List is : ", numbers)
        break

    elif ch=="reverse":
        numbers.reverse()
        print("Reverse List is : ", numbers)
        break

    elif ch=="unique":
        unique = []

        for number in numbers:
            if number not in unique:
                unique.append(number)

        print("The Unique List : ", unique) 
        break

    elif ch=="count":
        cnt=int(input("Enter the element you want to count for? "))
        print("Count is : ",numbers.count(cnt))
        break

    elif ch=="reverse":
        rem = int(input("Enter the element you wanna remove : "))
        numbers.remove(rem)
        print("Updated List : ",numbers)
        break

    elif ch=="pop":
        pop_ele = int(input("Enter the index of the element you wanna pop : "))
        numbers.pop(pop_ele)
        print("Updated List : ",numbers)
        break
    
    elif ch=="insert":
        index = int(input("Enter the index of the element you wanna insert the element : "))
        num = int(input("Enter the element : "))
        numbers.insert(index,num)
        print("Updated List : ",numbers)
        break

    elif ch=="append":
        app_ele = int(input("Enter the element you wanna append in the list : "))
        numbers.append(app_ele)
        print("Updated List : ",numbers)
        break

    else:
        ch=="quit"



    




    

       