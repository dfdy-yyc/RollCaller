import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextBrowser, QListWidget, QFontComboBox, QSpinBox
from PyQt5.QtCore import Qt,QTimer
import os
from PyQt5 import uic
import random
file_path = os.path.join(os.getcwd(), [file for file in os.listdir(os.getcwd()) if file.endswith('.txt')][0])
font_family = 'Arial'
font_size = 200


def read_txt():
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    return lines


def textrandom(text_browser):
    list1 = read_txt()
    text = random.choice(list1)
    cursor = text_browser.textCursor()
    # 清空文本框
    text_browser.clear()
    # 使用 HTML 和 CSS 设置上下左右居中

    cursor.insertHtml(f'''
        <div style="
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: {font_family};
            text-align: center;
            margin: 0;
            padding: 0;
            font-size: {font_size}px;
        ">
              {text}
        </div>
    ''')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 加载 UI 文件
        uic.loadUi('./main1017.ui', self)
        self.setWindowTitle('RollCaller')
        # 获取控件
        self.mainwindow = self.findChild(QMainWindow, 'RollCaller')
        self.pushButton = self.findChild(QPushButton, 'pushButton')
        self.textBrowser = self.findChild(QTextBrowser, 'textBrowser')
        self.listWidget= self.findChild(QListWidget, 'listWidget')
        self.setAttribute(Qt.WA_TranslucentBackground)
        self._margin = 20  # 设置缩放区域的边距
        # 连接信号与槽
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.listWidget.itemClicked.connect(self.on_link_clicked)

        # 初始化文本
        textrandom(self.textBrowser)


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._drag_start = event.globalPos() - self.pos()

    def mouseMoveEvent(self, event):
        self.setCursor(Qt.ArrowCursor)
        self.move(event.globalPos() - self._drag_start)

    def on_pushButton_clicked(self):
        if self.pushButton.text() == '开始':
            self.timer = QTimer()
            self.timer.timeout.connect(self.pushButton_update)
            self.timer.start(15)
            self.pushButton.setText('停止')
        elif self.pushButton.text() == '停止':
            self.timer.stop()
            self.pushButton.setText('开始')

    def pushButton_update(self):
        textrandom(self.textBrowser)


    def on_link_clicked(self, item):
        if item.text() == 'link':
            url='https://github.com/dfdy-yyc/RollCaller'
            import webbrowser
            webbrowser.open(url)
        if item.text() == 'setting':
            self.setting_window = SettingWindow()
            self.setting_window.show()
            self.window().hide()
        if item.text() == 'file path':
            from PyQt5.QtWidgets import QFileDialog
            global file_path
            file_path = QFileDialog.getOpenFileName(self, '选择文件', os.getcwd(), 'Text files(*.txt)')[0] or file_path
            textrandom(self.textBrowser)


class SettingWindow(QMainWindow):
    _margin = 20
    def __init__(self):
        super().__init__()
        # 加载 UI 文件
        uic.loadUi('./setting.ui', self)
        self.listWidget = self.findChild(QListWidget, 'listWidget')
        self.listWidget.itemClicked.connect(self.on_link_clicked)
        self.setWindowTitle('Setting')
        self.fontComboBox = self.findChild(QFontComboBox, 'fontComboBox')
        self.fontComboBox.currentFontChanged.connect(self.update_font)
        self.SpinBox = self.findChild(QSpinBox, 'spinBox')
        self.SpinBox.valueChanged.connect(self.update_font_size)
        





        # 识别当前字体
    def update_font(self, font):
        global font_family
        font_family = font.family()

    def mousePressEvent(self, event):
        self._drag_start = event.globalPos() - self.pos()

    def mouseMoveEvent(self, event):
        self.setCursor(Qt.ArrowCursor)
        self.move(event.globalPos() - self._drag_start)



    def update_font_size(self, size):
        global font_size
        font_size = size




    def on_link_clicked(self, item):
        if item.text() == 'main':
            self.mainwindow = MainWindow()
            self.mainwindow.show()
            self.window().hide()
        if item.text() == 'link':
            url='https://github.com/dfdy-yyc/RollCaller'
            import webbrowser
            webbrowser.open(url)
        if item.text() == 'file path':
            import os
            from PyQt5.QtWidgets import QFileDialog
            global file_path
            file_path = QFileDialog.getOpenFileName(self, '选择文件', os.getcwd(), 'Text files(*.txt)')[0] or file_path







if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

