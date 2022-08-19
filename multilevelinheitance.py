class Parent:
	     def method1(self):
	            print("this is parent class")
class Child1(Parent):
	      def method2(self):
	            print("this is child class 1")
class Child2(Child1):
	     def method3(self):
	            print("this is child class 2")

if __name__ == '__main__':
    ob = Child2()
    ob.method1()
    ob.method2()
    ob.method3()