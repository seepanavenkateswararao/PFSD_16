import math
def circle(radius):
    print("the area of the circle is {area}".format(area=3.14*radius*radius))
    print("The perimeter of the circle is {perimeter}".format(perimeter=2*3.14*radius))
def Rectangle(length,breadth):
    print("The area of the Rectangle is {area}".format(area=(length*breadth)))
    print("The perimeter of the Rectangel is {perimeter}".format(perimeter=(2*(length+breadth))))
def Triangle(side1,side2,side3):
    s=(side1+side2+side3)/2
    print("The area of the Triangle {area}".format(area=(math.sqrt(s*(s-side1)(s-side2)(s-side3)))))
    print("The perimeter of the Triangle is {perimeter}".format(perimeter=((side1+side2+side3))))
radius=int(input("Enter the radius of the circle"))
circle(radius)
length,breadth=int(input("Enter the length of the Rectangle")),int(input("Enter the breadth of the Rectangle"))
Rectangle(length,breadth)
side1,side2,side3=int(input("Enter side1")),int(input("Enter side2")),int(input("enter side3"))
Triangle(side1,side2,side3)