# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Cosas de guardar\Uni\Año 5\Segundo cuatrimestre\Inteligencia artificial 2\TP Integrador\Codigo\Codigo Fuente\Interfaz_Grafica.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form3(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1189, 560)
        Form.setMaximumSize(QtCore.QSize(10000, 10000))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setSpacing(9)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_5 = QtWidgets.QFrame(Form)
        self.frame_5.setStyleSheet("")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalSlider = QtWidgets.QSlider(self.frame_5)
        self.horizontalSlider.setGeometry(QtCore.QRect(10, 10, 231, 27))
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(15)
        self.horizontalSlider.setPageStep(12)
        self.horizontalSlider.setProperty("value", 1)
        self.horizontalSlider.setSliderPosition(1)
        self.horizontalSlider.setTracking(True)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.horizontalSlider.setTickInterval(1)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.mostrarK = QtWidgets.QLineEdit(self.frame_5)
        self.mostrarK.setGeometry(QtCore.QRect(250, 10, 41, 20))
        self.mostrarK.setReadOnly(True)
        self.mostrarK.setObjectName("mostrarK")
        self.pushButton = QtWidgets.QPushButton(self.frame_5)
        self.pushButton.setGeometry(QtCore.QRect(300, 10, 81, 21))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.frame_5, 1, 0, 1, 1)
        self.frame_6 = QtWidgets.QFrame(Form)
        self.frame_6.setStyleSheet("")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.gridLayout.addWidget(self.frame_6, 1, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setStyleSheet(".QFrame{border: 1px solid rgb(159, 159, 159);}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setSpacing(9)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.frame_2)
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.gridLayout_3.addWidget(self.plainTextEdit_2, 1, 1, 1, 1)
        self.grafica2 = QtWidgets.QVBoxLayout()
        self.grafica2.setObjectName("grafica2")
        self.gridLayout_3.addLayout(self.grafica2, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 1, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 3)
        self.gridLayout_3.setColumnStretch(1, 1)
        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setStyleSheet(".QFrame{border: 1px solid rgb(159, 159, 159);}")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(9, -1, -1, -1)
        self.gridLayout_2.setSpacing(9)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.frame)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout_2.addWidget(self.plainTextEdit, 1, 0, 1, 1)
        self.grafica1 = QtWidgets.QVBoxLayout()
        self.grafica1.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.grafica1.setObjectName("grafica1")
        self.gridLayout_2.addLayout(self.grafica1, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 3)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Aplicar K"))
        self.pushButton_3.setText(_translate("Form", "Mostrar K óptimo"))
        self.pushButton_2.setText(_translate("Form", "Volver"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\">Algoritmo K-nn Ponderado</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\">Datos</span></p></body></html>"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\">Algoritmo K-nn</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\">Datos</span></p></body></html>"))
