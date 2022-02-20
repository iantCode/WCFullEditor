from PyQt5.QtWidgets import QMainWindow, QAction, QFileDialog, QMessageBox, QApplication
import sys
import os

from tab import TabWidget
from ui.Menubar import MainMenuBar
from structures.wcfull import WCFull

class WCFullEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WCFullEditor - *.wc7full")
        self._lastFile = './'
        self.wcfile = WCFull()
        
        self.MainWindow()


    def MainWindow(self):
        MainMenuBar(self)

        #For enabling Drag&Drop WC*Files.
        self.setAcceptDrops(True)

        self.tabwidget = TabWidget(self)
        self.setCentralWidget(self.tabwidget)

        self.show()
        self.setFixedSize(self.size())


    def closeEvent(self, event):
        '''
            For checking whether the user want to quit the program.
        '''
        reply = QMessageBox.question(self, '확인', "wcfullEditor를 끄시겠습니까?", QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def openFile(self, filename):
        #if file is not wc* file or wc*full file
        if len(filename[0]) == 0:
            return

        if filename[0][-3:] not in ["wc6", "wc7"] and filename[0][-7:] not in ["wc6full", "wc7full"]:
            return QMessageBox.about(self,'파일 에러!','적절한 배포 파일이 아닙니다!')

        #if file is exists
        if os.path.exists(filename[0]):
            gen = 0

            #if file is wc6full or wc7full
            if filename[0][-7:] in ["wc6full", "wc7full"]:
                #check size
                if os.stat(filename[0]).st_size != 784:
                    return QMessageBox.about(self,'파일 에러!','784바이트의 파일이어야 하지만 {}바이트의 파일을 불러왔습니다.'.format(os.stat(filename[0]).st_size))
                gen = int(filename[0][-5:-4])
                self.wcfile.gen = gen
                self.wcfile.readFromFiles(filename[0])
            
            #if file is wc6 or wc7
            if filename[0][-3:] in ["wc6", "wc7"]:
                #check size
                if os.stat(filename[0]).st_size != 264:
                    return QMessageBox.about(self,'파일 에러!','264바이트의 파일이어야 하지만 {}바이트의 파일을 불러왔습니다.'.format(os.stat(filename[0]).st_size))
                gen = int(filename[0][-1:])

            self.tabwidget.updateData()

    def saveFile(self, filename):
        self.tabwidget.saveData()
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WCFullEditor()
    sys.exit(app.exec_())