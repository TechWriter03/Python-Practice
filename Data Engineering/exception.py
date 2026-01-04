x = "10"

try:
    if (x>10):
        print("greater than 10")
    else:
        print("less than 10")
except Exception as e:
    print("error message -",e)
finally:
    print("always run")

print("rest of code")
print()


def func(x):
    try:
        if (x%2==0):
            return 1
    except Exception as e:
        return e
    finally:
        print("always run")
    print("rest of code")

print(func(1))
print(func(2))
print()

age = 17
if age<18:
    # raise ValueError("age should be more than 18")
    raise Exception("age should be more than 18")