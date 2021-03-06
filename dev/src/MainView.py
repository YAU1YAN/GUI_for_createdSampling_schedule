# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/Main.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 800))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.timeRangeInput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.timeRangeInput.setGeometry(QtCore.QRect(30, 180, 221, 25))
        self.timeRangeInput.setMinimumSize(QtCore.QSize(221, 25))
        self.timeRangeInput.setMaximumSize(QtCore.QSize(221, 25))
        self.timeRangeInput.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.timeRangeInput.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.timeRangeInput.setObjectName("timeRangeInput")
        self.timeRangeLbl = QtWidgets.QLabel(self.centralwidget)
        self.timeRangeLbl.setGeometry(QtCore.QRect(30, 160, 331, 16))
        self.timeRangeLbl.setObjectName("timeRangeLbl")
        self.decayInput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.decayInput.setGeometry(QtCore.QRect(30, 240, 221, 25))
        self.decayInput.setMinimumSize(QtCore.QSize(221, 25))
        self.decayInput.setMaximumSize(QtCore.QSize(221, 25))
        self.decayInput.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.decayInput.setObjectName("decayInput")
        self.decayLbl = QtWidgets.QLabel(self.centralwidget)
        self.decayLbl.setGeometry(QtCore.QRect(30, 220, 401, 16))
        self.decayLbl.setObjectName("decayLbl")
        self.runSimulationBtn = QtWidgets.QPushButton(self.centralwidget)
        self.runSimulationBtn.setGeometry(QtCore.QRect(90, 510, 101, 26))
        self.runSimulationBtn.setToolTip("")
        self.runSimulationBtn.setObjectName("runSimulationBtn")
        self.samplingLbl = QtWidgets.QLabel(self.centralwidget)
        self.samplingLbl.setGeometry(QtCore.QRect(30, 280, 401, 16))
        self.samplingLbl.setObjectName("samplingLbl")
        self.samplingInput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.samplingInput.setGeometry(QtCore.QRect(30, 300, 221, 25))
        self.samplingInput.setMinimumSize(QtCore.QSize(221, 25))
        self.samplingInput.setMaximumSize(QtCore.QSize(221, 25))
        self.samplingInput.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.samplingInput.setObjectName("samplingInput")
        self.loadingSpinnerLbl = QtWidgets.QLabel(self.centralwidget)
        self.loadingSpinnerLbl.setGeometry(QtCore.QRect(0, 0, 1191, 751))
        self.loadingSpinnerLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.loadingSpinnerLbl.setObjectName("loadingSpinnerLbl")
        self.loadingLbl = QtWidgets.QLabel(self.centralwidget)
        self.loadingLbl.setGeometry(QtCore.QRect(0, 20, 1191, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.loadingLbl.setFont(font)
        self.loadingLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.loadingLbl.setObjectName("loadingLbl")
        self.saveOutputBtn = QtWidgets.QPushButton(self.centralwidget)
        self.saveOutputBtn.setGeometry(QtCore.QRect(170, 710, 85, 26))
        self.saveOutputBtn.setObjectName("saveOutputBtn")
        self.graphWidget = QtWidgets.QWidget(self.centralwidget)
        self.graphWidget.setGeometry(QtCore.QRect(300, 20, 881, 691))
        self.graphWidget.setObjectName("graphWidget")
        self.expDecayEvalLbl = QtWidgets.QLabel(self.centralwidget)
        self.expDecayEvalLbl.setGeometry(QtCore.QRect(30, 340, 221, 111))
        self.expDecayEvalLbl.setWordWrap(True)
        self.expDecayEvalLbl.setObjectName("expDecayEvalLbl")
        self.expDecayEvalInput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.expDecayEvalInput.setGeometry(QtCore.QRect(30, 460, 221, 25))
        self.expDecayEvalInput.setMinimumSize(QtCore.QSize(221, 25))
        self.expDecayEvalInput.setMaximumSize(QtCore.QSize(221, 25))
        self.expDecayEvalInput.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.expDecayEvalInput.setPlainText("")
        self.expDecayEvalInput.setObjectName("expDecayEvalInput")
        self.printOptionsGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.printOptionsGroup.setGeometry(QtCore.QRect(10, 550, 151, 151))
        self.printOptionsGroup.setTitle("")
        self.printOptionsGroup.setObjectName("printOptionsGroup")
        self.printMethodRawBtn = QtWidgets.QRadioButton(self.printOptionsGroup)
        self.printMethodRawBtn.setGeometry(QtCore.QRect(20, 50, 95, 21))
        self.printMethodRawBtn.setChecked(True)
        self.printMethodRawBtn.setObjectName("printMethodRawBtn")
        self.printMethodSingleBtn = QtWidgets.QRadioButton(self.printOptionsGroup)
        self.printMethodSingleBtn.setGeometry(QtCore.QRect(20, 80, 95, 21))
        self.printMethodSingleBtn.setObjectName("printMethodSingleBtn")
        self.printMethodMultiBtn = QtWidgets.QRadioButton(self.printOptionsGroup)
        self.printMethodMultiBtn.setGeometry(QtCore.QRect(20, 110, 95, 21))
        self.printMethodMultiBtn.setObjectName("printMethodMultiBtn")
        self.startFromGroupLbl_2 = QtWidgets.QLabel(self.printOptionsGroup)
        self.startFromGroupLbl_2.setGeometry(QtCore.QRect(20, 30, 91, 16))
        self.startFromGroupLbl_2.setObjectName("startFromGroupLbl_2")
        self.startFromGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.startFromGroup.setGeometry(QtCore.QRect(170, 550, 121, 151))
        self.startFromGroup.setTitle("")
        self.startFromGroup.setObjectName("startFromGroup")
        self.startFromGroupLbl = QtWidgets.QLabel(self.startFromGroup)
        self.startFromGroupLbl.setGeometry(QtCore.QRect(10, 30, 91, 16))
        self.startFromGroupLbl.setObjectName("startFromGroupLbl")
        self.startFrom0 = QtWidgets.QRadioButton(self.startFromGroup)
        self.startFrom0.setGeometry(QtCore.QRect(10, 60, 95, 21))
        self.startFrom0.setChecked(True)
        self.startFrom0.setObjectName("startFrom0")
        self.startFrom1 = QtWidgets.QRadioButton(self.startFromGroup)
        self.startFrom1.setGeometry(QtCore.QRect(10, 100, 95, 21))
        self.startFrom1.setObjectName("startFrom1")
        self.normalisationBox = QtWidgets.QGroupBox(self.centralwidget)
        self.normalisationBox.setGeometry(QtCore.QRect(30, 30, 231, 111))
        self.normalisationBox.setTitle("")
        self.normalisationBox.setObjectName("normalisationBox")
        self.normalisationLbl = QtWidgets.QLabel(self.normalisationBox)
        self.normalisationLbl.setGeometry(QtCore.QRect(20, 20, 251, 21))
        self.normalisationLbl.setObjectName("normalisationLbl")
        self.normalisationMethodNone = QtWidgets.QRadioButton(self.normalisationBox)
        self.normalisationMethodNone.setGeometry(QtCore.QRect(20, 40, 95, 21))
        self.normalisationMethodNone.setChecked(True)
        self.normalisationMethodNone.setObjectName("normalisationMethodNone")
        self.normalisationMethod_1 = QtWidgets.QRadioButton(self.normalisationBox)
        self.normalisationMethod_1.setGeometry(QtCore.QRect(20, 60, 95, 21))
        self.normalisationMethod_1.setObjectName("normalisationMethod_1")
        self.normalisationMethod_2 = QtWidgets.QRadioButton(self.normalisationBox)
        self.normalisationMethod_2.setGeometry(QtCore.QRect(20, 80, 95, 21))
        self.normalisationMethod_2.setObjectName("normalisationMethod_2")
        self.vclistSizeLbl = QtWidgets.QLabel(self.centralwidget)
        self.vclistSizeLbl.setGeometry(QtCore.QRect(350, 720, 81, 16))
        self.vclistSizeLbl.setObjectName("vclistSizeLbl")
        self.vclistSizeValueLbl = QtWidgets.QLabel(self.centralwidget)
        self.vclistSizeValueLbl.setGeometry(QtCore.QRect(440, 720, 81, 16))
        self.vclistSizeValueLbl.setText("")
        self.vclistSizeValueLbl.setObjectName("vclistSizeValueLbl")
        self.timeVolumeLbl = QtWidgets.QLabel(self.centralwidget)
        self.timeVolumeLbl.setGeometry(QtCore.QRect(610, 720, 91, 16))
        self.timeVolumeLbl.setObjectName("timeVolumeLbl")
        self.timeVolumeValueLbl = QtWidgets.QLabel(self.centralwidget)
        self.timeVolumeValueLbl.setGeometry(QtCore.QRect(720, 720, 111, 16))
        self.timeVolumeValueLbl.setText("")
        self.timeVolumeValueLbl.setObjectName("timeVolumeValueLbl")
        self.dimensionsLbl = QtWidgets.QLabel(self.centralwidget)
        self.dimensionsLbl.setGeometry(QtCore.QRect(300, 20, 881, 691))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.dimensionsLbl.setFont(font)
        self.dimensionsLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.dimensionsLbl.setObjectName("dimensionsLbl")
        self.loadingLbl.raise_()
        self.loadingSpinnerLbl.raise_()
        self.timeRangeLbl.raise_()
        self.decayLbl.raise_()
        self.samplingLbl.raise_()
        self.decayInput.raise_()
        self.timeRangeInput.raise_()
        self.graphWidget.raise_()
        self.runSimulationBtn.raise_()
        self.saveOutputBtn.raise_()
        self.expDecayEvalLbl.raise_()
        self.samplingInput.raise_()
        self.expDecayEvalInput.raise_()
        self.printOptionsGroup.raise_()
        self.startFromGroup.raise_()
        self.normalisationBox.raise_()
        self.vclistSizeLbl.raise_()
        self.vclistSizeValueLbl.raise_()
        self.timeVolumeLbl.raise_()
        self.timeVolumeValueLbl.raise_()
        self.dimensionsLbl.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Graph Application"))
        self.timeRangeInput.setPlainText(_translate("MainWindow", "100,100"))
        self.timeRangeLbl.setText(_translate("MainWindow", "Time Range (Comma Seperated Integers)"))
        self.decayInput.setPlainText(_translate("MainWindow", "-3,-3"))
        self.decayLbl.setText(_translate("MainWindow", "Decay (Comma Seperated Integers)"))
        self.runSimulationBtn.setText(_translate("MainWindow", "Run"))
        self.samplingLbl.setText(_translate("MainWindow", "Sampling Portion (single Integer)"))
        self.samplingInput.setPlainText(_translate("MainWindow", "1"))
        self.loadingSpinnerLbl.setText(_translate("MainWindow", "Loading..."))
        self.loadingLbl.setText(_translate("MainWindow", "Running Simulation, this may take a while"))
        self.saveOutputBtn.setText(_translate("MainWindow", "Save Output"))
        self.expDecayEvalLbl.setText(_translate("MainWindow", "Custom exponential decay function.  You can insert a single line funtion here, using the inputs t (time) and b (something), numpy is include so you can use any function available in that package.  If this field is empty it will use the default (exp(float(b) * float(t)))"))
        self.printMethodRawBtn.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.printMethodRawBtn.setText(_translate("MainWindow", "Raw Output"))
        self.printMethodSingleBtn.setText(_translate("MainWindow", "Single Line"))
        self.printMethodMultiBtn.setText(_translate("MainWindow", "Multi Line"))
        self.startFromGroupLbl_2.setText(_translate("MainWindow", "Save Format"))
        self.startFromGroupLbl.setText(_translate("MainWindow", "Start from"))
        self.startFrom0.setText(_translate("MainWindow", "0"))
        self.startFrom1.setText(_translate("MainWindow", "1"))
        self.normalisationLbl.setText(_translate("MainWindow", "Select Normalisation Method"))
        self.normalisationMethodNone.setText(_translate("MainWindow", "None"))
        self.normalisationMethod_1.setText(_translate("MainWindow", "Method 1"))
        self.normalisationMethod_2.setText(_translate("MainWindow", "Method 2"))
        self.vclistSizeLbl.setText(_translate("MainWindow", "Size of VCList:"))
        self.timeVolumeLbl.setText(_translate("MainWindow", "Points Demanded:"))
        self.dimensionsLbl.setText(_translate("MainWindow", "Too many dimensions to create graph"))

