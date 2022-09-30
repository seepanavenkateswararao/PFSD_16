from pymongo import MongoClient
db = MongoClient("mongodb://127.0.0.1:27017")
client = db['PFSD-Lab']
stu_data = client.students
class Lab4:
    def insertion(self):
        product_id=int(input("Enter the product id"))
        name=input('Enter the product name')
        country=input("enter the name of the country")
        s={"Product_id":product_id,"Name of the product":name,"country":country}
        stu_data.insert_one(s)
    def deletion(self):
        name=input("Enter which name you want to delete")
        delete={"name":name}
        stud_data.delete_one(delete)
    def retrive(self):
        name = input("Enter which name you want to retrive")
        retriv={"name":name}
        stu_data.find_one(retriv)
    def updation(self):
        name = input("Enter which name to which you want to update")
        names=input("Enter you updapted name")
        select={"name":name}
        updation={"$set":{"name":names}}
        stud_data.update_one(select,updation)

if __name__ == "__main__":
    l=Lab4()
    while True:
        print("1.insertion\n2.deletion\n3.updation\n4.retrive")
        opt=input("Enter your option")
        if opt.lower()=='insertion':
            l.insertion()
        elif opt.lower()=='deletion':
            l.deletion()
        elif opt.lower()=='updation':
            l.updation()
        elif opt.lower()=='retrive':
            l.retrive()
        op=input("enter whether you want to continue ore not yes/No")
        if op.lower()=='no':
            db.close()
            break