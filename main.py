import os
import stat
import re
from sys import argv
from sys import exit
import send2trash
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
from PyQt5 import QtCore, QtWidgets
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("文件删除工具")
        Form.resize(383, 182)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 381, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser, 0, QtCore.Qt.AlignVCenter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu Mono derivative Powerline\',\'Consolas\',\'Courier New\',\'monospace\'; font-size:16pt; color:#0a3069;\">是否采取递归删除？</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; background-color:#ffffff;\"><span style=\" font-family:\'Ubuntu Mono derivative Powerline\',\'Consolas\',\'Courier New\',\'monospace\'; font-size:16pt; color:#0a3069;\">注：递归删除的意思是，将文件子目录的文件也会一并删除</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; background-color:#ffffff;\"><span style=\" font-family:\'Ubuntu Mono derivative Powerline\',\'Consolas\',\'Courier New\',\'monospace\'; font-size:16pt; color:#0a3069;\">请谨慎使用！！！</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "是"))
        self.pushButton_2.setText(_translate("Form", "否"))

def delete_file(folder_path):
    pattern = re.compile(r'.*\(\d\).*')
    filelist=os.listdir(folder_path)
    matchfilelist=[]
    #找出匹配的文件名
    for file in filelist:
        if re.match(pattern,file):
            matchfilelist.append(folder_path+"/"+file)
    #权限检查，移除只读属性
    for file in matchfilelist:
        try:
            os.chmod(file, stat.S_IWRITE)
            send2trash.send2trash(os.path.normpath(file))#将匹配的文件放入回收站
            print(f"成功删除了文件: {file}")
        except Exception as e:
            print(f"删除文件时出现错误: {file}，错误信息: {e}")

def recursive_delete_file(directory):
    for root, dirs, files in os.walk(directory):
        delete_file(root)
class delete_tool_widget(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("文件删除工具")
        self.setupUi(self)
        self.pushButton.clicked.connect(self.yes_event)
        self.pushButton_2.clicked.connect(self.no_event)
    def yes_event(self):
        directory = QFileDialog.getExistingDirectory(None,"选择目录",".",QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        recursive_delete_file(directory)
        exit(app.exec_())
    def no_event(self):
        directory = QFileDialog.getExistingDirectory(None,"选择目录",".",QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        delete_file(directory)
        exit(app.exec_())
   
if __name__=='__main__':
    app=QApplication(argv)
    window=delete_tool_widget()
    window.show()
    exit(app.exec_())
    input()
    
