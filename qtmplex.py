# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 15:43:07 2012

Example matplotlib and pyqt file that adds a random number to a plot every 0.5
seconds. The plot can be started, stopped, cleared and saved.

@author: cameron bates
"""
import sys
from qtmpl import MyMplCanvas
from plotui import *
import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui
import numpy as np


class plotview(QtGui.QMainWindow):
    def __init__(self, parent=None,cmdpipes = None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_plotview()
        self.ui.setupUi(self)
        
        self.layout = QtGui.QVBoxLayout(self.ui.groupBox)
        self.figure = MyMplCanvas(self.ui.centralwidget, width=5, height=4, dpi=100)
        self.layout.addWidget(self.figure.canvas)
        self.layout.addWidget(self.figure.mpl_toolbar)        
        
        QtCore.QObject.connect(self.ui.start,QtCore.SIGNAL("clicked()"),self.start)
        QtCore.QObject.connect(self.ui.stop,QtCore.SIGNAL("clicked()"),self.stop)
        QtCore.QObject.connect(self.ui.save,QtCore.SIGNAL("clicked()"),self.save)
        QtCore.QObject.connect(self.ui.clear,QtCore.SIGNAL("clicked()"),self.clear)
        self.timer = QtCore.QTimer(self)
        QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), self.update_figure)
        self.running = False        
        self.data = []        
    def start(self):
        if self.running == False:
            self.timer.start(500)
            self.running = True
        
    def stop(self):
        if self.running == True:
            self.timer.stop()
            self.running = False
        
    def update_figure(self):
        #get data from keithley here        
        self.data.append(np.random.rand()) 
        
        self.figure.axes.plot(self.data)
        self.figure.canvas.draw()
        
    def save(self):
        np.save('data',self.data)
        
    def clear(self):
        self.data = []
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    plot = plotview()
    plot.show()
    if app.exec_():
        pass
