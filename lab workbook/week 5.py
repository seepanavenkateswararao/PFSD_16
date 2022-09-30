import csv
class Employee:
    def insertion(self):
        with open('emp.csv','w') as f:
            w=csv.writer(f)
            w.writerow(['Emp_ID','Emp_Name', 'DOB', 'Department', 'Designation', 'years_of_Experience', 'leaves', 'Salary'])
            while True:
                emp_id=int(input("Enter the employee number"))
                emp_name=input("Enter the name of the employee")
                dob=int(input("Enter the date of birth"))
                dept=input("Enter the department of the employee")
                designation=input("Enter the designation of the emplloyee")
                experience=int(input('Enter the experience of the employee'))
                leaves=int(input("Enter no of leaves"))
                emp_sal=float(input("Enter the employee salary"))
                w.writerow([emp_id,emp_name,dob,dept,designation,experience,leaves,emp_sal])
                opt=input("do you want to continue Yes/No")
                if opt.lower()=='no':
                    f.close()
                    break

    def retriveByName(self):
        with open('emp.csv', 'r') as file:
            r = csv.reader(file)
            found = False
            emp_id = int(input("Enter employee id"))
            emp_name = input("Enter the key you want")
            for row in r:
                if (row[0] == emp_id and row[1]==emp_name):
                    print(row)
                    found = True
        if found==False:
            print("search key is not present in the file")

    def retriveBySalary(self):
        with open('emp.csv', 'r') as file:
            r = csv.reader(file)
            emp_sal = input("Enter employee salary")
            for row in r:
                if (row[7]>=emp_sal):
                    print(row)
    def retriveByleaves(self):
        with open('emp.csv', 'r') as file:
            r = csv.reader(file)
            leaves = input("Enter employee salary")
            for row in r:
                if (row[6]>=leaves):
                    print(row)


def retriveByName(self):
    with open('emp.csv', 'r') as file:
        r = csv.reader(file)
        found = False
        emp_id = int(input("Enter employee id"))
        emp_name = input("Enter the key you want")
        for row in r:
            if (row[0] == emp_id and row[1] == emp_name):
                print(row)
                found = True
        if found == False:
            print("search key is not present in the file")

if __name__ == "__main__":
    l=Employee()
    while True:
        print("1.insertion\n2.retriveByName\n3.retriveBySalary\n4.retriveByleaves")
        opt=input("Enter your option")
        if opt.lower()=='insertion':
            l.insertion()
        if opt.lower()=='retriveByName':
            l.retriveByName()
        if opt.lower() == 'retriveBySalary':
            l.retriveBySalary()
        if opt.lower() == 'retriveByleaves':
            l.retriveByleaves()
        op=input("enter whether you want to continue ore not yes/No")
        if op.lower()=='no':
            break