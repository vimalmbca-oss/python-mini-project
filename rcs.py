def rc():
    print("1.rc125")
    print("2.rc200")
    print("3.rc930")
    ch=int(input("enter your choice:"))
    if ch==1:
        print("rc125")
        from mini import rc125
        rc125.rc1()
    elif ch==2:
        print("rc200")
        from mini import rc200
        rc200.rc2()
    elif ch==3:
        print("rc390")
        from mini import rc390
        rc390.rc3()
    
    
     
