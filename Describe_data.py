# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Describe_data.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_desc_data(object):
    def setupUi(self, desc_data):
        desc_data.setObjectName("desc_data")
        desc_data.resize(499, 250)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/acer/Downloads/logo.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        desc_data.setWindowIcon(icon)
        desc_data.setStyleSheet("border-image: url(:/images/BackGround.jpg);")
        self.gridLayout = QtWidgets.QGridLayout(desc_data)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(desc_data)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.comboBox = QtWidgets.QComboBox(desc_data)
        self.comboBox.setStyleSheet("border-image: url(:/images/1WhiteBackground.jpg);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(38, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.label_2 = QtWidgets.QLabel(desc_data)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem6 = QtWidgets.QSpacerItem(148, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.comboBox_2 = QtWidgets.QComboBox(desc_data)
        self.comboBox_2.setStyleSheet("border-image: url(:/images/1WhiteBackground.jpg);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        spacerItem7 = QtWidgets.QSpacerItem(48, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem9 = QtWidgets.QSpacerItem(218, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.buttonBox = QtWidgets.QDialogButtonBox(desc_data)
        self.buttonBox.setStyleSheet("border-image: url(:/images/1WhiteBackground.jpg);")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_3.addWidget(self.buttonBox)
        spacerItem10 = QtWidgets.QSpacerItem(48, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(desc_data)
        self.buttonBox.accepted.connect(self.desc)
        self.buttonBox.rejected.connect(desc_data.reject)
        QtCore.QMetaObject.connectSlotsByName(desc_data)

    def retranslateUi(self, desc_data):
        _translate = QtCore.QCoreApplication.translate
        desc_data.setWindowTitle(_translate("desc_data", "Describe Data"))
        self.label.setText(_translate("desc_data", "<html><head/><body><p><span style=\" color:#ffffff;\">What do you want to describe ?</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("desc_data", "SELECT"))
        self.comboBox.setItemText(1, _translate("desc_data", "Headers"))
        self.comboBox.setItemText(2, _translate("desc_data", "Column"))
        self.comboBox.setItemText(3, _translate("desc_data", "Datatypes"))
        self.comboBox.setItemText(4, _translate("desc_data", "Statistics"))
        self.label_2.setText(_translate("desc_data", "<html><head/><body><p><span style=\" color:#ffffff;\">Choose Column : </span></p></body></html>"))
        self.comboBox_2.setItemText(0, _translate("desc_data", "SELECT"))
import Images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    desc_data = QtWidgets.QDialog()
    ui = Ui_desc_data()
    ui.setupUi(desc_data)
    desc_data.show()
    sys.exit(app.exec_())
