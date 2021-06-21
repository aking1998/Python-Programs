ch=''
while ch!='quit':
    print("1.Read File ")
    print("2.Read One line from File ")
    print("3.Write/Append Content to the File")
    print("4.Overwrite the Content of File")
    print("5.Delete the File")
    
    ch=input("Enter your choice : ")
    if ch=='1':
        f = open("myfile.txt")
        print(f.read()) 
        f.close()
    
    elif ch=='2':
        f = open("myfile.txt")
        print(f.readline())
        f.close()

    elif ch=='3':
        f = open("myfile.txt","a")                 # "a" - Append - will append to the end of the file
        content=input("Enter the content : ")
        f.write(content)
        print("File Updated Successfully!!")
        f.close()

    elif ch=='4':
        f = open("myfile.txt","w")                # Note: the "w" method will overwrite the entire file.
        content=input("Enter the content : ")
        f.write(content)
        print("File Updated Successfully!!")
        f.close()

    elif ch=='5':
        import os
        os.remove("myfile.txt")
        print("File Deleted..") 
        
    elif ch=='quit':
        break
        







