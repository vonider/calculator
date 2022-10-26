# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'standard_calc.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def __init__(self):
        self.operators = ['+', '-', '*', '/']
        self.digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.decimal_number = False
        self.first_zero = False

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(290, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(290, 300))
        Dialog.setMaximumSize(QtCore.QSize(290, 300))
        Dialog.setWindowTitle("Calculator")
        self.output_screen = QtWidgets.QLineEdit(Dialog)
        self.output_screen.setGeometry(QtCore.QRect(5, 5, 280, 45))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.output_screen.setFont(font)
        self.output_screen.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.output_screen.setReadOnly(False)
        self.output_screen.setObjectName("output_screen")
        self.num_8 = QtWidgets.QPushButton(Dialog, clicked=lambda: self.press_it("8"))
        self.num_8.setGeometry(QtCore.QRect(76, 55, 66, 44))
        self.num_8.setAutoDefault(False)
        self.num_8.setDefault(False)
        self.num_8.setObjectName("num_8")
        self.num_9 = QtWidgets.QPushButton(Dialog, clicked=lambda: self.press_it("9"))
        self.num_9.setGeometry(QtCore.QRect(147, 55, 66, 44))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.num_9.setFont(font)
        self.num_9.setAutoDefault(False)
        self.num_9.setObjectName("num_9")
        self.division = QtWidgets.QPushButton(Dialog, clicked=lambda: self.press_it("/"))
        self.division.setGeometry(QtCore.QRect(218, 55, 66, 44))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.division.setFont(font)
        self.division.setAutoDefault(False)
        self.division.setObjectName("division")
        self.num_6 = QtWidgets.QPushButton(Dialog, clicked=lambda: self.press_it("6"))
        self.num_6.setGeometry(QtCore.QRect(147, 104, 66, 44))
        self.num_6.setAutoDefault(False)
        self.num_6.setObjectName("num_6")
        self.num_5 = QtWidgets.QPushButton(Dialog, clicked=lambda: self.press_it("5"))
        self.num_5.setGeometry(QtCore.QRect(76, 104, 66, 44))
        self.num_5.setAutoDefault(False)
        self.num_5.setObjectName("num_5")
        self.num_4 = QtWidgets.QPushButton(Dialog, clicked=lambda: self.press_it("4"))
        self.num_4.setGeometry(QtCore.QRect(5, 104, 66, 44))
        self.num_4.setAutoDefault(False)
        self.num_4.setObjectName("num_4")
        self.multiplication = QtWidgets.QPushButton(Dialog, clicked=lambda: self.press_it("*"))
        self.multiplication.setGeometry(QtCore.QRect(218, 104, 66, 44))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.multiplication.setFont(font)
        self.multiplication.setAutoDefault(False)
        self.multiplication.setObjectName("multiplication")
        self.num_3 = QtWidgets.QPushButton(Dialog, clicked=lambda: self.press_it("3"))
        self.num_3.setGeometry(QtCore.QRect(147, 153, 66, 44))
        self.num_3.setAutoDefault(False)
        self.num_3.setObjectName("num_3")
        self.num_2 = QtWidgets.QPushButton(Dialog, clicked=lambda: self.press_it("2"))
        self.num_2.setGeometry(QtCore.QRect(76, 153, 66, 44))
        self.num_2.setAutoDefault(False)
        self.num_2.setObjectName("num_2")
        self.num_1 = QtWidgets.QPushButton(Dialog, clicked=lambda: self.press_it("1"))
        self.num_1.setGeometry(QtCore.QRect(5, 153, 66, 44))
        self.num_1.setAutoDefault(False)
        self.num_1.setObjectName("num_1")
        self.minus = QtWidgets.QPushButton(Dialog, clicked=lambda: self.press_it("-"))
        self.minus.setGeometry(QtCore.QRect(218, 153, 66, 44))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.minus.setFont(font)
        self.minus.setAutoDefault(False)
        self.minus.setObjectName("minus")
        self.backspace = QtWidgets.QPushButton(Dialog, clicked=lambda: self.press_it("back"))
        self.backspace.setGeometry(QtCore.QRect(147, 202, 66, 44))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.backspace.setFont(font)
        self.backspace.setAutoDefault(False)
        self.backspace.setObjectName("backspace")
        self.dot = QtWidgets.QPushButton(Dialog, clicked=lambda: self.press_it("."))
        self.dot.setGeometry(QtCore.QRect(76, 202, 66, 44))
        self.dot.setAutoDefault(False)
        self.dot.setObjectName("dot")
        self.num_0 = QtWidgets.QPushButton(Dialog, clicked=lambda: self.press_it("0"))
        self.num_0.setGeometry(QtCore.QRect(5, 202, 66, 44))
        self.num_0.setAutoDefault(False)
        self.num_0.setObjectName("num_0")
        self.plus = QtWidgets.QPushButton(Dialog, clicked=lambda: self.press_it("+"))
        self.plus.setGeometry(QtCore.QRect(218, 202, 66, 44))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plus.setFont(font)
        self.plus.setAutoDefault(False)
        self.plus.setObjectName("plus")
        self.close_parenthesis = QtWidgets.QPushButton(Dialog, clicked=lambda: self.press_it(")"))
        self.close_parenthesis.setGeometry(QtCore.QRect(147, 251, 66, 44))
        font = QtGui.QFont()
        font.setFamily("Arimo")
        self.close_parenthesis.setFont(font)
        self.close_parenthesis.setAutoDefault(False)
        self.close_parenthesis.setObjectName("close_parenthesis")
        self.open_parethesis = QtWidgets.QPushButton(Dialog, clicked=lambda: self.press_it('('))
        self.open_parethesis.setGeometry(QtCore.QRect(76, 251, 66, 44))
        self.open_parethesis.setAutoDefault(False)
        self.open_parethesis.setObjectName("open_parenthesis")
        self.clear_entry = QtWidgets.QPushButton(Dialog, clicked=lambda: self.press_it("C"))
        self.clear_entry.setGeometry(QtCore.QRect(5, 251, 66, 44))
        self.clear_entry.setAutoDefault(False)
        self.clear_entry.setObjectName("clear_entry")
        self.equals = QtWidgets.QPushButton(Dialog, clicked=lambda: self.press_it("="))
        self.equals.setGeometry(QtCore.QRect(218, 251, 66, 44))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.equals.setFont(font)
        self.equals.setAutoDefault(False)
        self.equals.setObjectName("equals")
        self.num_7 = QtWidgets.QPushButton(Dialog, clicked=lambda: self.press_it("7"))
        self.num_7.setGeometry(QtCore.QRect(5, 55, 66, 44))
        self.num_7.setAutoDefault(False)
        self.num_7.setObjectName("num_7")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def press_it(self, pressed):
        string = self.output_screen

        if string.text() == 'Syntax error' or string.text() == 'Error: Division by zero':
            string.setText("")

        if pressed == 'C':
            string.setText("")
            self.decimal_number = False
            self.first_zero = False

        elif pressed in self.digits:
            if len(string.text()) != 0:
                if string.text()[-1] in self.digits and (not self.first_zero or self.decimal_number):
                    string.setText(f"{string.text()}{pressed}")
                elif string.text()[-1] in self.operators:
                    if pressed == '0':
                        self.first_zero = True
                    else:
                        self.first_zero = False
                    string.setText(f"{string.text()}{pressed}")
                elif string.text()[-1] == '.':
                    string.setText(f"{string.text()}{pressed}")
                elif string.text()[-1] == '(':
                    string.setText(f"{string.text()}{pressed}")
            else:
                if pressed == '0':
                    self.first_zero = True
                else:
                    self.first_zero = False
                string.setText(f"{pressed}")

        elif pressed == '.' and not self.decimal_number:
            if len(string.text()) != 0 and string.text()[-1] in self.digits:
                string.setText(f"{string.text()}{pressed}")
                self.decimal_number = True

        elif pressed in self.operators:
            if len(string.text()) == 0 and pressed == '-':
                string.setText(pressed)
            elif len(string.text()) != 0:
                if string.text()[-1] in self.digits:
                    string.setText(f"{string.text()}{pressed}")
                    self.first_zero = False
                    self.decimal_number = False
                elif string.text()[-1] in ['*', '/'] and pressed == '-':
                    string.setText(f"{string.text()}{pressed}")
                elif string.text()[-1] in self.operators and len(string.text()) != 1:
                    string.setText(f"{string.text()[0:-1]}{pressed}")
                elif string.text()[-1] == ')':
                    string.setText(f"{string.text()}{pressed}")

        elif pressed in ['(', ')']:
            if len(string.text()) == 0 and pressed == '(':
                string.setText("(")
            elif string.text()[-1] in self.operators and pressed == '(':
                string.setText(f"{string.text()}{pressed}")
            elif string.text()[-1] == pressed:
                string.setText(f"{string.text()}{pressed}")
            elif string.text()[-1] in self.digits and pressed == ')':
                string.setText(f"{string.text()}{pressed}")


        elif pressed == '=' and len(string.text()) != 0:
            if string.text()[-1] in self.operators:
                result = 'Syntax error'
            elif string.text().count(')') != string.text().count('('):
                result = 'Syntax error'
            else:
                try:
                    result = eval(string.text())
                except ZeroDivisionError:
                    result = 'Error: Division by zero'
            string.setText(str(result))

        elif pressed == 'back' and len(string.text()) != 0:
            if len(string.text()) == 1 and string.text()[-1] == '0':
                self.first_zero = False
                string.setText("")
            elif string.text()[-1] == '0' and string.text()[-2] in self.operators:
                self.first_zero = False
                string.setText(string.text()[0:-1])
            elif string.text()[-1] == '.':
                self.decimal_number = False
                string.setText(string.text()[0:-1])
            else:
                string.setText(string.text()[0:-1])


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.num_8.setText(_translate("Dialog", "8"))
        self.num_9.setText(_translate("Dialog", "9"))
        self.division.setText(_translate("Dialog", "÷"))
        self.num_6.setText(_translate("Dialog", "6"))
        self.num_5.setText(_translate("Dialog", "5"))
        self.num_4.setText(_translate("Dialog", "4"))
        self.multiplication.setText(_translate("Dialog", "×"))
        self.num_3.setText(_translate("Dialog", "3"))
        self.num_2.setText(_translate("Dialog", "2"))
        self.num_1.setText(_translate("Dialog", "1"))
        self.minus.setText(_translate("Dialog", "-"))
        self.backspace.setText(_translate("Dialog", "Del"))
        self.dot.setText(_translate("Dialog", "."))
        self.num_0.setText(_translate("Dialog", "0"))
        self.plus.setText(_translate("Dialog", "+"))
        self.close_parenthesis.setText(_translate("Dialog", ")"))
        self.open_parethesis.setText(_translate("Dialog", "("))
        self.clear_entry.setText(_translate("Dialog", "C"))
        self.equals.setText(_translate("Dialog", "="))
        self.num_7.setText(_translate("Dialog", "7"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
