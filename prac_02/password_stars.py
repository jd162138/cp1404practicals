user_password = input("Enter a password: ")
while len(user_password) < 5:
	print("Error password too short")
	user_password = input("Enter a password: ")
print("*" * len(user_password))