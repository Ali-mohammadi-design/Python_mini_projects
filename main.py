from turtle import *
import random
timy=Turtle()
screen=Screen()
a=0
b=0
# for n in range(10):
#      for m in range(3+b):
#         timy.forward(50)
#         timy.right(abs(120-a))
#
#      a=a+30
#      b=b+1
def clor(a):
    if a==0:
        return "brown"
    if a==1:
        return "red"
    if a==2:
        return "blue"
    if a==3:
        return "yellow"
    if a==4:
        return "green"
    if a==5:
        return "purple"

r=random.randint(0,5)
print(r)
b=3
for n in range(40):
    for m in range(b):
             timy.color(clor(r))
             timy.forward(50)
             timy.right(360/b)
    b=b+1
    r = random.randint(0, 5)



screen.exitonclick()
