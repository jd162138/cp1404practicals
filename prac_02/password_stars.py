""" Finds and checks length of user password """
MIN_CHARACTERS = 5


def main():
	password = get_password()
	print_password(password)


def print_password(password: str):
	print("*" * len(password))


def get_password() -> str:
	password = input("Enter a password: ")
	while len(password) < MIN_CHARACTERS:
		print("Error password too short")
		password = input("Enter a password: ")
	return password

main()