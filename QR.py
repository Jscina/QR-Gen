import pyqrcode


# @Author: Joshua Scina
# @Version 1.0

class QR_Code:
    # Generates the QR Code with specified url and name
    def gen_code(self, site, name):
        url = pyqrcode.create(site)
        url.png(f"{name}.png", scale=6)
