c1 = "make a lot of money"
c2 = "buy now"
c3 = "subscribe this"
c4 = "click here"

message = input("Enter your comment")
if (c1 in message or c2 in message or c3 in message or c4 in message):
    print("This is a spam message")
else:
    print("This is a valid message")