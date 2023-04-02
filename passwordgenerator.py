import random

upp_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # Letters That We Will use
low_letters = upp_letters.lower() # Letters din but lowercase
digits = "0123456789" # some numbers

upper, lower, nums = True, True, True # thi says kung ano ang gusto mo pong gamitin

all = "" # A variable containing all the letters and numbers

if upper:
    all += upp_letters # appending the LETTERS in the all variable
if lower:
    all += low_letters # appending low in the all variable
if nums:
    all += digits # appending digits in the all var

length = 16 # the length
amount = 10 # amount that will generate

for x in range(amount):
    # this just tells the system to pick a random length(16) letters and numbers in the "all" variable and print it
    password = "".join(random.sample(all, length))
    print(password)
