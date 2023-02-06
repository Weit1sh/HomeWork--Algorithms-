print("Enter the number of students")
n = int(input(">>> "))
print("Enter the number of students who passed the session perfectly")
s = int(input(">>> "))
print("Enter the total amount of funds allocated for scholarships")
m = int(input(">>> "))
s_money = (m / s)
print("The amount received by students who passed the session with excellence = " + str(s_money))

print("-------")


n_money = (m / n)
all_money = (s_money - n_money)
print("If all students passed the session with excellence, then students who passed the session with excellence will receive " + str(all_money) + " less")