import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QMainWindow, QFileDialog
from pytube import YouTube


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'YouTube Downloader'
        self.left = 10
        self.top = 10
        self.width = 500
        self.height = 140
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.textbox = QLineEdit(self)
        font = self.textbox.font()
        font.setPointSize(14)
        self.textbox.setFont(font)
        self.textbox.move(20, 20)
        self.textbox.resize(340, 40)

        self.button = QPushButton('Download', self)
        self.button.move(130, 80)

        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        url = self.textbox.text()
        youtube = YouTube(url)
        video = youtube.streams.get_highest_resolution()
        file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.textbox.setText("Done")
        video.download(file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    ex = App()
    sys.exit(app.exec_())
