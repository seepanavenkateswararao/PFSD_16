class Base:
    def method1(self):
              print("this is base")
class Derived1(Base):
    def method2(self):
               print("this is derived1")
class Derived2(Base):
    def method3(self):
        print("this is derived2")
class Final(Derived1,Derived2):
    def method4(self):
        print("this is final ")

if __name__=='__main__':

    ob=Final()

    ob.method1()
    ob.method2()
    ob.method3()
    ob.method4()


