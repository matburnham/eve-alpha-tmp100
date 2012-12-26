import unittest
import tmp100
import smbus

address = 0b1001000 #address 0x48

class TestTmp(unittest.TestCase):
    def test_smbus(self):
        tmp = tmp100.Temp100()
        self.assertIsInstance(tmp, tmp100.Temp100)
        self.assertTrue(tmp.defaultBus == 0)
        self.assertIsInstance(tmp.bus, smbus.SMBus)

    def test_address(self):
        tmp = tmp100.Temp100()
        tmp.defaultAddress = address
        self.assertTrue(tmp.defaultAddress == address)

    def test_getConfig(self):
        tmp = tmp100.Temp100()
        print "config: " + bin(tmp.getConfiguration())

    def test_getTemp(self):
        tmp = tmp100.Temp100()
        print "temp: "+str(tmp.getTemperature())

    def test_set12bit(self):
        tmp = tmp100.Temp100()
        tmp.setResolution12bit()

    def test_set9bit(self):
        tmp = tmp100.Temp100()
        tmp.setResolution9bit()

    def test_setsleep(self):
        tmp = tmp100.Temp100()
        tmp.setShutdown()

    def test_setwake(self):
        tmp = tmp100.Temp100()
        tmp.setShutclear()

if __name__ == '__main__':
    unittest.main()
