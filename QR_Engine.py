# @Author: Joshua Scina
# @Version: 2
# @Purpose: Create a QR Code using Python
import pyqrcode, PyInstaller.__main__, os

class QR_Code_Engine:
    # Generates the QR Code with specified url and name
    def gen_code(self, site: str = "www.google.com", name: str = "test_file", size: int = 6):
        if name.find(".") > 0:
            name = name.removesuffix(name[name.find("."):])
        url = pyqrcode.create(site, error='L', mode='binary')
        url.png(f"{name}.png", scale=size)

class Create_Exe:
    def __init__(self, name:str) -> None:
        self.icon = os.path.abspath("Icon\\qr_gen_icon.ico")
        self.name = name
    def run(self) -> None:
        PyInstaller.__main__.run([
            f'{self.name}.py',
            '--onedir',
            '--windowed',
            f'-i={self.icon}'
        ])

if __name__ == "__main__":
    build = Create_Exe("QR")
    build.run()