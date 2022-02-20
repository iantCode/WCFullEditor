from PyQt5.QtWidgets import QButtonGroup, QHBoxLayout, QLabel, QLineEdit, QComboBox, QGroupBox, QGridLayout, QRadioButton, QWidget
from PyQt5.QtGui import QIntValidator
from constants.pokemon import *
from packages.ExtendedComboBox import ExtendedComboBox
# from contents.pokemontab import PokemonLayout

class PokemonTab(QWidget):
    def __init__(self, wcfile):
        super().__init__()
        self.wcfile = wcfile
        self.layout = QGridLayout()
        self.setLayout(self.layout)

#POKEMON
        self.layout.addWidget(QLabel('포켓몬: '), 0, 0)
        self.pokemon = ExtendedComboBox()
        for i in range(1, MAX_P7 + 1):
            self.pokemon.addItem(POKEMON_NAME[i])
        self.layout.addWidget(self.pokemon, 0, 1)

#LEVEL
        self.layout.addWidget(QLabel('레벨'), 1, 0)
        self.level = QLineEdit()
        self.level.setValidator(QIntValidator())
        self.level.setText('1')
        self.layout.addWidget(self.level, 1, 1)

#FORM
        self.layout.addWidget(QLabel('폼체인지: '), 2, 0)
        self.form = QComboBox()
        self.CheckForm()
        self.layout.addWidget(self.form, 2, 1)

#ITEM
        self.layout.addWidget(QLabel('아이템: '), 3, 0)
        self.item = ExtendedComboBox()
        for i in range(0, MAX_I7):
            self.item.addItem(ITEM_NAME[i])
        self.layout.addWidget(self.item, 3, 1)

#BALL
        self.layout.addWidget(QLabel('볼: '), 4, 0)
        self.ball = ExtendedComboBox()
        for i in range(1, MAX_B7 + 1):
            self.ball.addItem(BALL_NAME[i])
        self.layout.addWidget(self.ball, 4, 1)

#NATURE
        self.layout.addWidget(QLabel('성격: '), 5, 0)
        self.nature = QComboBox()
        self.nature.addItem('랜덤')
        for i in range(0, len(NATURE_NAME)):
            self.nature.addItem(NATURE_NAME[i])
        self.layout.addWidget(self.nature, 5, 1)

#ABILITY
        self.layout.addWidget(QLabel('특성'), 6, 0)
        self.ability = QComboBox()
        self.ability.addItem("1번 특성")
        self.ability.addItem("2번 특성")
        self.ability.addItem("숨겨진 특성")
        self.ability.addItem("랜덤 특성 (숨겨진 특성 제외)")
        self.ability.addItem("랜덤 특성")
        self.layout.addWidget(self.ability, 6, 1)

#LANGUAGE
        self.layout.addWidget(QLabel('언어: '), 7, 0)
        self.language = QComboBox()
        for i in ["수령자 언어", "일본어", "영어", "프랑스어", "독일어", "스페인어", "이탈리아어", "한국어", "중국어-간체", "중국어-번체"]:
            self.language.addItem(i)
        self.layout.addWidget(self.language, 7, 1)

#MOVES
        moveGB = QGroupBox('기술')
        moveGBlayout = QGridLayout()
        moveGB.setLayout(moveGBlayout)
        self.move = [ExtendedComboBox() for i in range(4)]
        for i in range(0, MAX_M7):
            for j in range(4):
                self.move[j].addItem(MOVE_NAME[i])

        for i in range(4):
            moveGBlayout.addWidget(self.move[i])
        self.layout.addWidget(moveGB, 0, 2, 4, 1)

#RELEARNMOVE
        re_moveGB = QGroupBox('다시 배울 수 있는 기술')
        re_moveGBlayout = QGridLayout()
        re_moveGB.setLayout(re_moveGBlayout)
        self.re_move = [ExtendedComboBox() for i in range(4)]
        for i in range(0, MAX_M7):
            for j in range(4):
                self.re_move[j].addItem(MOVE_NAME[i])

        for i in range(4):
            re_moveGBlayout.addWidget(self.re_move[i])
        self.layout.addWidget(re_moveGB, 0, 3, 4, 1)

        trainerGB = QGroupBox('트레이너 설정')
        trainerGBLayout = QGridLayout()
        trainerGB.setLayout(trainerGBLayout)

