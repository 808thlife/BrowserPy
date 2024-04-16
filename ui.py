from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

import sys
import os

DEFAULT_SEARCH_ENGINE = "google.com"

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)

        #setting appropriate size for browser window.     
        self.setFixedWidth(1200)
        self.setFixedHeight(700)

        #starting page.
        self.tabs = QTabWidget()

        # making document mode true
        self.tabs.setDocumentMode(True)
 
        # making tabs closeable
        self.tabs.setTabsClosable(True)

        self.setCentralWidget(self.tabs)
        
        self.setWindowTitle("BrowserPy")

        #toolbar on the top. 
        toolbar = QToolBar("Toolbar")
        self.addToolBar(toolbar)

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        #refresh page
        button_action = QAction(QIcon(os.path.join("assets", "img","refresh.png")),"Refresh", self) # added a button
        button_action.setStatusTip("Refreshing current page")
        #connect to a function
        button_action.triggered.connect(lambda: self.tabs.currentWidget().reload())
        toolbar.addAction(button_action)

        #binding a key to refresh a page
        self.shortcut = QShortcut(QKeySequence("Ctrl+R"), self)
        self.shortcut.activated.connect(lambda: self.tabs.currentWidget().reload())
        toolbar.addSeparator()

        #adding urlbar
        self.urlbar = QLineEdit()
 
        # adding action to line edit when return key is pressed
        self.urlbar.returnPressed.connect(self.navigate_to_url)
 
        # adding line edit to tool bar
        toolbar.addWidget(self.urlbar)

        #adding first tab 
        self.add_new_tab()

        self.setStatusBar(QStatusBar(self))
        

        self.show()
        
    def refresh_page(self):
        browser = QWebEngine
        browser.reload()
    
    def navigate_to_url(self):
 
        # get the line edit text
        # convert it to QUrl object
        q = QUrl(self.urlbar.text())
 
        # if scheme is blank
        if q.scheme() == "":
            # set scheme
            q.setScheme("http")
 
        # set the url
        self.tabs.currentWidget().setUrl(q)

    def add_new_tab(self, qurl=None, label="New Tab"):
        if qurl is None:
            qurl = QUrl(DEFAULT_SEARCH_ENGINE)

        browser = QWebEngineView()

        i = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(i)

        browser.load(qurl)
        



app = QApplication(sys.argv)
window = MainWindow()

app.exec_()