from PyQt5.QtWidgets import QWidget, QTabWidget, QGridLayout, QVBoxLayout
from tabs.PokemonTab import PokemonTab
from tabs.WonderCardTab import WonderCardTab

class TabWidget(QWidget):
    def __init__(self, window):
        super().__init__()

        #For Saving RawFile
        self._window = window

        self.initUI()

    def initUI(self):
        self.setWindowTitle("WCFullEditor")

        self.PokemonTab = PokemonTab(self._window.wcfile)
        self.WonderCardTab = WonderCardTab(self._window)

        self.tabs = QTabWidget()
        self.tabs.addTab(self.PokemonTab, "포켓몬")
        self.tabs.addTab(self.WonderCardTab, "이상한소포")
        
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.tabs)
        #탭 설정 끝

        self.setLayout(self.vbox)

        self.show()

    def ChangeGen(self):
        self.PokemonTab.ChangeGen(self._window.wcfile.gen)
        self.WonderCardTab.ChangeGen(self._window.wcfile.gen)

    def reset(self):
        self.PokemonTab.Reset()
        self.WonderCardTab.Reset()

    def updateData(self):
        self.PokemonTab.updateData()
        self.WonderCardTab.updateData()

    def saveData(self):
        self.PokemonTab.saveData()