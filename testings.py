import time
value1 = int(input("value?"))
value2 = 24

def check():
    if value1 > value2:
        print("value is over 24")

print("in one second there should be a check")
time.sleep(1)
check()