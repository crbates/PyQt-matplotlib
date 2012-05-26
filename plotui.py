# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plot.ui'
#
# Created: Sat Jan 14 15:39:51 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_plotview(object):
    def setupUi(self, plotview):
        plotview.setObjectName(_fromUtf8("plotview"))
        plotview.resize(934, 540)
        plotview.setWindowTitle(QtGui.QApplication.translate("plotview", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(plotview)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        spacerItem = QtGui.QSpacerItem(20, 60, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 0, 1, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 2, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.start = QtGui.QPushButton(self.groupBox_2)
        self.start.setText(QtGui.QApplication.translate("plotview", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.start.setObjectName(_fromUtf8("start"))
        self.verticalLayout.addWidget(self.start)
        self.stop = QtGui.QPushButton(self.groupBox_2)
        self.stop.setText(QtGui.QApplication.translate("plotview", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.stop.setObjectName(_fromUtf8("stop"))
        self.verticalLayout.addWidget(self.stop)
        self.save = QtGui.QPushButton(self.groupBox_2)
        self.save.setText(QtGui.QApplication.translate("plotview", "Save Data", None, QtGui.QApplication.UnicodeUTF8))
        self.save.setObjectName(_fromUtf8("save"))
        self.verticalLayout.addWidget(self.save)
        self.clear = QtGui.QPushButton(self.groupBox_2)
        self.clear.setText(QtGui.QApplication.translate("plotview", "Clear Data", None, QtGui.QApplication.UnicodeUTF8))
        self.clear.setObjectName(_fromUtf8("clear"))
        self.verticalLayout.addWidget(self.clear)
        self.exit = QtGui.QPushButton(self.groupBox_2)
        self.exit.setText(QtGui.QApplication.translate("plotview", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.exit.setObjectName(_fromUtf8("exit"))
        self.verticalLayout.addWidget(self.exit)
        self.gridLayout_3.addWidget(self.groupBox_2, 1, 1, 1, 1)
        plotview.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(plotview)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 934, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        plotview.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(plotview)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        plotview.setStatusBar(self.statusbar)

        self.retranslateUi(plotview)
        QtCore.QObject.connect(self.exit, QtCore.SIGNAL(_fromUtf8("clicked()")), plotview.close)
        QtCore.QMetaObject.connectSlotsByName(plotview)

    def retranslateUi(self, plotview):
        pass

