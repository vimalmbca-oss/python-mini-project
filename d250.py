def d2():
    from PIL import Image
    print("IMAGE:")
    print("1.show image")
    print("2.skip")
    ch=int(input("enter your choice:"))
    if ch==1:
        img=Image.open(r"C:\Users\Alex\Downloads\download (3).jfif")
        img.show()
        print("--------------------")
    elif ch==2:
        print("--------------------")
    print("---SPECIFICATIONS---")
    print("cc:249.07cc")
    print("mileage:31.5kpl")
    print("seat heigh:800mm")
    print("ex showroom price:2,29,995")
    print("on road price:2,71,349")
    from PIL import Image
    print("------colour option-------")
    print("1.view colours\n2.skip")
    ch=int(input("enter your choice:"))
    if ch==1:
        print("1.orange\n2.black\n3.blue")
        ch=int(input("enter colour:"))
        if ch==1:
            print("orange")
            img=Image.open(r"C:\Users\Alex\Downloads\download (5).jpg")
            img.show()
        elif ch==2:
            print("black")
            img=Image.open(r"C:\Users\Alex\Downloads\images.jpg")
            img.show()
        elif ch==3:
            print("blue")
            img=Image.open(r"C:\Users\Alex\Downloads\download (4).jpg")
            img.show()
            print("----------------------")
    elif ch==2:
        print("----------------------")
    print("-------OFFERS-------")
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
    print("downpayment above 70,000rs")
    if ch==1:
        a=int(input("enter the downpayment:"))
        b=int(input("enter the months:"))
        c=271349
        d=c-a
        f=d/b
        c=d*12/100*b/12
        g=c/b
        j=f+g
        print("monthly payment:",f)
        print("monthly interest:",g)
        print("total EMI amount:",j)
        print("total interest:",c)
        print("--------------------")
    elif ch==2:
        print("--------------------")
    import webbrowser
    print("----view the bike----")
    print("1.view")
    print("2.skip")
    ch=int(input("enter your choice:"))
    if ch==1:
        webbrowser.open_new("https://youtu.be/zJp7_6ZOAek?si=U7vLgxQhYp3DbHfZ")
        print("--------------------")
    elif ch==2:
        print("--------------------")
    from mini import ext
    ext.ex()


