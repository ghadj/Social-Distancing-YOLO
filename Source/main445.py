# Form implementation generated from reading ui file '445_main_b.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject
from matplotlib import pyplot as plt
import sys
import cv2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(892, 755)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("@font-face {\n"
"  font-family: Roboto;\n"
"  src: url(\'https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap\');\n"
"}\n"
"\n"
"QMainWindow {\n"
"    font-family: Roboto;\n"
"}\n"
"\n"
"#sidebar_bg {\n"
"    background-color:#343957;\n"
"}\n"
"\n"
"#centralwidget {\n"
"    background-color: #f8f9fe;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: none;\n"
"    background-color: #343957;\n"
"    color: white;\n"
"    font-size: 12px;\n"
"    padding: 15px 0 15px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #6b51df;\n"
"}\n"
"\n"
"QPushButton > QLabel {\n"
"    color: white;\n"
"}\n"
"\n"
"#sidebar_bg > QLabel {\n"
"    color: white;\n"
"}\n"
"\n"
"#heading_stats {\n"
"    font-size: 22px;\n"
"    color: #3d4465;\n"
"    margin-bottom: 0.5rem;\n"
"    font-weight: 500;\n"
"    line-height: 1.2;\n"
"}\n"
"\n"
"#sidebar_bg > QPushButton {\n"
"    text-align: left;\n"
"    padding-left: 15px;\n"
"}\n"
"\n"
"#label_menu, #label_information {\n"
"    font-size: 16px;\n"
"    padding-top: 10px;\n"
"    padding-left: 15px;\n"
"    color: #627186;\n"
"}\n"
"\n"
"QFrame > QTextBrowser {\n"
"    background-color: #d4dbf9;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"#button_train_browse, #button_weights_browse, #button_images_browse {\n"
"    padding: 5px 0 5px 0;\n"
"}\n"
"\n"
"\n"
"")
        self.gridLayout_4 = QtWidgets.QGridLayout(MainWindow)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.gridLayout_4.addWidget(self.menubar, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.sidebar_bg = QtWidgets.QFrame(MainWindow)
        self.sidebar_bg.setMaximumSize(QtCore.QSize(240, 16777215))
        self.sidebar_bg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sidebar_bg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sidebar_bg.setObjectName("sidebar_bg")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.sidebar_bg)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_menu = QtWidgets.QLabel(self.sidebar_bg)
        self.label_menu.setObjectName("label_menu")
        self.verticalLayout.addWidget(self.label_menu)
        self.button_training = QtWidgets.QPushButton(self.sidebar_bg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_training.sizePolicy().hasHeightForWidth())
        self.button_training.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons/bullseye-solid - white.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_training.setIcon(icon)
        self.button_training.setIconSize(QtCore.QSize(24, 24))
        self.button_training.setObjectName("button_training")
        self.verticalLayout.addWidget(self.button_training)
        self.button_inference = QtWidgets.QPushButton(self.sidebar_bg)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./icons/running-solid - white.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_inference.setIcon(icon1)
        self.button_inference.setIconSize(QtCore.QSize(24, 24))
        self.button_inference.setObjectName("button_inference")
        self.verticalLayout.addWidget(self.button_inference)
        self.label_information = QtWidgets.QLabel(self.sidebar_bg)
        self.label_information.setObjectName("label_information")
        self.verticalLayout.addWidget(self.label_information)
        self.button_about_us = QtWidgets.QPushButton(self.sidebar_bg)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./icons/users-solid - white.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_about_us.setIcon(icon2)
        self.button_about_us.setIconSize(QtCore.QSize(24, 24))
        self.button_about_us.setObjectName("button_about_us")
        self.verticalLayout.addWidget(self.button_about_us)
        self.button_technical_information = QtWidgets.QPushButton(self.sidebar_bg)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./icons/cogs-solid - white.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_technical_information.setIcon(icon3)
        self.button_technical_information.setIconSize(QtCore.QSize(24, 24))
        self.button_technical_information.setObjectName("button_technical_information")
        self.verticalLayout.addWidget(self.button_technical_information)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.sidebar_bg)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.sidebar_bg)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.gridLayout.addWidget(self.sidebar_bg, 1, 0, 1, 1)
        self.app_container = QtWidgets.QFrame(MainWindow)
        self.app_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.app_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.app_container.setObjectName("app_container")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.app_container)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.heading_stats = QtWidgets.QLabel(self.app_container)
        self.heading_stats.setEnabled(True)
        self.heading_stats.setWhatsThis("")
        self.heading_stats.setObjectName("heading_stats")
        self.verticalLayout_2.addWidget(self.heading_stats)
        self.frame_training = QtWidgets.QFrame(self.app_container)
        self.frame_training.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_training.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_training.setObjectName("frame_training")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_training)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.frame_training)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.text_dataset = QtWidgets.QLineEdit(self.frame_training)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_dataset.sizePolicy().hasHeightForWidth())
        self.text_dataset.setSizePolicy(sizePolicy)
        self.text_dataset.setObjectName("text_dataset")
        self.horizontalLayout.addWidget(self.text_dataset)
        self.button_train_browse = QtWidgets.QPushButton(self.frame_training)
        self.button_train_browse.setObjectName("button_train_browse")
        self.horizontalLayout.addWidget(self.button_train_browse)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.button_train_submit = QtWidgets.QPushButton(self.frame_training)
        self.button_train_submit.setObjectName("button_train_submit")
        self.verticalLayout_3.addWidget(self.button_train_submit)
        self.gridLayout_6.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_training)
        self.frame = QtWidgets.QFrame(self.app_container)
        self.frame.setEnabled(True)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.text_weights = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_weights.sizePolicy().hasHeightForWidth())
        self.text_weights.setSizePolicy(sizePolicy)
        self.text_weights.setObjectName("text_weights")
        self.horizontalLayout_2.addWidget(self.text_weights)
        self.button_weights_browse = QtWidgets.QPushButton(self.frame)
        self.button_weights_browse.setObjectName("button_weights_browse")
        self.horizontalLayout_2.addWidget(self.button_weights_browse)
        self.gridLayout_7.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.text_images = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_images.sizePolicy().hasHeightForWidth())
        self.text_images.setSizePolicy(sizePolicy)
        self.text_images.setObjectName("text_images")
        self.horizontalLayout_3.addWidget(self.text_images)
        self.button_images_browse = QtWidgets.QPushButton(self.frame)
        self.button_images_browse.setObjectName("button_images_browse")
        self.horizontalLayout_3.addWidget(self.button_images_browse)
        self.gridLayout_7.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_7.addWidget(self.pushButton, 2, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_about = QtWidgets.QFrame(self.app_container)
        self.frame_about.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_about.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_about.setObjectName("frame_about")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_about)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_about)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setStyleSheet("")
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_3.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_about)
        self.frame_technical = QtWidgets.QFrame(self.app_container)
        self.frame_technical.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_technical.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_technical.setObjectName("frame_technical")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_technical)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.frame_technical)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_3.sizePolicy().hasHeightForWidth())
        self.textBrowser_3.setSizePolicy(sizePolicy)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.gridLayout_5.addWidget(self.textBrowser_3, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_technical)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.gridLayout.addWidget(self.app_container, 1, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setGeometry(QtCore.QRect(0, 0, 3, 18))
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(MainWindow)
        self.button_about_us.clicked.connect(self.frame_about.show)
        self.button_technical_information.clicked.connect(self.frame_about.hide)
        self.button_about_us.clicked.connect(self.frame_technical.hide)
        self.button_technical_information.clicked.connect(self.frame_technical.show)
        self.button_inference.clicked.connect(self.frame_about.hide)
        self.button_training.clicked.connect(self.frame_about.hide)
        self.button_training.clicked.connect(self.frame_technical.hide)
        self.button_inference.clicked.connect(self.frame_technical.hide)
        self.button_training.clicked.connect(self.frame_training.show)
        self.button_inference.clicked.connect(self.frame_training.hide)
        self.button_about_us.clicked.connect(self.frame_training.hide)
        self.button_technical_information.clicked.connect(self.frame_training.hide)
        self.button_training.clicked.connect(self.frame.hide)
        self.button_inference.clicked.connect(self.frame.show)
        self.button_about_us.clicked.connect(self.frame.hide)
        self.button_technical_information.clicked.connect(self.frame.hide)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Hide all frames except first one
        self.frame_about.hide()
        self.frame_technical.hide()
        self.frame.hide()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_menu.setText(_translate("MainWindow", "MENU"))
        self.button_training.setText(_translate("MainWindow", "  Training"))
        self.button_inference.setText(_translate("MainWindow", "  Inference"))
        self.label_information.setText(_translate("MainWindow", "INFORMATION"))
        self.button_about_us.setText(_translate("MainWindow", "  About"))
        self.button_technical_information.setText(_translate("MainWindow", "  Technical information"))
        self.label.setText(_translate("MainWindow", "Last Update: 28/11/2020"))
        self.label_2.setText(_translate("MainWindow", "Version: Beta 0.9"))
        self.heading_stats.setAccessibleName(_translate("MainWindow", "h1"))
        self.heading_stats.setText(_translate("MainWindow", "COVID-19 Distance calculator"))
        self.label_3.setText(_translate("MainWindow", "Dataset directory: "))
        self.button_train_browse.setText(_translate("MainWindow", "Browse"))
        self.button_train_submit.setText(_translate("MainWindow", "Train"))
        self.label_4.setText(_translate("MainWindow", "Load weights:"))
        self.button_weights_browse.setText(_translate("MainWindow", "Browse"))
        self.label_5.setText(_translate("MainWindow", "Images:"))
        self.button_images_browse.setText(_translate("MainWindow", "Browse"))
        self.pushButton.setText(_translate("MainWindow", "Run Demo"))
        self.frame_about.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\">Some bullshit about this project and the purpose of this course</p></body></html>"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><a name=\"output\"></a><span style=\" font-size:8pt;\">S</span><span style=\" font-size:8pt;\">ome technical bullshit about YOLO and QT</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    ui= Ui_MainWindow()
    ui.setupUi(window)

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
