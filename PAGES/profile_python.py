# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Birol/Desktop/ESSK/assets/GUI/profile.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 476)
        Form.setMinimumSize(QtCore.QSize(400, 400))
        Form.setMaximumSize(QtCore.QSize(450, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/assets/essk.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.tc_edit = QtWidgets.QLineEdit(Form)
        self.tc_edit.setObjectName("tc_edit")
        self.horizontalLayout.addWidget(self.tc_edit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.isim_edit = QtWidgets.QLineEdit(Form)
        self.isim_edit.setObjectName("isim_edit")
        self.horizontalLayout_7.addWidget(self.isim_edit)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.soyad_edit = QtWidgets.QLineEdit(Form)
        self.soyad_edit.setObjectName("soyad_edit")
        self.horizontalLayout_6.addWidget(self.soyad_edit)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.phone_edit = QtWidgets.QLineEdit(Form)
        self.phone_edit.setObjectName("phone_edit")
        self.horizontalLayout_3.addWidget(self.phone_edit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.brans_comboBox = QtWidgets.QComboBox(Form)
        self.brans_comboBox.setObjectName("brans_comboBox")
        self.brans_comboBox.addItem("")
        self.brans_comboBox.addItem("")
        self.brans_comboBox.addItem("")
        self.brans_comboBox.addItem("")
        self.brans_comboBox.addItem("")
        self.horizontalLayout_4.addWidget(self.brans_comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.register_edit = QtWidgets.QLineEdit(Form)
        self.register_edit.setObjectName("register_edit")
        self.horizontalLayout_5.addWidget(self.register_edit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.register_finish_edit = QtWidgets.QLineEdit(Form)
        self.register_finish_edit.setObjectName("register_finish_edit")
        self.horizontalLayout_2.addWidget(self.register_finish_edit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_12.addWidget(self.label_12)
        self.veli_name_edit = QtWidgets.QLineEdit(Form)
        self.veli_name_edit.setObjectName("veli_name_edit")
        self.horizontalLayout_12.addWidget(self.veli_name_edit)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_11.addWidget(self.label_14)
        self.veli_phone_edit = QtWidgets.QLineEdit(Form)
        self.veli_phone_edit.setObjectName("veli_phone_edit")
        self.horizontalLayout_11.addWidget(self.veli_phone_edit)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_16.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.photo_label = QtWidgets.QLabel(Form)
        self.photo_label.setMinimumSize(QtCore.QSize(200, 200))
        self.photo_label.setText("")
        self.photo_label.setObjectName("photo_label")
        self.verticalLayout_4.addWidget(self.photo_label)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.idcard = QtWidgets.QPushButton(Form)
        self.idcard.setMaximumSize(QtCore.QSize(100, 100))
        self.idcard.setIconSize(QtCore.QSize(10, 10))
        self.idcard.setObjectName("idcard")
        self.horizontalLayout_14.addWidget(self.idcard)
        self.pick_photo_button = QtWidgets.QPushButton(Form)
        self.pick_photo_button.setObjectName("pick_photo_button")
        self.horizontalLayout_14.addWidget(self.pick_photo_button)
        self.verticalLayout_5.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.psiko_button = QtWidgets.QPushButton(Form)
        self.psiko_button.setObjectName("psiko_button")
        self.horizontalLayout_19.addWidget(self.psiko_button)
        self.matches_button = QtWidgets.QPushButton(Form)
        self.matches_button.setObjectName("matches_button")
        self.horizontalLayout_19.addWidget(self.matches_button)
        self.verticalLayout_5.addLayout(self.horizontalLayout_19)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.horizontalLayout_13.addLayout(self.verticalLayout_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)
        self.lisans_no_edit = QtWidgets.QLineEdit(Form)
        self.lisans_no_edit.setObjectName("lisans_no_edit")
        self.horizontalLayout_10.addWidget(self.lisans_no_edit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.date_of_birth_date_edit = QtWidgets.QLabel(Form)
        self.date_of_birth_date_edit.setObjectName("date_of_birth_date_edit")
        self.horizontalLayout_8.addWidget(self.date_of_birth_date_edit)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.date_of_birth_edit = QtWidgets.QLineEdit(Form)
        self.date_of_birth_edit.setObjectName("date_of_birth_edit")
        self.horizontalLayout_8.addWidget(self.date_of_birth_edit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem4)
        self.hes_code_edit = QtWidgets.QLineEdit(Form)
        self.hes_code_edit.setObjectName("hes_code_edit")
        self.horizontalLayout_9.addWidget(self.hes_code_edit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_17.addWidget(self.label_8)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem5)
        self.kusak_edit = QtWidgets.QLineEdit(Form)
        self.kusak_edit.setObjectName("kusak_edit")
        self.horizontalLayout_17.addWidget(self.kusak_edit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_18.addWidget(self.label_13)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem6)
        self.mail_edit = QtWidgets.QLineEdit(Form)
        self.mail_edit.setObjectName("mail_edit")
        self.horizontalLayout_18.addWidget(self.mail_edit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.update_pushButton = QtWidgets.QPushButton(Form)
        self.update_pushButton.setObjectName("update_pushButton")
        self.horizontalLayout_15.addWidget(self.update_pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16.addLayout(self.verticalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Detay Sayfası"))
        self.label.setText(_translate("Form", " TC :     "))
        self.label_7.setText(_translate("Form", "İsim :    "))
        self.label_6.setText(_translate("Form", "Soyad : "))
        self.label_3.setText(_translate("Form", "Telefon : "))
        self.label_4.setText(_translate("Form", "Branş : "))
        self.brans_comboBox.setItemText(0, _translate("Form", "Taekwondo"))
        self.brans_comboBox.setItemText(1, _translate("Form", "Judo"))
        self.brans_comboBox.setItemText(2, _translate("Form", "Pilates"))
        self.brans_comboBox.setItemText(3, _translate("Form", "Karate"))
        self.brans_comboBox.setItemText(4, _translate("Form", "Fitness"))
        self.label_5.setText(_translate("Form", "Kayit Tarihi :"))
        self.label_2.setText(_translate("Form", "Bitiş Tarihi : "))
        self.label_12.setText(_translate("Form", "Veli Adı :     "))
        self.label_14.setText(_translate("Form", "Veli phone:"))
        self.idcard.setText(_translate("Form", "ID CARD"))
        self.pick_photo_button.setText(_translate("Form", "Fotoğraf Seç"))
        self.psiko_button.setText(_translate("Form", "Psiko"))
        self.matches_button.setText(_translate("Form", "Matches"))
        self.label_10.setText(_translate("Form", "Lisans No : "))
        self.date_of_birth_date_edit.setText(_translate("Form", "Doğum Tarihi : "))
        self.label_9.setText(_translate("Form", "Hes Kodu : "))
        self.label_8.setText(_translate("Form", "Kuşak : "))
        self.label_13.setText(_translate("Form", "Mail Adresi:"))
        self.update_pushButton.setText(_translate("Form", "Güncelle"))

import assets.py_rc.icons_rc as icons_rc
