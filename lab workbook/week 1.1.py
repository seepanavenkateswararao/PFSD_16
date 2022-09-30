class Reservation:
    def _init_(self,train_no,pass_name,pass_age,pass_gender,pass_departure,pass_destination,pass_seat_preference,depar_time,arrival_time):
        self.train_no=train_no
        self.pass_name=pass_name
        self.pass_age=pass_age
        self.pass_gender=pass_gender
        self.pass_departure=pass_departure
        self.pass_destination=pass_destination
        self.pass_seat_preference=pass_seat_preference
        self.depar_time=depar_time
        self.arrival_time=arrival_time
    def trainBooking(self):
        print("train no {train_no}".format(train_no=self.train_no))
        print("Passenger name :{pass_name} age:{pass_age} "
              "gender:{pass_gender}".format(pass_name=self.pass_name,pass_age=self.pass_age,pass_gender=self.pass_gender))
        print("Boarding station {pass_departure} at {depar_time}".format(pass_departure=self.pass_departure,depar_time=self.depar_time))
        print("Arrival station {pass_destination} at {arrival_time} ".format(pass_destination=self.pass_destination,arrival_time=self.arrival_time))
        print("You train is successfully booked")
class Passenger(Reservation):
    train_no=int(input("Enter train number"))
    pass_name=input("Enter passenger name")
    pass_age=int(input("enter passenger age"))
    pass_gender=input("Enter passenger gender")
    pass_departure=input("enter passenger boarding")
    pass_destination=input("Enter passenger destination")
    pass_seat_preference=int(input("enter seat preference"))
    depar_time=int(input("enter the departure time"))
    arrival_time=int(input("Enter the arrival time"))
#super()._init_(train_no,pass_name,pass_age,pass_gender,pass_departure,pass_destination,pass_seat_preference,depar_time,arrival_time)
    reserve=Reservation(train_no,pass_name,pass_age,pass_gender,pass_departure,pass_destination,pass_seat_preference,depar_time,arrival_time)
    #reserve.trainBooking(train_no,pass_name,pass_age,pass_gender,pass_departure,pass_destination,pass_seat_preference,depar_time,arrival_time)
    reserve.trainBooking()