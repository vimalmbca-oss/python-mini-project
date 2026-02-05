def ad2():
    from PIL import Image
    print("IMAGE:")
    print("1.show image")
    print("2.skip")
    ch=int(input("enter your choice:"))
    if ch==1:
        img=Image.open(r"C:\Users\Alex\Downloads\download (8).jfif")
        img.show()
        print("--------------------")
    elif ch==2:
        print("--------------------")
    print("---SPECIFICATIONS---")
    print("cc:398.6cc")
    print("mileage:30.5kpl")
    print("seat heigh:855")
    print("ex showroom price:2,88,450")
    print("on road price:3,64,349")
    from PIL import Image
    print("------colour option------")
    print("1.view colours\n2.skip")
    ch=int(input("enter your choice:"))
    if ch==1:
        print("1.orange\n2.white")
        ch=int(input("enter colour:"))
        if ch==1:
            print("orange")
            img=Image.open(r"C:\Users\Alex\Downloads\download (18).jpg")
            img.show()
        elif ch==2:
            print("white")
            img=Image.open(r"C:\Users\Alex\Downloads\download (8).jfif")
            img.show()
            print("----------------------")
    elif ch==2:
        print("----------------------")
    print("------OFFERS------")
    print("1.yes\n2.no")
    ch=int(input("view the offers:"))
    if ch==1:
        print("OFFERS:\n 1.tankfull\n 2.brand new helmet\n 3.bike cover")
        print("--------------------")
    elif ch==2:
        print("--------------------")
    print("-----EMI SCHEMES-----")
    print("1.EMI")
    print("2.skip")
    ch=int(input("enter the your choice:"))
    print("downpayment above 90,000rs")
    if ch==1:
        a=int(input("enter the downpayment:"))
        b=int(input("enter the month:"))
        c=364349
        d=c-a
        f=d/b
        c=d*12/100*b/12
        g=c/b
        j=f+g
        print("monthly payment:",f)
        print("monthly interest:",g)
        print("total EMI Amount:",j)
        print("total interest:",c)
        print("--------------------")
    elif ch==2:
        print("--------------------")
    import webbrowser
    print("---view the bike---")
    print("1.view")
    print("2.skip")
    ch=int(input("enter your choice:"))
    if ch==1:
        webbrowser.open_new("https://youtu.be/iL5TXkfgeWc?si=W_0-_bfjoCRt141G")
        print("--------------------")
    elif ch==2:
        print("--------------------")
    from mini import ext
    ext.ex()