#TRAINERNAME
        trainerGBLayout.addWidget(QLabel('이름'), 0, 0)
        self.trainer = QLineEdit()
        self.trainer.setMaxLength(13)
        trainerGBLayout.addWidget(self.trainer, 0, 1)

#TRAINERGENDER
        trainerGenderGB = QGroupBox('성별')
        self.trainerGenderRG = QButtonGroup()
        trainerGenderGBlayout = QHBoxLayout()
        trainerGenderGB.setLayout(trainerGenderGBlayout)
        trainerMale = QRadioButton('남성')
        trainerMale.setChecked(True)
        self.trainerGenderRG.addButton(trainerMale, 0)
        trainerFemale = QRadioButton('여성')
        self.trainerGenderRG.addButton(trainerFemale, 1)
        trainerOther = QRadioButton('수령자의 성별')
        self.trainerGenderRG.addButton(trainerOther, 3)
        trainerGenderGBlayout.addWidget(trainerMale)
        trainerGenderGBlayout.addWidget(trainerFemale)
        trainerGenderGBlayout.addWidget(trainerOther)
        trainerGBLayout.addWidget(trainerGenderGB, 1, 0, 1, 2)

#TID
        trainerGBLayout.addWidget(QLabel('TID: '), 0, 2)
        self.TID = QLineEdit()
        self.TID.setValidator(QIntValidator())
        self.TID.setText('0')
        trainerGBLayout.addWidget(self.TID, 0, 3)

#SID
        trainerGBLayout.addWidget(QLabel('SID: '), 1, 2)
        self.SID = QLineEdit()
        self.SID.setValidator(QIntValidator(0, 4294, trainerGBLayout))
        self.SID.setText('0')
        trainerGBLayout.addWidget(self.SID, 1, 3)

#Add Trainer Group Box Here
        self.layout.addWidget(trainerGB, 6, 2, 3, 2)


#Check Events Here
        self.pokemon.currentIndexChanged.connect(self.pokemonChanged) # for checking existing Form
        self.level.textChanged.connect(self.levelChanged) # for checking Level limit
        self.TID.textChanged.connect(self.TIDChanged) # for checking TID limit
        self.SID.textChanged.connect(self.SIDChanged) # for checking SID limit


    def pokemonChanged(self):
        '''
            For checking Form
        '''
        self.CheckForm()

    def levelChanged(self):
        '''
            For changing level to meet requirement(level 1~100)
        '''
        try:
            level = int(self.level.text())
            if level < 1:
                self.level.setText('1')
            elif level > 100:
                self.level.setText('100')
        except:
            level = 1
            self.level.setText('1')
            self.level.selectAll()


    def TIDChanged(self):
        '''
            For changing level to meet requirement(vary by gen)
        '''
        try:
            TID = int(self.TID.text())
        except:#if text() == ''
            TID = 0
            self.TID.setText('0')
            self.TID.selectAll()

        if self.wcfile.gen == 6 and TID > 65535:
            self.TID.setText('65535')
        
        if self.wcfile.gen == 7 and TID > 967295 and int(self.SID.text()) == 4294:
            self.TID.setText('967295')

    def SIDChanged(self):
        '''
            For changing level to meet requirement(vary by gen)
        '''
        try:
            SID = int(self.SID.text())
        except: #if text() == ''
            SID = 0
            self.SID.setText('0')
            self.SID.selectAll()
        if self.wcfile.gen == 6 and SID > 65535:
            self.SID.setText('65535')
        if self.wcfile.gen == 7 and SID > 4294:
            self.SID.setText('4294')
            if int(self.TID.text()) > 967295:
                self.TID.setText('967295')

    def ChangeGen(self, gen):
        self.Reset()
#POKEMON
        self.pokemon.clear()
        if gen == 6:
            for i in range(1, MAX_P6 + 1):
                self.pokemon.addItem(POKEMON_NAME[i])
        elif gen == 7:
            for i in range(1, MAX_P7 + 1):
                self.pokemon.addItem(POKEMON_NAME[i])

