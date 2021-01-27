from PyQt5 import QtCore, QtGui, QtWidgets

from QR import QR_Code

import os


# @Author: Joshua Scina
# @Version 1.0

class Ui_GenerateQR(object):
    # Setup the UI
    def setupUi(self, GenerateQR):
        GenerateQR.setObjectName("GenerateQR")
        GenerateQR.resize(800, 600)
        GenerateQR.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                 "color: rgb(255, 255, 255);")
        GenerateQR.setWindowIcon(QtGui.QIcon(os.path.abspath('Icon\\qr_gen_icon.ico')))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.central_widget = QtWidgets.QWidget(GenerateQR)
        self.central_widget.setObjectName("central_widget")
        self.gridLayout = QtWidgets.QGridLayout(self.central_widget)

        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 4, 7, 1)

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
        self.gridLayout.addItem(spacerItem2, 6, 2, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 1, 7, 1)

        self.filename_input = QtWidgets.QLineEdit(self.central_widget)
        self.filename_input.setStyleSheet("background-color: rgb(100, 100, 100);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border-radius: 5px;")
        self.filename_input.setObjectName("filename_input")

        self.gridLayout.addWidget(self.filename_input, 5, 2, 1, 1)
        self.file_name_label = QtWidgets.QLabel(self.central_widget)
        self.file_name_label.setObjectName("file_name_label")

        self.gridLayout.addWidget(self.file_name_label, 4, 2, 1, 1)
        self.generate_button = QtWidgets.QPushButton(self.central_widget)
        self.generate_button.setStyleSheet("background-color: rgb(100, 100, 100);")
        self.generate_button.setObjectName("generate_button")
        self.generate_button.clicked.connect(self.gen)

        self.gridLayout.addWidget(self.generate_button, 4, 3, 1, 1)
        GenerateQR.setCentralWidget(self.central_widget)

        self.retranslateUi(GenerateQR)
        QtCore.QMetaObject.connectSlotsByName(GenerateQR)

    def retranslateUi(self, GenerateQR):
        _translate = QtCore.QCoreApplication.translate
        GenerateQR.setWindowTitle(_translate("GenerateQR", "QR Code Generator"))
        self.url_label.setText(_translate("GenerateQR", "Enter Url:"))
        self.file_name_label.setText(_translate("GenerateQR", "File Name Without Extension"))
        self.generate_button.setText(_translate("GenerateQR", "Generate"))

    # Calls the QR Code generator
    def gen(self):
        # Get the input from the lineEdits
        url = self.url_input.text()
        filename = self.filename_input.text()
        # Create QR_Code object
        create_qr = QR_Code()
        # Generate QR Code
        create_qr.gen_code(url, filename)
        del url, filename
        # Clear input fields
        self.url_input.clear()
        self.filename_input.clear()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    GenerateQR = QtWidgets.QMainWindow()
    ui = Ui_GenerateQR()
    ui.setupUi(GenerateQR)
    GenerateQR.show()
    sys.exit(app.exec_())
