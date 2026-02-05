def mod():
    print("-----WELCOME TO KTM BIKES-----")
    print("BIKE MODELS")
    print("1.duke")
    print("2.rc")
    print("3.adventure")
    ch=int(input("enter bike model:"))
    if ch==1:
        print("duke")
        from mini import dukes
        dukes.duke()
    elif ch==2:
        print("rc")
        from mini import rcs
        rcs.rc()
    elif ch==3:
        print("adventure")
        from mini import adves
        adves.adve()
    
    
     
     
     
             
