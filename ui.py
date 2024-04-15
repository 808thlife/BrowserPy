from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

import sys
import os

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)

        #setting appropriate size for browser window.     
        self.setFixedWidth(1200)
        self.setFixedHeight(700)

        #starting page.
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))
        
        self.setCentralWidget(self.browser)
        
        self.setWindowTitle("BrowserPy")

        #toolbar on the top. 
        toolbar = QToolBar("Toolbar")
        self.addToolBar(toolbar)

        #refresh page
        button_action = QAction(QIcon(os.path.join("assets", "img","refresh.png")),"Refresh", self) # added a button
        button_action.setStatusTip("Refreshing current page")
        #connect to function
        button_action.triggered.connect(self.refresh_page)
        toolbar.addAction(button_action)

        #binding a key to refresh a page
        self.shortcut = QShortcut(QKeySequence("Ctrl+R"), self)
        self.shortcut.activated.connect(self.refresh_page)

        self.setStatusBar(QStatusBar(self))

        self.show()
        
    def refresh_page(self):
        self.browser.reload()



app = QApplication(sys.argv)
window = MainWindow()

app.exec_()