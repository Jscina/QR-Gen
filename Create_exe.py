import PyInstaller.__main__, os

class Create_exe:
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
    build = Create_exe("QR_Gen")
    build.run()