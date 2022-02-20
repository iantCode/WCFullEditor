from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QButtonGroup, QGridLayout, QLabel, QLineEdit, QMessageBox, QRadioButton, QTextEdit, QCheckBox, QDateEdit, QGroupBox, QHBoxLayout, QWidget
from PyQt5.QtGui import QIntValidator
from constants.pokemon import *
# from contents.pokemontab import PokemonLayout

class WonderCardTab(QWidget):
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.wcfile = self.window.wcfile
        self.layout = QGridLayout()
        self.setLayout(self.layout)

#CARDTYPE
        genGB = QGroupBox('세대')
        self.gen = QButtonGroup()
        genGBlayout = QHBoxLayout()
        genGB.setLayout(genGBlayout)
        gen1 = QRadioButton('6세대')
        self.gen.addButton(gen1, 6)
        gen2 = QRadioButton('7세대')
        gen2.setChecked(True)
        self.gen.addButton(gen2, 7)
        genGBlayout.addWidget(gen1)
        genGBlayout.addWidget(gen2)
        self.layout.addWidget(genGB, 0, 0, 1, 5)

#CARDTYPE
        cardTypeGB = QGroupBox('카드 종류')
        self.cardType = QButtonGroup()
        cardTypeGBlayout = QHBoxLayout()
        cardTypeGB.setLayout(cardTypeGBlayout)
        cardType1 = QRadioButton('포켓몬')
        cardType1.setChecked(True)
        self.cardType.addButton(cardType1, 0)
        cardType2 = QRadioButton('아이템')
        self.cardType.addButton(cardType2, 1)
        cardType3 = QRadioButton('BP')
        self.cardType.addButton(cardType3, 3)
        cardTypeGBlayout.addWidget(cardType1)
        cardTypeGBlayout.addWidget(cardType2)
        cardTypeGBlayout.addWidget(cardType3)
        self.layout.addWidget(cardTypeGB, 1, 0, 1, 5)

#RECEIVEDGAME
        gameGB = QGroupBox('받을 수 있는 게임')
        gameGBlayout = QHBoxLayout()
        gameGB.setLayout(gameGBlayout)
        self.game = [None, None, None, None]
        temp = 0
        for i in ['S', 'M', 'US', "UM"]:
            self.game[temp] = QCheckBox(i)
            gameGBlayout.addWidget(self.game[temp])
            temp += 1
        self.layout.addWidget(gameGB, 2, 0, 1, 5)


#CARDID
        self.layout.addWidget(QLabel('카드 ID'), 3, 0)
        self.cardID = QLineEdit()
        self.cardID.setMaxLength(4)
        self.cardID.setValidator(QIntValidator())
        self.cardID.setText('0')
        self.layout.addWidget(self.cardID, 3, 1)

#CARDREDEMPTIONDATE
        self.layout.addWidget(QLabel('카드 수령일'), 3, 2)
        self.cardDate = QDateEdit()
        self.cardDate.setDate(QDate.currentDate())
        self.cardDate.setMinimumDate(QDate(2010, 1, 1))
        self.cardDate.setMaximumDate(QDate(2029, 12, 31))
        self.layout.addWidget(self.cardDate, 3, 3, 1, 2)

#CARDNAME
        self.layout.addWidget(QLabel('카드 이름'), 4, 0)
        self.cardName = QLineEdit()
        self.cardName.setMaxLength(37)
        self.layout.addWidget(self.cardName, 4, 1)

#REDEMPTIONTEXT
        self.redemptionText = QTextEdit()
        self.redemptionText.setAcceptRichText(False)
        self.redemptionText.setPlaceholderText("Redemption Text")
        self.layout.addWidget(self.redemptionText, 5, 0, 2, 5)


#Check Events Here
        self.gen.buttonClicked.connect(self.genChanged)
        self.cardType.buttonClicked.connect(self.CardTypeChanged)
        self.redemptionText.textChanged.connect(self.redemptionTextChanged) #for checking text max length


    def genChanged(self):
        reply = QMessageBox.question(self, '경고!', '세대를 바꾸려면 새 파일을 만들어야 합니다.\n새 파일을 만들겠습니까?', QMessageBox.Yes | QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.wcfile.gen = self.gen.checkedId()
            self.window.lastFile = './'
            self.window.setWindowTitle("WCFullEditor - *.wc{}full".format(self.gen.checkedId()))
            self.window.tabwidget.ChangeGen(self.wcfile.gen)


    def redemptionTextChanged(self):
        if len(self.redemptionText.toPlainText()) > 253:
            self.redemptionText.setPlainText(self.redemptionText.toPlainText()[0:252])


    def CardTypeChanged(self):
        self.mother.HideOther(self.cardType.checkedId())


    def ChangeGen(self, gen):
        self.Reset()
        if gen == 6:
            self.game1.setText('Y')
            self.game2.setText('X')
            self.game3.setText('AS')
            self.game4.setText('OR')
        if gen == 7:
            self.game1.setText('S')
            self.game2.setText('M')
            self.game3.setText('US')
            self.game4.setText('UM')


    def updateData(self):
        for i in range(0, 3):
            self.cardType.buttons()[i].setDisabled(False)
        for i in range(4):
            if (self.wcfile.getData('ReceivedGame') >> i) & 0x1 == 0x1:
                self.game[i].setChecked(True)
                continue
            self.game[i].setChecked(False)

        self.cardID.setText(str(self.wcfile.getData('CardID')))

        year, tempDate = divmod(self.wcfile.getData("CardRedemptionDate"), 10000)
        month, day = divmod(tempDate, 100)
        tempQDate = QDate()
        if self.wcfile.gen == 6:
            tempQDate.setDate(year, month, day)
        else:
            tempQDate.setDate(year + 2000, month, day)
        self.cardDate.setDate(tempQDate)

        self.cardName.setText(self.wcfile.getData('CardTitle'))
        self.redemptionText.setPlainText(self.wcfile.getData('RedemptionText'))


    def Reset(self):
        for i in range(0, 3):
            self.cardType.buttons()[i].setDisabled(False)
        for i in range(4):
            self.game[i].setChecked(False)
        self.cardID.setText('')
        self.cardDate.setDate(QDate.currentDate())
        self.cardName.setText('')
        self.redemptionText.setPlainText('')