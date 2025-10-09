x=4
p=1

def hello():
    global p
    p=34
    x=5
    print(f"The Local X is {x}")
    print("Hello Fun")


print(f"The global x is {x}")
hello()
print(f"The global x is {x}")
print(f"Updaet a Value of a P using local {p}")