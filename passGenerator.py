
import string
import random
def randomString(stringLength):
    """Generate a random string of 5 charcters"""
    letters = string.ascii_letters
    numbers = string.digits
    imges = string.punctuation
    alpha = letters + numbers + imges
    return ''.join(random.choice(alpha) for i in range(stringLength))

print ("Random String is ", randomString(15) )