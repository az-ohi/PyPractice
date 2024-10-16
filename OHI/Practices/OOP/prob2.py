from random import randint


class train:

    def __init__(self, train_no):
        self.train_no = train_no

    def book_ticket(self, frm, to):
        print(f"Ticket is booked in train {self.train_no} from {frm} to {to}.")

    def get_status(self):
        print(f"The train {self.train_no}  running on time...")

    def get_fare(self, frm, to):
        print(f"Ticket fare is in train {self.train_no} from {frm} to {to} is {randint(300,2000)}.")

print("Good Evening, Sir!!!")
x = int(input("Give Your train number please: "))
a = input("From where you want to start your Journey: ")
b = input("Where you want to go: ")

t = train(x)
t.book_ticket(a, b)
t.get_status()
t.get_fare(a, b)