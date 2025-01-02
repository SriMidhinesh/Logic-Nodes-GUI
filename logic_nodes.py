import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QMenu, QToolBar, QAction, QDockWidget, QListWidget, QListWidgetItem
from PyQt5.QtGui import QIcon

import qrc_resources

class Window(QMainWindow):
    
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("Logic Nodes")
        self.resize(800,800)
        self.centralWidget = QLabel("Hello, World")
        self.centralWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.centralWidget)
        self._createActions()
        self._createMenuBar()
        self._sidePanel()
        # self._createToolBars()
        self._createContextMenu()
        
        
    def _createMenuBar(self):
            menuBar = self.menuBar() #method of the QMainWindow
            fileMenu = QMenu("&File", self)
            #Creating menus using a QMenu object
            menuBar.addMenu(fileMenu)
            fileMenu.addAction(self.newAction)
            fileMenu.addAction(self.openAction)
            fileMenu.addAction(self.saveAction)
            #Creating menus using a title
            editMenu = menuBar.addMenu("&Edit")
            editMenu.addAction(self.undoAction)
            editMenu.addAction(self.redoAction)
            editMenu.addSeparator()
            editMenu.addAction(self.cutAction) 
            editMenu.addAction(self.copyAction)
            editMenu.addAction(self.pasteAction)
            editMenu.addAction(self.deleteAction)
            windowMenu = menuBar.addMenu("&Window")
            # nodes =
            
    def _createToolBars(self):
        #Using a title
        fileToolBar = self.addToolBar("File")
        #Using a QToolBar Object
        editToolBar = QToolBar("Edit", self)
        #Using a QToolBar object and a toolbar area
        windowToolBar = QToolBar("Window", self)
        self.addToolBar(Qt.LeftToolBarArea, windowToolBar)
        
    def _createActions(self):
        #Creating action using the first constructor
        self.newAction = QAction(self)
        self.newAction.setText("&New")
        self.newAction.setIcon(QIcon(":file-new.svg"))
        #Creating actions using the second constructor
        self.openAction = QAction(QIcon(":file-open.svg"),"&Open...", self)
        self.saveAction = QAction(QIcon(":file-save.svg"),"&Save", self)
        self.exitAction = QAction("&Exit", self)
        self.undoAction = QAction("&Undo", self)
        self.redoAction = QAction("&Redo", self)
        self.deleteAction = QAction("&Delete", self)
        self.copyAction = QAction(QIcon(":edit-copy.svg"),"&Copy", self)
        self.pasteAction = QAction(QIcon(":edit-paste.svg"),"&Paste", self)
        self.cutAction = QAction(QIcon(":edit-cut.svg"),"&Cut", self)
        self.aboutAction = QAction("&About", self)   
        
    def _createContextMenu(self):
        #Setting contextMenuPolicy
        self.centralWidget.setContextMenuPolicy(Qt.ActionsContextMenu)
        #Populating the widget with actions
        self.centralWidget.addAction(self.newAction)
        self.centralWidget.addAction(self.openAction)
        self.centralWidget.addAction(self.saveAction)
        #Creating a separator action
        separator = QAction(self)
        separator.setSeparator(True)
        #Adding the separator to the menu
        self.centralWidget.addAction(separator)
        self.centralWidget.addAction(self.cutAction)
        self.centralWidget.addAction(self.copyAction)
        self.centralWidget.addAction(self.pasteAction)
        
    def _sidePanel(self):
        self.sidePanel = QDockWidget("Nodes", self)
        self.nodesList = QListWidget()
        node_input = QListWidgetItem(QIcon(":side-input.svg"), "Input")
        self.nodesList.addItem(node_input)
        node_output = QListWidgetItem(QIcon(":side-output.svg"), "Output")
        self.nodesList.addItem(node_output)
        logic_and = QListWidgetItem(QIcon(":side-and.svg"), "And")
        self.nodesList.addItem(logic_and)
        logic_or = QListWidgetItem(QIcon(":side-or.svg"), "Or")
        self.nodesList.addItem(logic_or)
        logic_not = QListWidgetItem(QIcon(":side-not.svg"), "Not")
        self.nodesList.addItem(logic_not)
        logic_nor = QListWidgetItem(QIcon(":side-nor.svg"), "Nor")
        self.nodesList.addItem(logic_nor)
        logic_nand = QListWidgetItem(QIcon(":side-nand.svg"), "Nand")
        self.nodesList.addItem(logic_nand)
        logic_xnor = QListWidgetItem(QIcon(":side-xnor.svg"), "Xnor")
        self.nodesList.addItem(logic_xnor)
        logic_xor = QListWidgetItem(QIcon(":side-xor.svg"), "Xor")
        self.nodesList.addItem(logic_xor)
        self.sidePanel.setWidget(self.nodesList)
        self.sidePanel.setFloating(False)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.sidePanel)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())