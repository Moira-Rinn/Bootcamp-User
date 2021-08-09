class User:
    def __init__(self, name, age, dob, email, balance):
        self.name = name
        self.age = age
        self.dob = dob
        self.email = email
        self.account_balance = balance


sara = User("Sara McCloud", 27, "July 19th, 1994", "SMcCloud@gmail.com", 1300)
rachael = User("Rachael Anderson", 19, "October 31st, 2002",
               "RAnderson@hotmail.com", 1000)
liz = User("Elibeth McKnight", 43, "March 23rd, 1978",
           "EMcKnight@gmail.com", 10300)

print(sara.name)
