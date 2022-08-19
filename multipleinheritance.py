class Base1:
	      def method1(Self):
	             print("this is base1")
class Base2:
	       def method2(Self):
	             print("this is base2")
class Base3:
	       def method3(Self):
	             print("this is base3")
class Derived(Base1,Base2,Base3):
	      def method4(Self):
	             print("this is derived")

if __name__=='__main__':
    ob = Derived()
    ob.method1()
    ob.method2()
    ob.method3()
    ob.method4()
