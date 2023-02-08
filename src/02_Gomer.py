print("Enter your weight: ")
weight = int(input(">>> "))
print("Enter your desired weight: ")
desired_weight = int(input(">>> "))
while weight >= desired_weight:
    weight = weight - (weight / 100 * 5)
    print(weight)
