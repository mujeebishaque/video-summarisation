from PyQt5 import QtCore, QtGui, QtWidgets
import pathlib

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(613, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(90, 10, 421, 51))
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(12)
        font.setUnderline(True)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(50, 89, 521, 181))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 40, 140, 16))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(160, 30, 91, 31))
        self.comboBox.setCurrentText("")
        self.comboBox.setMaxVisibleItems(200)
        self.comboBox.setObjectName("comboBox")
        self.select_video = QtWidgets.QPushButton(self.groupBox)
        self.select_video.setGeometry(QtCore.QRect(300, 30, 171, 31))
        self.select_video.setObjectName("select_video")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 130, 13))
        self.label_2.setObjectName("label_2")
        self.video_file_path = QtWidgets.QLabel(self.groupBox)
        self.video_file_path.setGeometry(QtCore.QRect(160, 90, 310, 13))
        self.video_file_path.setText("")
        self.video_file_path.setObjectName("video_file_path")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(180, 120, 180, 40))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.select_video.clicked.connect(self.select_video_file)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Videos Anomaly Detection"))
        self.title.setText(_translate("MainWindow", "Anomaly Detection Based Video Summarization "))
        self.groupBox.setTitle(_translate("MainWindow", "Actions Available"))
        self.label.setText(_translate("MainWindow", "Select Object To Detect"))
        self.select_video.setText(_translate("MainWindow", "Select Video File"))
        self.label_2.setText(_translate("MainWindow", "Video File Selected"))
        self.pushButton.setText(_translate("MainWindow", "Summarize Video"))

    def select_video_file(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Video Files(*.mp4 *.avi)")
        URL_OF_VIDEO = str(pathlib.Path(file_path)) # get's the full path with one slash in between
        return URL_OF_VIDEO

    def summarize_video(self):
        pass

    def run_yolo_on_video(self):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
