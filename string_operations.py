
input_string = input("Enter the string : ")
print("String is :- ",input_string)
ch = input("Enter your choice :")
while True:
    if ch=='length':
        counter=0
        for i in input_string:
            counter = counter + 1 
        print("Length is : ",counter)
        break

    elif ch=='capital':
        print(input_string.capitalize())
        break

    elif ch=='count':
        ele = input("Enter the character you wanna find(how many times?): ")
        print(input_string.count(ele))
        break

    elif ch=='find':
        ele= input("Enter the word you wanna find : ")
        print(input_string.find(ele))
        break

    elif ch=='index':
        ele= input("Enter the element whose index you wanna find : ")
        print(input_string.index(ele))
        break

    

    
        

