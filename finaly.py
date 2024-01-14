# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)]
# Embedded file name: FINALOUTCOME.py
# Size of source mod 2**32: 227 bytes


class MissingDataException(Exception):

    def __init__(self, value):
        self._MissingDataException__value = value

    def __str__(self):
        return 'The ' + self._MissingDataException__value + ' text box is empty. You should provide this mandatory data!'


class PlatenumberException(Exception):
    pass


class cars:

    def __init__(self, make, fuel, model, color, paltenumber,registered=False):
        self._cars__make = make
        self._cars__fuel = fuel
        self._cars__model = model
        self._cars__color = color
        self._cars__platenumber = paltenumber
        self.__cars__registered = registered

    def getmake(self):
        return self._cars__make
    def getregistered(self):
        return self.__cars__registered
    
    def setregistered(self,registered):
        self.__cars__registered=registered

    def setmake(self, make):
        self._cars__make = make

    def getfuel(self):
        return self._cars__fuel

    def setfuel(self, fuel):
        self._cars__fuel = fuel

    def getmodel(self):
        return self._cars__model

    def setmodel(self, model):
        self._cars__model = model

    def getcolor(self):
        return self._cars__color

    def setcolor(self, color):
        self._cars__color = color

    def getplatenumber(self):
        return self._cars__platenumber

    def setplatenumber(self, platenm):
        self._cars__platenumber = platenm

    def __eq__(self, other):
        if self._cars__platenumber == other._cars__platenumber:
            return True
        return False

    def __le__(self, other):
        if self._cars__platenumber == other._cars__platenumber:
            return True
        if self._cars__platenumber < other._cars__platenumber:
            return True
        return False

    def __lt__(self, other):
        if self._cars__platenumber < other._cars__platenumber:
            return True
        return False

    def __str__(self):
        x = self._cars__make + '      ' + 'plate number:' + '(' + self._cars__platenumber + ')'
        return x



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import re
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os

