# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2, sys

import tensorflow as tf

gpus = tf.config.list_physical_devices('GPU')
try:
    tf.config.experimental.set_memory_growth(gpus[0], True)
    print(gpus[0])
except:
    print("No GPUs")


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1123, 917)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 70, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 370, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 500, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 500, 491, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 70, 491, 371))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(190, 710, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(480, 710, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1123, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(lambda: self.open_image())
        self.pushButton_2.clicked.connect(lambda: self.model_())
        self.pushButton_3.clicked.connect(lambda: self.predict_(self.model))
        self.pushButton_4.clicked.connect(lambda: self.reset_())
        self.pushButton_5.clicked.connect(lambda: sys.exit())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "OPEN IMAGE"))
        self.pushButton_2.setText(_translate("MainWindow", "CHOOSE MODEL"))
        self.pushButton_3.setText(_translate("MainWindow", "GET DIAGNOSIS"))
        self.pushButton_4.setText(_translate("MainWindow", "RESET"))
        self.pushButton_5.setText(_translate("MainWindow", "EXIT"))

    def open_image(self):
        self.label.clear()
        self.file_path, _ = QtWidgets.QFileDialog.getOpenFileName()
        pixmap = QtGui.QPixmap(self.file_path)
        self.label_2.setPixmap(pixmap.scaled(self.label_2.width(), self.label_2.height(), QtCore.Qt.KeepAspectRatio))

    def model_(self):
        self.model_path, _ = QtWidgets.QFileDialog.getOpenFileName()
        self.model = tf.keras.models.load_model(self.model_path)
        print(self.model.summary())

    def predict_(self, model):
        import numpy as np
        img = np.array([cv2.resize(cv2.imread(self.file_path), (224, 224))])
        pred = np.argmax(model.predict(img), axis=1)
        if pred == 1:
            self.label.setText("PRESENCE OF INFILTRATES IN LUNGS, INDICATION OF PNEUMONIA, MAYBE COVID-19")
            self.label.setWordWrap(True)
            self.label.adjustSize()
        elif pred == 0:
            self.label.setText("NORMAL LUNGS, NO PNEUMONIA/COVID-19")
            self.label.setWordWrap(True)
            self.label.adjustSize()

    def reset_(self):
        self.label.setText("")
        self.label_2.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())
