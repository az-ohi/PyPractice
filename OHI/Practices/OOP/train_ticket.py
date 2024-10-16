from random import randint


class train:

    def __init__(ohi, train_no):
        ohi.train_no = train_no

    def book_ticket(ohi, frm, to):
        print(f"Ticket is booked in train {ohi.train_no} from {frm} to {to}.")

    def get_status(ohi):
        print(f"The train {ohi.train_no}  running on time...")

    def get_fare(ohi, frm, to):
        print(f"Ticket fare is in train {ohi.train_no} from {frm} to {to} is {randint(300,2000)}.")

print("Good Evening, Sir!!!")
x = int(input("Give Your train number please: "))
a = input("From where you want to start your Journey: ")
b = input("Where you want to go: ")

t = train(x)
t.book_ticket(a, b)
t.get_status()
t.get_fare(a, b)