#ITEM
        self.item.clear()
        if gen == 6:
            for i in range(0, MAX_I6):
                self.item.addItem(ITEM_NAME[i])
        elif gen == 7:
            for i in range(0, MAX_I7):
                self.item.addItem(ITEM_NAME[i])

#BALL
        self.ball.clear()
        if gen == 6:
            for i in range(1, MAX_B6 + 1):
                self.ball.addItem(BALL_NAME[i])
        elif gen == 7:
            for i in range(1, MAX_B7 + 1):
                self.ball.addItem(BALL_NAME[i])

#MOVE
        for i in range(1, 4):
            self.move[i].clear()
            self.re_move[i].clear()

        if gen == 6:
            for i in range(0, MAX_M6):
                for j in range(4):
                    self.move[j].addItem(MOVE_NAME[i])
                    self.re_move[j].addItem(MOVE_NAME[i])
        elif gen == 7:
            for i in range(0, MAX_M7):
                for j in range(4):
                    self.move[j].addItem(MOVE_NAME[i])
                    self.re_move[j].addItem(MOVE_NAME[i])

    def updateData(self):
        self.ChangeGen(self.wcfile.gen)
        self.pokemon.setCurrentIndex(self.wcfile.getData("Species") - 1)
        self.level.setText(str(self.wcfile.getData("Level")))
        self.form.setCurrentIndex(self.wcfile.getData("Form"))
        self.item.setCurrentIndex(self.wcfile.getData("HeldItem"))
        self.ball.setCurrentIndex(self.wcfile.getData("CaughtBall") - 1)
        self.ability.setCurrentIndex(0)
        self.nature.setCurrentIndex(0)
        for i in range(4):
            self.move[i].setCurrentIndex(0)
            self.re_move[i].setCurrentIndex(0)
        self.trainer.setText('')
        self.TID.setText(str(self.wcfile.getData("TIDSID")[0]))
        self.SID.setText(str(self.wcfile.getData("TIDSID")[1]))

    
    def saveData(self):
        self.wcfile.setData("Species", self.pokemon.currentIndex() + 1)
        self.wcfile.setData("Level", int(self.level.text()))
        self.wcfile.setData("Form", self.form.currentIndex())
        self.wcfile.setData("HeldItem", self.item.currentIndex())
        self.wcfile.setData("CaughtBall", self.ball.currentIndex() + 1)
        # Ability, nature, move to be edited.
        self.wcfile.setData("TIDSID", [int(self.TID.text()), int(self.SID.text())])

        print(self.wcfile.getData("Species"))


    def Reset(self):
        self.pokemon.setCurrentIndex(0)
        self.level.setText('1')
        self.form.setCurrentIndex(0)
        self.item.setCurrentIndex(0)
        self.ball.setCurrentIndex(0)
        self.ability.setCurrentIndex(0)
        self.nature.setCurrentIndex(0)
        for i in range(4):
            self.move[i].setCurrentIndex(0)
            self.re_move[i].setCurrentIndex(0)
        self.trainer.setText('')
        self.TID.setText('0')
        self.SID.setText('0')
        return


    def CheckForm(self):
        '''
            get lists of possible form lists
        '''
        self.form.clear()
        self.form.setEnabled(True)

        if self.pokemon.currentText() == '캐스퐁':
            self.form.addItem('노말')
            self.form.addItem(FORM_NAME[889])
            self.form.addItem(FORM_NAME[890])
            self.form.addItem(FORM_NAME[891])
            return
        if self.pokemon.currentText() == '가이오가':
            self.form.addItem('노말')
            self.form.addItem(FORM_NAME[899])
            return
        if self.pokemon.currentText() == '그란돈':
            self.form.addItem('노말')
            self.form.addItem(FORM_NAME[899])
            return
        if self.pokemon.currentText() == '테오키스':
            self.form.addItem('노말')
            self.form.addItem(FORM_NAME[902])
            self.form.addItem(FORM_NAME[903])
            self.form.addItem(FORM_NAME[904])
            return
        if self.pokemon.currentText() == '도롱충이' or self.pokemon.currentText() == '도롱마담' or self.pokemon.currentText() == '나메일':
            self.form.addItem(FORM_NAME[412])
            self.form.addItem(FORM_NAME[902])
            self.form.addItem(FORM_NAME[903])
            return
        if self.pokemon.currentText() == '체리꼬':
            self.form.addItem(FORM_NAME[421])
            self.form.addItem(FORM_NAME[909])
            return
        if self.pokemon.currentText() == '깝질무' or self.pokemon.currentText() == '트리토돈':
            self.form.addItem(FORM_NAME[422])
            self.form.addItem(FORM_NAME[911])
            return
        if self.pokemon.currentText() == '로토무':
            self.form.addItem('노말')
            self.form.addItem(FORM_NAME[917])
            self.form.addItem(FORM_NAME[918])
            self.form.addItem(FORM_NAME[919])
            self.form.addItem(FORM_NAME[920])
            self.form.addItem(FORM_NAME[921])
            return
        if self.pokemon.currentText() == '기라티나':
            self.form.addItem(FORM_NAME[487])
            self.form.addItem(FORM_NAME[922])
            return
        if self.pokemon.currentText() == '쉐이미':
            self.form.addItem(FORM_NAME[492])
            self.form.addItem(FORM_NAME[923])
            return
        if self.pokemon.currentText() == '아르세우스':
            for i in ["노말", "격투", "비행", "독", "땅", "바위", "벌레", "고스트", "강철", "불꽃", "물", "풀", "전기", "에스퍼", "얼음", "드래곤", "악", "페어리"]:
                self.form.addItem(i)
            return
        if self.pokemon.currentText() == '배쓰나이':
            self.form.addItem(FORM_NAME[550])
            self.form.addItem(FORM_NAME[942])
            return
        if self.pokemon.currentText() == '불비달마':
            self.form.addItem(FORM_NAME[555])
            self.form.addItem(FORM_NAME[943])
            return
        if self.pokemon.currentText() == '사철록' or self.pokemon.currentText() == '바라철록':
            self.form.addItem(FORM_NAME[585])
            self.form.addItem(FORM_NAME[947])
            self.form.addItem(FORM_NAME[948])
            self.form.addItem(FORM_NAME[949])
            return
        if self.pokemon.currentText() == '토네로스' or self.pokemon.currentText() == '볼트로스' or self.pokemon.currentText() == '랜드로스':
            self.form.addItem(FORM_NAME[641])
            self.form.addItem(FORM_NAME[952])
            return
        if self.pokemon.currentText() == '큐레무':
            self.form.addItem(pokemon.currentText())
            self.form.addItem(FORM_NAME[953])
            self.form.addItem(FORM_NAME[954])
            return
        if self.pokemon.currentText() == '케르디오':
            self.form.addItem(FORM_NAME[647])
            self.form.addItem(FORM_NAME[955])
            return
        if self.pokemon.currentText() == '메로엣타':
            self.form.addItem(FORM_NAME[648])
            self.form.addItem(FORM_NAME[956])
            return
        if self.pokemon.currentText() == '게노세크트':
            self.form.addItem('노말')
            self.form.addItem('물')
            self.form.addItem('전기')
            self.form.addItem('불')
            self.form.addItem('얼음')
            return
        if self.pokemon.currentText() == '개굴닌자':
            self.form.addItem('노말')
            self.form.addItem(FORM_NAME[962])
            self.form.addItem(FORM_NAME[1012])
            return
        if self.pokemon.currentText() == '비비용':
            self.form.addItem(FORM_NAME[666])
            for i in range(963, 982):
                self.form.addItem(FORM_NAME[i])
            return
        if self.pokemon.currentText() in ['플라베베', '플로제스']:
            self.form.addItem(FORM_NAME[669])
            for i in range(986, 990):
                self.form.addItem(FORM_NAME[i])
            return
        if self.pokemon.currentText() == '플라엣테':
            self.form.addItem(FORM_NAME[669])
            for i in range(986, 991):
                self.form.addItem(FORM_NAME[i])
            return
        if self.pokemon.currentText() == '트리미앙':
            self.form.addItem(FORM_NAME[676])
            for i in range(995, 1004):
                self.form.addItem(FORM_NAME[i])
            return
        if self.pokemon.currentText() == '냐오닉스':
            self.form.addItem("수컷")
            self.form.addItem("암컷")
            return
        if self.pokemon.currentText() == '킬가르도':
            self.form.addItem(FORM_NAME[681])
            self.form.addItem(FORM_NAME[1005])
            return
        if self.pokemon.currentText() in ['호바귀', '펌킨인']:
            self.form.addItem(FORM_NAME[710])
            for i in range(1006, 1009):
                self.form.addItem(FORM_NAME[i])
            return
        if self.pokemon.currentText() == '제르네아스':
            self.form.addItem(FORM_NAME[716])
            self.form.addItem(FORM_NAME[1012])
            return
        if self.pokemon.currentText() == '후파':
            self.form.addItem(FORM_NAME[720])
            self.form.addItem(FORM_NAME[1018])
            return
        if self.pokemon.currentText() == '지가르데':
            self.form.addItem(FORM_NAME[718])
            for i in range(1013, 1017):
                self.form.addItem(FORM_NAME[i])
            return
        if self.wcfile.gen == 6:
            if self.pokemon.currentText() == '피카츄':
                self.form.addItem('노말')
                for i in range(729, 735):
                    self.form.addItem(FORM_NAME[i])
                return
        if self.wcfile.gen == 7:
            if self.pokemon.currentText() == '피카츄':
                self.form.addItem('노말')
                for i in range(813, 819):
                    self.form.addItem(FORM_NAME[i])
                self.form.addItem(FORM_NAME[1063])
                return
            if self.pokemon.currentText() in ['꼬렛', '레트라', '라이츄', '모래두지', '고지', '식스테일', '나인테일', '디그다', '닥트리오', '나옹', '페르시온', '꼬마돌', '데구리', '딱구리', '질퍽이', '질뻐기', '나시', '텅구리']:
                self.form.addItem('노말')
                self.form.addItem(FORM_NAME[810])
                return
            if self.pokemon.currentText() == '춤추새':
                self.form.addItem(FORM_NAME[741])
                for i in range(1021, 1024):
                    self.form.addItem(FORM_NAME[i])
                self.form.addItem(FORM_NAME[1063])
                return
            if self.pokemon.currentText() == '암멍이':
                self.form.addItem('노말')
                self.form.addItem(FORM_NAME[1064])
                return
            if self.pokemon.currentText() == '루가루암':
                self.form.addItem('노말')
                self.form.addItem(FORM_NAME[1024])
                self.form.addItem(FORM_NAME[1064])
                return
            if self.pokemon.currentText() == '약어리':
                self.form.addItem(FORM_NAME[746])
                self.form.addItem(FORM_NAME[1025])
                return
            if self.pokemon.currentText() == '실버디':
                for i in ["노말", "격투", "비행", "독", "땅", "바위", "벌레", "고스트", "강철", "불꽃", "물", "풀", "전기", "에스퍼", "얼음", "드래곤", "악", "페어리"]:
                    self.form.addItem(i)
                return
            if self.pokemon.currentText() == '메테노':
                self.form.addItem(FORM_NAME[774])
                for i in range(1045, 1058):
                    self.form.addItem(FORM_NAME[i])
                return
            if self.pokemon.currentText() == '따라큐':
                self.form.addItem(FORM_NAME[778])
                self.form.addItem(FORM_NAME[1058])
                return
            if self.pokemon.currentText() == '네크로즈마':
                self.form.addItem('노말')
                self.form.addItem(FORM_NAME[1065])
                self.form.addItem(FORM_NAME[1066])
                self.form.addItem(FORM_NAME[1067])
                return
            if self.pokemon.currentText() == '마기아나':
                self.form.addItem('노말')
                self.form.addItem(FORM_NAME[1062])
                return


        self.form.addItem(self.pokemon.currentText())
        self.form.setEnabled(False)
        return