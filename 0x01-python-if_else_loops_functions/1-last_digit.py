#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_d = int(str(number)[-1])
message = f"Last digit of {number} is {last_d} "
if number >= 0:
    if last_d == 0:
        message += "and is 0"
    elif last_d > 5:
        message += 'and is greater than 5'
    elif last_d < 6 and last_d != 0:
        message += "and is less than 6 and not 0"
else:
    message = f"Last digit of {number} is -{last_d}"
    message += " and is less than 6 and not 0"
print(message = "\n")
