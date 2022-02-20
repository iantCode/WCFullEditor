# from structures.wc import WC
from structures.pokemon import WCPokemon

import struct

class WC:
    def __init__(self, gen=7, ifWCFull=False):
        self.gen = gen
        self._offset = 0x0

        if ifWCFull:
            self._offset = 0x208

        self.content = WCPokemon(gen)

        self._data = {
            "CardID": {
                "data": int(),
                "length": 2,
                "type": int,
                "location": 0x0
            },
            "CardTitle": {
                "data": str(),
                "length": 74,
                "type": str,
                "location": 0x2
            },
            "CardRedemptionDate": {
                "data": int(),
                "length": 4,
                "type": int,
                "location": 0x4C
            },
            "CardLocation": {
                "data": int(),
                "length": 1,
                "type": int,
                "location": 0x50
            },
            "CardType": {
                "data": int(),
                "length": 1,
                "type": int,
                "location": 0x51
            },
            "Statuses": {
                "data": int(),
                "length": 1,
                "type": int,
                "location": 0x52
            },
            "BackgroundColor": {
                "data": int(),
                "length": 1,
                "type": int,
                "location": 0x53
            }
        }

    def getData(self, name):
        if self._data.__contains__(name):
            return self._data[name]['data']

    def readFromFiles(self, file):
        convertTable = {
            1: 'B',
            2: 'H',
            4: 'I'
        }
        savefile = open(file, "rb")
        for section in self._data:
            currentData = self._data[section]
            savefile.seek(currentData['location'] + self._offset)
            if currentData['type'] is int:
                self._data[section]['data'] = struct.unpack(convertTable[currentData['length']], savefile.read(currentData['length']))[0]
            elif currentData['type'] is str:
                self._data[section]['data'] = savefile.read(currentData['length']).decode('utf-16-le').replace('\x00', '')

        savefile.close()

        self.content.readFromFiles(file)
            

    def writeToFiles(self, file):
        pass