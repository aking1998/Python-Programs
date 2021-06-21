
values = input("Input some comma seprated numbers : ")
list = values.split(",")               
tuple = tuple(list)                    # converting list into tuple
print("Tuple : ",tuple)

ele = input("enter the element you wanna count : ")
print(tuple.count(ele)," times!!")

ind = input("enter the element whose index you  wanna search for : ")
print(ind + " is present at index ",tuple.index(ind),)