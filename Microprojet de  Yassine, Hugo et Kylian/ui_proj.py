# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'proj.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(766, 354)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.selectionEdit = QtWidgets.QLineEdit(self.groupBox)
        self.selectionEdit.setObjectName("selectionEdit")
        self.horizontalLayout.addWidget(self.selectionEdit)
        self.selectButton = QtWidgets.QToolButton(self.groupBox)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/media-playback-start-symbolic.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.selectButton.setIcon(icon)
        self.selectButton.setObjectName("selectButton")
        self.horizontalLayout.addWidget(self.selectButton)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.groupBox)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 766, 20))
        self.menubar.setObjectName("menubar")
        self.menuFichier = QtWidgets.QMenu(self.menubar)
        self.menuFichier.setObjectName("menuFichier")
        self.menuAide = QtWidgets.QMenu(self.menubar)
        self.menuAide.setObjectName("menuAide")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionEnregistrer_Sous = QtWidgets.QAction(MainWindow)
        self.actionEnregistrer_Sous.setObjectName("actionEnregistrer_Sous")
        self.actionQuitter = QtWidgets.QAction(MainWindow)
        self.actionQuitter.setObjectName("actionQuitter")
        self.actionAide_F1 = QtWidgets.QAction(MainWindow)
        self.actionAide_F1.setObjectName("actionAide_F1")
        self.action_propos = QtWidgets.QAction(MainWindow)
        self.action_propos.setObjectName("action_propos")
        self.menuFichier.addAction(self.actionEnregistrer_Sous)
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionQuitter)
        self.menuAide.addSeparator()
        self.menuAide.addAction(self.actionAide_F1)
        self.menuAide.addAction(self.action_propos)
        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuAide.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Expositions"))
        self.groupBox.setTitle(_translate("MainWindow", "Choisir"))
        self.label.setText(_translate("MainWindow", "Sélection"))
        self.selectButton.setToolTip(_translate("MainWindow", "Appliquer la sélection"))
        self.selectButton.setText(_translate("MainWindow", "..."))
        self.pushButton.setText(_translate("MainWindow", "Aide "))
        self.pushButton_2.setText(_translate("MainWindow", "À propos"))
        self.menuFichier.setTitle(_translate("MainWindow", "Fichier"))
        self.menuAide.setTitle(_translate("MainWindow", "Aide"))
        self.actionEnregistrer_Sous.setText(_translate("MainWindow", "Enregistrer Sous ..."))
        self.actionQuitter.setText(_translate("MainWindow", "Quitter"))
        self.actionAide_F1.setText(_translate("MainWindow", "Aide (F1)"))
        self.action_propos.setText(_translate("MainWindow", "À propos"))
