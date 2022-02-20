from structures.wc import WC

import struct
import os

class WCFull:
    def __init__(self, gen=7):
        self.gen = gen
        self.wc = WC(gen, True)

        self._data = {
            "ReceivedGame": {
                "data": int(),
                "length": 1,
                "type": int,
                "location": 0x0
            },
            "RedemptionText": {
                "data": str(),
                "length": 506,
                "type": str,
                "location": 0x4
            },
            "CardAnimation": {
                "data": int(),
                "length": 1,
                "type": int,
                "location": 0xFE
            },
            "AllowedLanguage": {
                "data": int(),
                "length": 1,
                "type": int,
                "location": 0xFF
            },
            "SubID": {
                "data": int(),
                "length": 1,
                "type": int,
                "location": 0x201
            },
            "Checksum": {
                "data": int(),
                "length": 2,
                "type": int,
                "location": 0x202
            },
        }

    def getData(self, name):
        if self._data.__contains__(name):
            return self._data[name]['data']
        else:
            if self.wc._data.__contains__(name):
                return self.wc._data[name]['data']
            else:
                if self.wc.content._data.__contains__(name):
                    return self.wc.content._data[name]['data']
                
        raise ValueError()

    def setData(self, name, value):
        if self._data.__contains__(name):
            self._data[name]['data'] = value
            return
        else:
            if self.wc._data.__contains__(name):
                self.wc._data[name]['data'] = value
                return
            else:
                if self.wc.content._data.__contains__(name):
                    self.wc.content._data[name]['data'] = value
                    return
                
        raise ValueError()


    def readFromFiles(self, file):
        convertTable = {
            1: 'B',
            2: 'H',
            4: 'I'
        }
        savefile = open(file, "rb")
        for section in self._data:
            currentData = self._data[section]
            savefile.seek(currentData['location'])
            if currentData['type'] is int:
                self._data[section]['data'] = struct.unpack(convertTable[currentData['length']], savefile.read(currentData['length']))[0]
            elif currentData['type'] is str:
                self._data[section]['data'] = savefile.read(currentData['length']).decode('utf-16-le').replace('\x00', '')

        savefile.close()
        self.wc.readFromFiles(file)


    def writeToFiles(self, file):
        pass

if __name__ == '__main__':
    WCFull = WCFull()
    WCFull.readFromFiles("/home/iant/test2.wc7full")
    print(WCFull.getData('ReceivedGame'))
    print(WCFull.getData("RedemptionText"))
    print(WCFull.getData("CardID"))
    print(WCFull.getData("CardTitle"))
    print(WCFull.getData("Species"))