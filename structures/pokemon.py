# from structures.wc import WC
# from move import Move

import struct

class WCPokemon:
    def __init__(self, gen=7, ifWCFull=False):
        self.gen = gen
        self._offset = 0x270

        self._data = {
            "TIDSID": {
                "data": [int(), int()],
                "length": 4,
                "type": "ID",
                "location": 0x0
            },
            "OriginGame": {
                "data": int(),
                "length": 1,
                "type": int,
                "location": 0x4,
            },
            "EC": {
                "data": int(),
                "length": 4,
                "type": int,
                "location": 0x8
            },
            "Ribbons": {
                "data": int(),
                "length": 2,
                "type": int,
                "location": 0xB
            },
            "CaughtBall": {
                "data": int(),
                "length": 2,
                "type": int,
                "location": 0xE
            },
            "HeldItem": {
                "data": int(),
                "length": 2,
                "type": int,
                "location": 0x10
            },
            "Move": {
                # "data": Move(),
                "data": None,
                "length": 8,
                "type": "Move",
                "location": 0x12
            },
            "Species": {
                "data": int(),
                "length": 2,
                "type": int,
                "location": 0x1A
            },
            "Form": {
                "data": int(),
                "length": 1,
                "type": int,
                "location": 0x1C
            },
            "Language": {
                "data": int(),
                "length": 1,
                "type": int,
                "location": 0x1D
            },
            "Nickname": {
                "data": str(),
                "length": 26,
                "type": str,
                "location": 0x1E
            },
            "Level": {
                "data": int(),
                "length": 1,
                "type": int,
                "location": 0x68
            },
        }

    def getData(self, name):
        if self._data.__contains__(name):
            return self._data[name]['data']


    def setData(self, name, value):
        if self._data.__contains__(name):
            self._data[name]['data'] = value
        else:
            raise ValueError()


    def readFromFiles(self, file):
        convertTable = {
            1: 'B',
            2: 'H',
            4: 'I'
        }
        self.savefile = open(file, "rb")
        for section in self._data:
            currentData = self._data[section]
            self.savefile.seek(currentData['location'] + self._offset)
            if currentData['type'] is int:
                self._data[section]['data'] = struct.unpack(convertTable[currentData['length']], self.savefile.read(currentData['length']))[0]
            elif currentData['type'] is str:
                self._data[section]['data'] = self.savefile.read(currentData['length']).decode('utf-16-le').replace('\x00', '')
            elif currentData['type'] == "ID":
                self.SaveTIDSID()
            elif currentData["type"] == "Move":
                pass

        self.savefile.close()
            

    def writeToFiles(self, file):
        pass


    def SaveTIDSID(self):
        self.savefile.seek(0x270)
        rawTID = struct.unpack('H', self.savefile.read(0x2))[0]
        rawSID = struct.unpack('H', self.savefile.read(0x2))[0]

        if self.gen == 6:
            self._data["TIDSID"]['data'] = [rawTID, rawSID]
            return
        temp = (rawSID << 16) + rawTID
        self._data["TIDSID"]['data'] = [temp % 1000000, int(temp / 1000000)]