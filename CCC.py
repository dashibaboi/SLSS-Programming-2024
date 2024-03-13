box_eight = int(input("How many boxes of 8 are there? "))
box_three = int(input("How many boxes of 3 are there? "))

total_cakes = box_eight*8 + box_three*3

final = total_cakes - 28

print(f"There will be",final, "cakes left")