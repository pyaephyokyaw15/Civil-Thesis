# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    import pyotp
    import hashlib

    # Generate OTP
    otp_secret = pyotp.random_base32()
    otp = pyotp.TOTP(otp_secret)
    otp_value = otp.now()
    print("Generated OTP:", otp_value)

    # Hash OTP
    hashed_otp = hashlib.sha256(otp_value.encode()).hexdigest()
    print("Hashed OTP:", hashed_otp)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
