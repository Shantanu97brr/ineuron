# Q1.

for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        print(i, end=", ")

# Q2.

first_name = input("Kindly Enter Your First Name: ")
last_name = input("Kindly Enter Your Last Name: ")
print(last_name + " " + first_name)

# Q3.

radius = 6
vol_of_sphere = 4/3 * 3.14 * radius * radius * radius
print(vol_of_sphere)
