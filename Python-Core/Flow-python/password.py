import getpass
VALID_USERNAME = "Anirudh_1112"
VALID_PASSWORD = "annu"
user_name = input("Enter the user_name: ").strip()
psd = getpass.getpass("Password: ")
if user_name == VALID_USERNAME and psd == VALID_PASSWORD:
    print(f"Valid_user={user_name}")
else:
    print("Invalid_user")