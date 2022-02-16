import string
import pyperclip 
import secrets


alphabet = string.ascii_letters + string.digits + string.punctuation

while True:
    pwlen = secrets.randbelow(30)
    if pwlen >= 18: break
    
while True:
    password = ''.join(secrets.choice(alphabet) for i in range(pwlen))
    if (sum(c.islower() for c in password) >=3
            and sum(c.isupper() for c in password) >=3
            and sum(c.isdigit() for c in password) >=3):
        break

pyperclip.copy(str(password))
print(pyperclip.paste())

print("Password copied to clipboard. Pw length: " + str(pwlen))
input("Press Enter to continue...")
