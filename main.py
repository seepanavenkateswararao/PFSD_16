class Parent:
	     def method1(self):
	            print("this is parent class")
class Child(Parent):
	      def method2(self):
	            print("this is child class")


if __name__ == '__main__':
    ob = Child()
    ob.method1()
    ob.method2()

