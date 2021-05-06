import pyotp
import os
from dotenv import load_dotenv

load_dotenv()


def get_totp_code():
    totp_secret = os.environ["TOTP_SECRET"]
    totp = pyotp.TOTP(totp_secret)

    totp_now = totp.now()
    return totp_now


# print(totp_now)
# print(totp.verify(totp_now))
