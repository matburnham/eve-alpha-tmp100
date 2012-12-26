TMP100 i2c Python lib
=====================

I wrote this library to read the temperature from the EVE Alpha board which has a TMP100 with the address 0x48 it maybe of use to other people also.

Some useful things to install on your RaspberryPi:

sudo apt-get install i2c-tools  
sudo apt-get install python-smbus  
sudo adduser <yourusername> i2c  

You can list available devices using, check which i2c bus to configure the library to use:
i2cdetect -y 0
i2cdetect -y 1

Run indivdual tests to check library:

python -m unittest tmp100_test.TestTmp.test_getTemp
python -m unittest tmp100_test.TestTmp.test_set12bit
