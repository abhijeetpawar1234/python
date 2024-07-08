roll =[]
name =[]
marks=[]
def addData():
        sroll = int(input("enter the roll no:"))
        sname = input("enter the name   :")
        smarks = int(input("enter the marks :"))
        roll.append(sroll)
        name.append(sname)
        marks.append(smarks)

def viewData():

    # print(roll)
    # print(name)
    # print(marks)

    print("ROLLNO \t NAME \t MARKS")
    for i in range(len (roll)):
        print(roll[i],"\t",name[i],"\t",marks[i] )

def  updatestud():
     
    #  tem=int(input("enter roll no want to update:"))
    #  popel = roll.index(tem)
    #  roll.pop(popel)
    #  name.pop(popel)
    #  marks.pop(popel)

    #  uroll = int(input("enter new roll no:"))
    #  uname = input("enter the name:")
    #  umarks = int(input("enter the new marks:"))

    #  roll.insert(popel,uroll)
    #  name.insert(popel,uname)
    #  marks.insert(popel,umarks)

    froll = int(input("enter the find roll:"))
    for i in range(len (roll)):
        if(roll[i]==froll):
            Uroll = int(input("enter the NEW roll no:"))
            Uname = input("enter the new name   :")
            Umarks = int(input("enter the  new marks :"))
        
            roll[i] =Uroll
            name[i] =Uname
            marks[i]=Umarks

def delete():
    #  dele=int(input("enter roll no want to delete:"))
    #  del_index = roll.index(dele)
    #  roll.pop(del_index)
    #  name.pop(del_index)
    #  marks.pop(del_index)
    #  print("Record deleted for roll",dele)
    
    droll = int(input("enter the delete record roll:"))
    for i in range(len (roll)):
        if(roll[i]==droll):
            
            roll.remove(roll[i])
            name.remove(name[i])
            marks.remove(marks[i])
            break

    
count  = 3
while(count!=0):
    Uname = input("enter the Username:")
    Upass = input("enter the Password:")
    if(Uname=="admin" and Upass=="1234"):
        print("login succesfully !")
        print("Student Management System")
        cnt = 1
        while(cnt!=0):
            print("1.Add Student \n 2.View List \n 3.Update \n 4.Delete \n 5.exit")
            ch = int(input("enter the choice:"))
            if(ch==1):
                print("Add student")
                addData()
            if(ch==2):
                print("View student")
                viewData()
            if(ch==3):
                print("Update student")
                updatestud()
            if(ch==4):
                print("delete student")
                delete()
            if(ch==5):
                cnt = 1
        cnt -=1
        count = 1
        
    elif(Uname!="admin" and Upass!="1234"):
        print("login Un Successfully Both incorrect !")
    elif(Uname!="admin"):
        print("Username incorrect !")
    elif(Upass!="1234"):
        print("User Password incorrect !")
    count -= 1
    print("remainin attempt::",count)


    