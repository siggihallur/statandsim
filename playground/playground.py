"""
    this script is to calculate possible income on a website
"""

# advertising cost per day
add_small = 500
add_medium = 750
add_big = 1000
add_special = 5000

max_add_small = 6
max_add_medium = 4
max_add_big = 2
max_add_special = 1

# subscription cost per month
pick_01 = 400
pick_02 = 650
pick_03 = 900
pick_all = 1500

# scenario one

adds_01 = (add_small * 6 + add_medium * 4 + add_big * 2  + add_special * 0.33) * 30
sub_01 = (pick_01 * 2000 + pick_02 * 800 + pick_03 * 200 + pick_all * 30)

print("Adds income: " + str(adds_01))
print("Subscription income: " + str(sub_01))

total = adds_01 + sub_01

print("Total income: " + str(total))

staff = 3
staffExpence = 1000000/12

print(total - staffExpence * staff)
