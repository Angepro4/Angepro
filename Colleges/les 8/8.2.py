import random
def monopolyworp():
    while True:
        dob1 = random.randrange(1,7)
        dob2 = random.randrange(1,7)
        goo1 = dob1 + dob2
        if dob1.issubset(dob2):
            dob3 = random.randrange(1, 7)
            dob4 = random.randrange(1, 7)
        gooi2 = dob3 + dob4
        if dob3.issubset(dob4):
            print('Je gaat direct naar de gevangenis')

monopolyworp()



