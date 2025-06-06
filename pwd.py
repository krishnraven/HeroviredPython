import re

def check_password_strength(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True

if __name__ == "__main__":
    password = input("Enter your password: ")
    if check_password_strength(password):
        print("✅ Strong password.")
    else:
        print("❌ Weak password. Ensure it has at least 8 characters, a mix of uppercase, lowercase, numbers, and special characters.")
