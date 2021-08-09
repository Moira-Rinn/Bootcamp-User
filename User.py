class User:
    def __init__(self, name, age, dob, email, balance):
        self.name = name
        self.age = age
        self.dob = dob
        self.email = email
        self.account_balance = balance

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdral(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        return round(self.account_balance, 2)

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount


sara = User("Sara McCloud", 27, "July 19th, 1994", "SMcCloud@gmail.com", 1300)
rachael = User("Rachael Anderson", 19, "October 31st, 2002",
               "RAnderson@hotmail.com", 1000)
liz = User("Elibeth McKnight", 43, "March 23rd, 1978",
           "EMcKnight@gmail.com", 10300)

sara.make_deposit(657.39)
sara.make_deposit(643.74)
sara.make_withdral(173.27)
sara.make_deposit(678.92)
print(sara.display_user_balance())


rachael.make_deposit(358.69)
rachael.make_withdral(97.19)
rachael.make_deposit(412.12)
rachael.make_withdral(103.67)
print(rachael.display_user_balance())

liz.make_deposit(1243.89)
liz.make_withdral(872.09)
liz.make_deposit(337.23)
print(liz.display_user_balance())

sara.transfer_money(liz, 100)
print(sara.display_user_balance())
print(liz.display_user_balance())
