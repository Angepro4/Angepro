import math
def new_password(oldpassword, newpassword):
    if oldpassword != newpassword and len(newpassword) >=7:
        return True
    else:
        return False
print(new_password('wachtwoord', 'Niuewwachtwoord'))


