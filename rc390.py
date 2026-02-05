def rc3():
    from PIL import Image
    print("IMAGE:")
    print("1.show image")
    print("2.skip")
    ch=int(input("enter your choice:"))
    if ch==1:
        img=Image.open(r"C:\Users\Alex\Downloads\download (5).jfif")
        img.show()
        print("--------------------")
    elif ch==2:
        print("--------------------")
    print("---SPECIFICATIONS---")
    print("cc:373.27cc")
    print("mileage:29.5kpl")
    print("seat heigh:800mm")
    print("ex showroom price:2,23,006")
    print("on road price:3,64,349")
    from PIL import Image
    print("------colour option------")
    print("1.view colours\n2.skip")
    ch=int(input("enter your choice:"))
    if ch==1:
        print("1.orange\n2.blue")
        ch=int(input("enter colour:"))
        if ch==1:
            print("orange")
            img=Image.open(r"C:\Users\Alex\Downloads\download (11).jpg")
            img.show()
        elif ch==2:
            print("blue")
            img=Image.open(r"C:\Users\Alex\Downloads\download (10).jpg")
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
    if ch==1:
        print("downpayment above 90,000rs")
        a=int(input("enter the downpayment:"))
        b=int(input("enter the months:"))
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
        webbrowser.open_new("https://youtu.be/e4xTt5OL4Rc?si=jzL8S2QhsJr3rOjT")
        print("--------------------")
    elif ch==2:
        print("--------------------")
    from mini import ext
    ext.ex()


