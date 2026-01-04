print("-----Password Strength Checker-----")
password=input("Enter password: ")
upper=False
digit=False
for ch in password:
    if ch.isupper():
        has_upper = True
    if ch.isdigit():
        has_digit = True

if len(password) >= 8 and has_upper and has_digit:
    print("Strong Password")
elif len(password) >= 6:
    print("Medium Password")
else:
    print("Weak Password")

print("-----Palindrome Checker-----")
text=input("Enter text")
if text == text[::-1]:
    print("Palindrome")
else :
    print("Not Palindrome")
