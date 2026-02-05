import pygame as p
import time
p.init()
p.display.set_caption("KTM BIKES")
ps1=p.display.set_mode((400,250))
ps=p.image.load(r"C:\Users\Alex\Downloads\download.png")
ps1.blit(ps,(20,50))
p.display.update()
time.sleep(5)
p.quit()
print("--------------------------KTM BIKES-----------------------------------")
print("REGISTRATION")
name=str(input("name  :"))
mobile=str(input("mobile:"))
if len(mobile)!=10:
    print("please enter the 10 digit number")
    mobile=str(input("mobile:"))
email=str(input("email :"))
print("registration successfully")
from mini import models
models.mod()


