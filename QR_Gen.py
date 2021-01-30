import os

from PyQt5 import QtCore, QtWidgets, QtGui

from QR import QR_Code


# @Author: Joshua Scina
# @Version 1.1

class Ui_GenerateQR(object):
    def setupUi(self, GenerateQR):
        GenerateQR.setObjectName("GenerateQR")
        GenerateQR.resize(800, 600)
        GenerateQR.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                 "color: rgb(255, 255, 255);")
        if os.path.exists(os.path.abspath("Icon\\qr_gen_icon.ico")):
            GenerateQR.setWindowIcon(QtGui.QIcon(os.path.abspath('Icon\\qr_gen_icon.ico')))
        else:
            GenerateQR.setWindowIcon(QtGui.QIcon(os.path.abspath('qr_gen_icon.ico')))
        # Set the font
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)

        self.central_widget = QtWidgets.QWidget(GenerateQR)
        self.central_widget.setObjectName("central_widget")
        self.gridLayout = QtWidgets.QGridLayout(self.central_widget)
        self.gridLayout.setObjectName("gridLayout")

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 5, 9, 1)
        self.url_label = QtWidgets.QLabel(self.central_widget)

        self.url_label.setObjectName("url_label")
        self.gridLayout.addWidget(self.url_label, 2, 2, 1, 1)
        self.url_input = QtWidgets.QLineEdit(self.central_widget)
        self.url_input.setStyleSheet("background-color: rgb(100, 100, 100);\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "border-radius: 5px;")
        self.url_input.setObjectName("url_input")

        self.gridLayout.addWidget(self.url_input, 3, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 8, 2, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 1, 9, 1)
        self.filename_input = QtWidgets.QLineEdit(self.central_widget)
        self.filename_input.setStyleSheet("background-color: rgb(100, 100, 100);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border-radius: 5px;")
        self.filename_input.setObjectName("filename_input")

        self.gridLayout.addWidget(self.filename_input, 7, 2, 1, 1)
        self.file_name_label = QtWidgets.QLabel(self.central_widget)
        self.file_name_label.setObjectName("file_name_label")

        self.gridLayout.addWidget(self.file_name_label, 6, 2, 1, 1)
        self.scale_input = QtWidgets.QLineEdit(self.central_widget)
        self.scale_input.setStyleSheet("background-color: rgb(100, 100, 100);\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "border-radius: 5px;")
        self.scale_input.setObjectName("scale_input")

        self.gridLayout.addWidget(self.scale_input, 5, 2, 1, 1)
        self.scale_label = QtWidgets.QLabel(self.central_widget)
        self.scale_label.setObjectName("scale_label")

        self.gridLayout.addWidget(self.scale_label, 4, 2, 1, 1)
        self.path_label = QtWidgets.QLabel(self.central_widget)
        self.path_label.setObjectName("path_label")

        self.gridLayout.addWidget(self.path_label, 7, 3, 1, 1)

        self.generate_button = QtWidgets.QPushButton(self.central_widget)
        self.generate_button.setStyleSheet("background-color: rgb(100, 100, 100);")
        self.generate_button.setObjectName("generate_button")
        self.generate_button.clicked.connect(self.gen)

        self.gridLayout.addWidget(self.generate_button, 5, 3, 1, 1)
        GenerateQR.setCentralWidget(self.central_widget)

        self.retranslateUi(GenerateQR)
        QtCore.QMetaObject.connectSlotsByName(GenerateQR)

    def retranslateUi(self, GenerateQR):
        _translate = QtCore.QCoreApplication.translate
        GenerateQR.setWindowTitle(_translate("GenerateQR", "QR Code Generator"))
        self.url_label.setText(_translate("GenerateQR", "Enter Url:"))
        self.url_input.setPlaceholderText(_translate("GenerateQR", "Ex: www.google.com"))
        self.filename_input.setPlaceholderText(_translate("GenerateQR", "Ex: myfile"))
        self.file_name_label.setText(_translate("GenerateQR", "File Name Without Extension"))
        self.scale_input.setPlaceholderText(_translate("GenerateQR", "Ex: 1"))
        self.scale_label.setText(_translate("GenerateQR", "Scale:"))
        self.path_label.setText(_translate("GenerateQR", "Path to File: None"))
        self.generate_button.setText(_translate("GenerateQR", "Generate"))

    # Calls the QR Code generator
    def gen(self):
        # Get the input from the lineEdits
        url = self.url_input.text()
        filename = self.filename_input.text()

        try:
            scale = int(self.scale_input.text())
        except ValueError:
            scale = 6  # Default scale

        # Create QR_Code object
        create_qr = QR_Code()

        # Generate QR Code
        create_qr.gen_code(site=url, name=filename, size=scale)

        # Clear input fields
        self.url_input.clear()
        self.scale_input.clear()
        self.filename_input.clear()

        # Check if file is created successfully
        self.check_success(filename)
        del url, filename

    def check_success(self, filename: str):
        # If file exist report path else report failed
        if os.path.exists(os.path.abspath(f"{filename}.png")):
            path = os.path.abspath(f"{filename}.png")
            self.path_label.setText(f"Path to file:\n{path}")
        else:
            self.path_label.setText("File creation failed!")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    GenerateQR = QtWidgets.QMainWindow()
    ui = Ui_GenerateQR()
    ui.setupUi(GenerateQR)
    GenerateQR.show()
    sys.exit(app.exec_())
