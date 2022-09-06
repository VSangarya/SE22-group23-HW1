import csv_tests

t=Tests()

print(t.the(the))

if t.sym():
    print("PASSED")
else:
    print("FAILED")

if t.nums():
    print("PASSED")
else:
    print("FAILED")


if t.bignums():
    print("PASSED")
else:
    print("FAILED")
