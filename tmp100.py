import smbus

class Temp100:
    def __init__(self):
        self.defaultBus = 1 # 0 for RPiv1, 1 for RPiv2
        self.bus = smbus.SMBus(self.defaultBus)
        self.defaultAddress = 0b1001011 # 0x4b for EveAlpha

        self.tmp100temp   = 0b00
        self.tmp100config = 0b01
        self.tmp100tempL  = 0b10
        self.tmp100tempH  = 0b11

	self.tmp100configres   = 0b10011111
        self.tmp100config9bit  = 0b00000000
        self.tmp100config10bit = 0b00100000
        self.tmp100config11bit = 0b01000000
        self.tmp100config12bit = 0b01100000

	self.tmp100configShutclear = 0b11111110
        self.tmp100configShutdown  = 0b00000001

    def readByteData(self, register):
        return self.bus.read_byte_data(self.defaultAddress, register)

    def readWordData(self, register):
        return self.bus.read_word_data(self.defaultAddress, register)

    def writeByteData(self, register, value):
        self.bus.write_byte_data(self.defaultAddress, register, value)

    def getConfiguration(self):
        return self.readByteData(self.tmp100config)

    def setShutdown(self):
        config = self.getConfiguration()
        config = config | self.tmp100configShutdown
        self.writeByteData(self.tmp100config,config)

    def setShutclear(self):
        config = self.getConfiguration()
        config = config & self.tmp100configShutclear
        self.writeByteData(self.tmp100config,config)

    def setResolution9bit(self):
        config = self.getConfiguration()
	config = config & self.tmp100configres
        config = config | self.tmp100config9bit
        self.writeByteData(self.tmp100config,config)

    def setResolution10bit(self):
        config = self.getConfiguration()
	config = config & self.tmp100configres
        config = config | self.tmp100config10bit
        self.writeByteData(self.tmp100config,config)

    def setResolution11bit(self):
        config = self.getConfiguration()
	config = config & self.tmp100configres
        config = config | self.tmp100config11bit
        self.writeByteData(self.tmp100config,config)

    def setResolution12bit(self):
        config = self.getConfiguration()
	config = config & self.tmp100configres
        config = config | self.tmp100config12bit
        self.writeByteData(self.tmp100config,config)

    def getTemperature(self):
        tempW = self.readWordData(self.tmp100temp)
        #print "word: "+bin(tempW)
        temp = (tempW&0xFF) + ((tempW>>12)/16.0)
        #print "temp: "+str(temp)
        return temp
