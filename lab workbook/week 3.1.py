from pymongo import MongoClient
db = MongoClient("mongodb://127.0.0.1:27017")
client = db['PFSD-Lab']
product_data = client.Product
class Lab4:
    def insertion(self):
        S_no=int(input("Enter product no"))
        prod_name=input("Enter product name")
        DOM=int(input("ENter date of manufacture"))
        mrp=float(input("enter th rarte of the product"))
        bill=float(input("enter th rarte of the product"))
        prod_man=input("Enter the name of the manufactrer")
        product={"S_NO":S_no,"prod_name":prod_name,"Date_of_Manufacture":DOM,"MRP":mrp,"Bill invoice":bill,"product_manufacturer":prod_man}
        stu_data.insert_one(product)
    def deletion(self):
        name=input("Enter which name you want to delete")
        delete={"prod_name":name}
        stud_data.delete_one(delete)
    def retrive(self):
        name = input("Enter which name you want to retrive")
        retriv={"prod_name":name}
        print(stu_data.find_one(retriv))
    def updation(self):
        name = input("Enter which name to which you want to update")
        names=input("Enter you updapted name")
        select={"prod_name":name}
        updation={"$set":{"prod_name":names}}
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