import os
import time

# connect the bluetooth of cell ##################################
os.system('blueutil --paired')
print()
my_phone_MAC = input('please type the MAC address of your device: ')
# my_phone_MAC = '58-cb-52-9a-df-60' # the MAC address of the cell 
isConnected = os.popen('echo "$(blueutil --is-connected %s)"' % my_phone_MAC).read()

while True:
    # first connect
    if '0' in isConnected:
        os.system('blueutil --connect %s' % my_phone_MAC)  
        isConnected = os.popen('echo "$(blueutil --is-connected %s)"' % my_phone_MAC).read()     
        # second check
        if '0' in isConnected:
            os.system('pmset displaysleepnow')            
        else:
            print('device %s is connected' % my_phone_MAC)
    else:
        print('device %s is already connected' % my_phone_MAC)
        
    time.sleep(3)
    isConnected = os.popen('echo "$(blueutil --is-connected %s)"' % my_phone_MAC).read()

