class Ui_MainWindow(object):
    Fo = open('michel.txt', 'r')
    loon = []
    for i in Fo:
        #strips the new line from the end of each row
        z = i.strip()
        l = z.split(',')
        k = cars(l[0], l[1], l[2], l[3], l[4],True)
        if k not in loon:
            loon.append(k)

    babi = []
    carsinsys = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName('MainWindow')
        MainWindow.resize(800, 681)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 155, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(147, 147, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 155, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName('centralwidget')
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 0, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName('label')
        self.makeEdet = QtWidgets.QLineEdit(self.centralwidget)
        self.makeEdet.setGeometry(QtCore.QRect(250, 60, 361, 41))
        self.makeEdet.setObjectName('makeEdet')
        self.colorEdt = QtWidgets.QLineEdit(self.centralwidget)
        self.colorEdt.setGeometry(QtCore.QRect(260, 170, 351, 41))
        self.colorEdt.setObjectName('colorEdt')
        self.plateEdt = QtWidgets.QLineEdit(self.centralwidget)
        self.plateEdt.setGeometry(QtCore.QRect(260, 270, 351, 41))
        self.plateEdt.setObjectName('plateEdt')
        self.plateEdt.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plateEdt.setFont(font)
        self.modelEdt = QtWidgets.QLineEdit(self.centralwidget)
        self.modelEdt.setGeometry(QtCore.QRect(260, 220, 351, 41))
        self.modelEdt.setObjectName('modelEdt')
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(110, 360, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.save.setFont(font)
        self.save.setObjectName('save')
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 130, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName('label_2')
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(30, 330, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName('checkBox')
        self.AddCARbtn = QtWidgets.QPushButton(self.centralwidget)
        self.AddCARbtn.setGeometry(QtCore.QRect(250, 330, 93, 28))
        self.AddCARbtn.setObjectName('AddCARbtn')
        self.deletebtn = QtWidgets.QPushButton(self.centralwidget)
        self.deletebtn.setGeometry(QtCore.QRect(540, 330, 93, 28))
        self.deletebtn.setObjectName('deletebtn')
        self.modifybtn = QtWidgets.QPushButton(self.centralwidget)
        self.modifybtn.setGeometry(QtCore.QRect(380, 330, 93, 28))
        self.modifybtn.setObjectName('modifybtn')
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(100, 400, 531, 221))
        self.listWidget.setObjectName('listWidget')
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(280, 120, 291, 31))
        self.comboBox.setObjectName('comboBox')
        self.comboBox.addItem('')
        self.comboBox.addItem('')
        self.comboBox.addItem('')
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 70, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName('label_3')
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 180, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName('label_4')
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(90, 230, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName('label_5')
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 270, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName('label_6')
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(290, 370, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName('label_7')
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName('menubar')
        self.menusave_as = QtWidgets.QMenu(self.menubar)
        self.menusave_as.setObjectName('menusave_as')
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName('statusbar')
        MainWindow.setStatusBar(self.statusbar)
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setObjectName('actionsave')
        self.menusave_as.addAction(self.actionsave)
        self.menubar.addAction(self.menusave_as.menuAction())
        listt = []
        lolo = []
        if os.stat('mydatafor_reopen').st_size != 0:
            x = open('mydatafor_reopen', 'r')
            for i in x:
                strr = i.strip()
                nstr = strr.split()
                ca = cars(nstr[0], nstr[1], nstr[2], nstr[3], nstr[4])
                lolo.append(nstr[5])
                if nstr[5] == 'green':
                    ca.setregistered(True)
                if nstr[5]=="red":
                    ca.setregistered(False)
                if ca not in listt:
                    listt.append(ca)
                    listt.sort()
                if ca not in self.carsinsys:
                    self.carsinsys.append(ca)
                    self.carsinsys.sort()

            c = -1
            for iio in listt:
                c += 1
                item = QListWidgetItem(iio.__str__(), self.listWidget)
                print(lolo[c])
                if lolo[c] == 'green':
                    item.setBackground(QColor('#008000'))
                    self.listWidget.addItem(item)
                    self.loon.append(iio)
                if lolo[c] == 'red':
                    item.setBackground(QColor('#ff0000'))
                    self.listWidget.addItem(item)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.AddCARbtn.clicked.connect(self.Btnclickedadd)
        self.listWidget.itemClicked.connect(self.fullclicked)
        self.deletebtn.clicked.connect(self.delbtnclicked)
        self.modifybtn.clicked.connect(self.modifybtnn)
        self.checkBox.stateChanged.connect(self.boxchecked)
        self.save.clicked.connect(self.saveclicked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate('MainWindow', 'MainWindow'))
        self.label.setText(_translate('MainWindow', 'car parking'))
        self.label_2.setText(_translate('MainWindow', 'select fuel'))
        self.checkBox.setText(_translate('MainWindow', 'sign in to park'))
        self.AddCARbtn.setText(_translate('MainWindow', 'ADD'))
        self.deletebtn.setText(_translate('MainWindow', 'DELETE'))
        self.modifybtn.setText(_translate('MainWindow', 'MODIFY'))
        self.comboBox.setItemText(0, _translate('MainWindow', 'gasoline'))
        self.comboBox.setItemText(1, _translate('MainWindow', 'diesel'))
        self.comboBox.setItemText(2, _translate('MainWindow', 'hybrid'))
        self.label_3.setText(_translate('MainWindow', 'make'))
        self.plateEdt.setText(_translate('MainWindow', 'GTX-567'))
        self.label_4.setText(_translate('MainWindow', 'color'))
        self.label_5.setText(_translate('MainWindow', 'model'))
        self.label_6.setText(_translate('MainWindow', 'plate number'))
        self.save.setText(_translate('MainWindow', 'save'))
        self.label_7.setText(_translate('MainWindow', 'cars in system'))
        self.menusave_as.setTitle(_translate('MainWindow', 'save '))
        self.actionsave.setText(_translate('MainWindow', 'save as'))

    def Btnclickedadd(self):
        make = self.makeEdet.text()
        color = self.colorEdt.text()
        fuel = self.comboBox.currentText()
        model = self.modelEdt.text()
        platenumber = self.plateEdt.text()
        if self.checkBox.isChecked()==True:
            registered=True
        else:
            registered=False
        try:
            if len(make) == 0:
                raise MissingDataException('make')
            else:
                if len(color) == 0:
                    raise MissingDataException('color')
                if len(model) == 0:
                    raise MissingDataException('model')
                if len(platenumber) == 0:
                    raise MissingDataException('platenumber')
                assert re.match('[a-zA-Z]{3,4}-\\w{2,4}', platenumber),"Invalid platenumber"
        except MissingDataException as mse:
            try:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Warning!')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText(mse.__str__())
                msg.exec()
            finally:
                mse = None
                del mse
        except AssertionError as e:
            try:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Warning!')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText(e.__str__())
                msg.exec()
            finally:
                e = None
                del e
        # except PlatenumberException as pne:
        #     try:
        #         msg = QtWidgets.QMessageBox()
        #         msg.setWindowTitle('Warning!')
        #         msg.setIcon(QtWidgets.QMessageBox.Warning)
        #         msg.setText('the plate number format is wronge')
        #         msg.exec()
        #     finally:
        #         pne = None
        #         del pne

        else:
            x = cars(make, fuel, model, color, platenumber)
            if len(self.carsinsys) > 0:
                count = 0
                for i in self.carsinsys:
                    if x.getplatenumber() != i.getplatenumber():
                        count += 1

                if count == len(self.carsinsys):
                    self.carsinsys.append(x)
                    self.carsinsys.sort()
                    self.listWidget.clear()
                    zold = 0
                    for i in self.carsinsys:
                        for j in self.loon:
                            if i.getplatenumber() == j.getplatenumber():
                                zold = 1
                                i.setregistered(True)
                        item = QListWidgetItem(i.__str__(), self.listWidget)
                        if zold == 1:
                            item.setBackground(QColor('#008000'))
                            self.listWidget.addItem(item)
                            zold = 0
                        else:
                            item.setBackground(QColor('#ff0000'))
                            self.listWidget.addItem(item)

                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Warning!')
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setText('This car is already in the system!')
                    msg.exec()
                self.plateEdt.setText('enter the same form as in the box')
                self.colorEdt.clear()
                self.makeEdet.clear()
                self.modelEdt.clear()
            else:
                self.carsinsys.append(x)
                self.carsinsys.sort()
                zold = 0
                for i in self.carsinsys:
                    for j in self.loon:
                        if i.getplatenumber() == j.getplatenumber():
                            zold = 1

                    item = QListWidgetItem(i.__str__(), self.listWidget)
                    if zold == 1:
                        item.setBackground(QColor('#008000'))
                        self.listWidget.addItem(item)
                        zold = 0
                    else:
                        item.setBackground(QColor('#ff0000'))
                        self.listWidget.addItem(item)

                self.colorEdt.clear()
                self.plateEdt.setText('enter the same form as in the box')
                self.modelEdt.clear()
                self.makeEdet.clear()
        if self.checkBox.isChecked() == True:
            self.checkBox.setChecked(False)

    def fullclicked(self, item):
        tmp = item.text()
        tmp = tmp.split('(')
        lol = tmp[1][:-1]
        for i in self.carsinsys:
            if lol == i.getplatenumber():
                self.comboBox.setCurrentText(i.getfuel())
                self.makeEdet.setText(i.getmake())
                self.colorEdt.setText(i.getcolor())
                self.modelEdt.setText(i.getmodel())
                self.plateEdt.setText(i.getplatenumber())
                if i in self.loon:
                    self.checkBox.setChecked(True)
                else:
                    self.checkBox.setChecked(False)    

    def modifybtnn(self):
        for i in self.carsinsys:
            if self.plateEdt.text() == i.getplatenumber():
                i.setmake(self.makeEdet.text())
                i.setcolor(self.colorEdt.text())
                i.setfuel(self.comboBox.currentText())
                i.setmodel(self.modelEdt.text())
                if self.checkBox.isChecked() == True:
                    i.setregistered(True)
                else:
                    i.setregistered(False)

                self.carsinsys.sort()
                self.listWidget.clear()
                zold=0
                for i in self.carsinsys:
                    for j in self.loon:
                        if i.getplatenumber() == j.getplatenumber():
                            zold = 1

                    item = QListWidgetItem(i.__str__(), self.listWidget)
                    if zold == 1 :
                        item.setBackground(QColor('#008000'))
                        self.listWidget.addItem(item)
                        zold = 0
                    else:
                        item.setBackground(QColor('#ff0000'))
                        self.listWidget.addItem(item)

    def delbtnclicked(self):
        make = self.makeEdet.text()
        color = self.colorEdt.text()
        fuel = self.comboBox.currentText()
        model = self.makeEdet.text()
        platenumber = self.plateEdt.text()
        x = cars(make, fuel, model, color, platenumber)
        cou = 0
        for i in self.carsinsys:
            cou += 1
            if x.getplatenumber() == i.getplatenumber():
                cou = 100000
                self.carsinsys.remove(i)
                self.carsinsys.sort()
                self.listWidget.clear()
                zold = 0
                for l in self.carsinsys:
                    for j in self.loon:
                        if l.getplatenumber() == j.getplatenumber():
                            zold = 1

                    item = QListWidgetItem(l.__str__(), self.listWidget)
                    if zold == 1:
                        item.setBackground(QColor('#008000'))
                        self.listWidget.addItem(item)
                        zold = 0
                    else:
                        item.setBackground(QColor('#ff0000'))
                        self.listWidget.addItem(item)

        if cou == len(self.carsinsys):
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Warning!')
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("it can't be deleted it's not in the system")
            msg.exec()

    def boxchecked(self, item):
        if item == Qt.Checked:
            make = self.makeEdet.text()
            color = self.colorEdt.text()
            fuel = self.comboBox.currentText()
            model = self.modelEdt.text()
            platenumber = self.plateEdt.text()
            try:
                if len(make) == 0:
                    raise MissingDataException('make')
                else:
                    if len(color) == 0:
                        raise MissingDataException('color')
                    if len(model) == 0:
                        raise MissingDataException('model')
                    if len(platenumber) == 0:
                        raise MissingDataException('platenumber')
                    assert re.match('[a-zA-Z]{3,4}-\\w{2,4}', platenumber)
            except MissingDataException as mse:
                try:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Warning!')
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setText(mse.__str__())
                    msg.exec()
                finally:
                    mse = None
                    del mse
            except AssertionError as e:
                try:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Warning!')
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setText(e.__str__())
                    msg.exec()
                finally:
                    e = None
                    del e
            except PlatenumberException as pne:
                try:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Warning!')
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setText('the plate number format is wronge')
                    msg.exec()
                finally:
                    pne = None
                    del pne

            else:
                x = cars(make, fuel, model, color, platenumber)
                if x not in self.loon:
                    self.loon.append(x)
                    print(len(self.loon))
        else:
            make = self.makeEdet.text()
            color = self.colorEdt.text()
            fuel = self.comboBox.currentText()
            model = self.modelEdt.text()
            platenumber = self.plateEdt.text()
            try:
                if len(make) == 0:
                    raise MissingDataException('make')
                else:
                    if len(color) == 0:
                        raise MissingDataException('color')
                    if len(model) == 0:
                        raise MissingDataException('model')
                    if len(platenumber) == 0:
                        raise MissingDataException('platenumber')
                    assert re.match('[a-zA-Z]{3,4}-\\w{2,4}', platenumber)
            except MissingDataException as mse:
                try:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Warning!')
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setText(mse.__str__())
                    msg.exec()
                finally:
                    mse = None
                    del mse
            except AssertionError as e:
                try:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Warning!')
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setText(e.__str__())
                    msg.exec()
                finally:
                    e = None
                    del e
            except PlatenumberException as pne:
                try:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Warning!')
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setText('the plate number format is wronge')
                    msg.exec()
                finally:
                    pne = None
                    del pne

            else:
                x = cars(make, fuel, model, color, platenumber)
                if x in self.loon:
                    self.loon.remove(x)
                    print(len(self.loon))

    def saveclicked(self):
        my_file = open('mydata', 'w')
        zold = 0
        for i in self.carsinsys:
            for j in self.loon:
                if i.getplatenumber() == j.getplatenumber():
                    zold = 1

            if zold == 1:
                print(('make: {}   fuel used: {}   model: {}   color: {}  plate number: {}      status: {}'.format(i.getmake(), i.getfuel(), i.getmodel(), i.getcolor(), i.getplatenumber(), 'green')), file=my_file)
                zold = 0
            else:
                print(('make: {}   fuel used: {}   model: {}   color: {}  plate number: {}      status: {}'.format(i.getmake(), i.getfuel(), i.getmodel(), i.getcolor(), i.getplatenumber(), 'red')), file=my_file)

        x = open('mydatafor_reopen', 'w')
        zoldd = 0
        for l in self.carsinsys:
            for m in self.loon:
                if l.getplatenumber() == m.getplatenumber():
                    zoldd = 1

            if zoldd == 1:
                print((l.getmake()), (l.getfuel()), (l.getmodel()), (l.getcolor()), (l.getplatenumber()), 'green', file=x)
                zoldd = 0
            else:
                print((l.getmake()), (l.getfuel()), (l.getmodel()), (l.getcolor()), (l.getplatenumber()), 'red', file=x)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
colors = [
 '#7fc97f', '#beaed4', '#fdc086', '#ffff99', '#386cb0', '#f0027f', '#bf5b17', '#666666']