import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextBrowser, QListWidget, QFontComboBox
#import time
from PyQt5 import uic
import random
global file_path
file_path = os.path.join(os.getcwd(), [file for file in os.listdir(os.getcwd()) if file.endswith('.txt')][0])
global font_family
font_family = 'Arial'
def adjust_font_size_to_fit(text_browser, text):
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
            font-size: 200px;
        ">
              {text}
        </div>
    ''')

def read_txt():
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    return lines

def textrandom():
    list1 = read_txt()
    text = random.choice(list1)
    return text

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
        # 连接信号与槽
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.listWidget.itemClicked.connect(self.on_link_clicked)

        # 初始化文本
        text = textrandom()
        adjust_font_size_to_fit(self.textBrowser, text)

    def on_pushButton_clicked(self):
        text = textrandom()
        adjust_font_size_to_fit(self.textBrowser, text)

    def on_link_clicked(self, item):
        if item.text() == 'link':
            url='https://www.baidu.com'
            import webbrowser
            webbrowser.open(url)
        if item.text() == 'setting':
            self.setting_window = SettingWindow()
            self.setting_window.show()
            self.window().hide()
        if item.text() == 'file path':

            from PyQt5.QtWidgets import QFileDialog
            global file_path
            file_path = QFileDialog.getOpenFileName(self, '选择文件', os.getcwd(), 'Text files(*.txt)')[0]
            text = textrandom()
            adjust_font_size_to_fit(self.textBrowser, text)
class SettingWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 加载 UI 文件
        uic.loadUi('./setting.ui', self)
        self.listWidget = self.findChild(QListWidget, 'listWidget')
        self.listWidget.itemClicked.connect(self.on_link_clicked)
        self.setWindowTitle('Setting')
        self.fontComboBox = self.findChild(QFontComboBox, 'fontComboBox')
        self.fontComboBox.currentFontChanged.connect(self.update_font)


        # 识别当前字体
    def update_font(self, font):
        global font_family
        font_family = font.family()




    def on_link_clicked(self, item):
        if item.text() == 'main':
            self.mainwindow = MainWindow()
            self.mainwindow.show()
            self.window().hide()
        if item.text() == 'link':
            url='https://www.baidu.com'
            import webbrowser
            webbrowser.open(url)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

