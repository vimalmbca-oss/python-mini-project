def ex():
    print("1.CONTINUE")
    print("2.EXIT")
    ch=int(input("enter your choice:"))
    if ch==1:
        from mini import models
        models.mod()
    elif ch==2:
        print("THANK YOU AND WELCOME BACK")
        
