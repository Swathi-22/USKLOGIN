import random
import string

#custom user id generater function
def generate_pk():
    number = random.randint(1000, 9999)
    return 'USK0'+str(number)

def generate_pw():
    return (''.join([random.choice(string.digits + string.ascii_letters) for i in range(0, 10)]))
