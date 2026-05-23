# Validate mobile number
import re
mobile = "9876543218"
pattern = r"^[6-9]\d{9}$"  # start should be between 6-9 and rest of the other 9 digits can be anything between 0 -9
if re.match(pattern,mobile):
    print("Mobile is valid")
else:
    print("Mobile is not valid")

# Validating email id

email = "test@gmail.com"

pattern = r"^[a-zA-Z0-9_.]+@[a-z]+\.[a-z]{2,}$"

if re.match(pattern,email):
    print("Email is valid")
else:
    print("Email is not valid")