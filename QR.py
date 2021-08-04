import pyqrcode


# @Author: Joshua Scina
# @Version 2

class QR_Code:
    # Generates the QR Code with specified url and name
    def gen_code(self, site: str = "www.google.com", name: str = "test_file", size: int = 6):
        if name.find(".") > 0:
            name = name.removesuffix(name[name.find("."):])
        url = pyqrcode.create(site, error='L', mode='binary')
        url.png(f"{name}.png", scale=size)
