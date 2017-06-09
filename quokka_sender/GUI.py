import sys
import PyQt5.QtWidgets as q
import PyQt5.QtGui as qtgui


class Example(q.QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        def btn1pressed(self):
            self.paths_from = q.QFileDialog.getOpenFileNames(self, 'Open file', '/home')

        def btn2pressed(self):
            self.paths_from = q.QFileDialog.getExistingDirectory(self, 'Open directory', '/home')

        def send_data(self):
            pass

        self.resize(400, 200)
        self.center()

        label_ip = q.QLabel('IP адрес брокера: ', self)
        label_ip.move(10, 20)

        input_ip = q.QLineEdit(self)
        input_ip.move(110, 18)

        label_choose_to = q.QLabel('Директория с изображениями: ', self)
        label_choose_to.move(10, 50)

        input_to = q.QLineEdit(self)
        input_to.move(170, 48)

        btn_choose_to = q.QPushButton('Выбор', self)
        btn_choose_to.setToolTip('Выбрать директорию с изображениями')
        btn_choose_to.resize(btn_choose_to.sizeHint())
        btn_choose_to.move(310, 48)

        label_choose_to = q.QLabel('Директория для результатов: ', self)
        label_choose_to.move(10, 80)

        input_out = q.QLineEdit(self)
        input_out.move(170, 78)

        btn_choose_out = q.QPushButton('Выбор', self)
        btn_choose_out.setToolTip('Выбрать директорию')
        btn_choose_out.resize(btn_choose_out.sizeHint())
        btn_choose_out.move(310, 78)

        btn = q.QPushButton('Send', self)
        btn.setToolTip('Send images to queue')
        btn.resize(btn.sizeHint())
        btn.move(160, 150)

        btn_choose_to.click.connect(btn1pressed)
        btn_choose_out.click.connect(btn2pressed)
        btn.click.connect(send_data)

        self.setWindowTitle('Send')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = q.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def showDialog(self):
        self.files = q.QFileDialog.getOpenFileNames(self, 'Open file', '/home')[0]


if __name__ == '__main__':
    app = q.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
