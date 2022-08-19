class Base:
    def method1(self):
        print("this is base")
class Derived1(Base):
    def method2(self):
        print("this is derived1")
class Derived2(Base):
    def method3(self):
        print("this is derived2")

if __name__=='__main__':
	ob=Derived2()
	ob.method1()
	ob.method3()