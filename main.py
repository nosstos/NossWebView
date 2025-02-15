import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://nosstos.github.io'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        feed_btn = QAction('Feedback', self)
        feed_btn.triggered.connect(self.navigate_feed)
        navbar.addAction(feed_btn)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://nosstos.github.io'))

    def navigate_feed(self):
        self.browser.setUrl(QUrl('https://example.com'))


app = QApplication(sys.argv)
QApplication.setApplicationName('NossWebView')
window = MainWindow()
app.exec_()