import os
import time
import tkinter as tk
import pyautogui

# UI #######################################################################
# 建立主視窗和 Frame（把元件變成群組的容器）
window = tk.Tk()
window.title('device security app')
window_w = 1020
window_h = 800
# monitor info
monitor_w = pyautogui.size()[0]
monitor_h = pyautogui.size()[1]
# width*length + x-position + y-position 視窗置中
window.geometry('%sx%s+%s+%s' % (str(window_w), str(window_h), 
    str(int((monitor_w-window_w)/2)), str(int((monitor_h-window_h)/2)) ) ) 
window.configure(background='grey16')

# frame1 ######################################
frame1 = tk.Frame(window, bg='grey16')
frame1.pack()

# label: 固定在左上角
list_label = tk.Label(frame1,
    text="The paired bluetooth devices are shown in below:",
    bg='grey50', fg='grey95')
list_label.place(x=2, y=8) # position

# list devices #####################
# frame1_1 ############
frame1_1 = tk.Frame(frame1, bg='grey16')
frame1_1.pack(pady=38)
# create components
list_scrollbar = tk.Scrollbar(frame1_1)
device_list = tk.Text(frame1_1, height=20, width=140, 
    bg='grey50', fg='grey95')

device_list.bind("<Configure>",device_list.configure(width=monitor_w)) # device_list width 隨視窗大小改變

# pack
list_scrollbar.pack(side='right', fill='y')
device_list.pack(side='left', padx=1) # position
# config
list_scrollbar.config(command=device_list.yview)
device_list.config(yscrollcommand=list_scrollbar.set)
# insert text
device_list.insert('end', os.popen('echo "$(blueutil --paired)"').read())
# todo: read-only and able to copy text
# device_list.configure(state='disabled') # read only

# button to refresh list (in frame1)
refresh_button = tk.Button(frame1, text='Refresh')

list_label.update() # need to update before get winfo_width
refresh_button.place(x=list_label.winfo_width()+4, y=9)
# clear text box messages









# 運行主程式
window.mainloop()

# functions ######################################################################
# connect the bluetooth of device 
def bluetooth_connect():
    print('The paired bluetooth devices are shown in below:')
    os.system('blueutil --paired')
    print()
    my_phone_MAC = input('please type the MAC address of your device: ')
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

# list devices 
def list_devices():
    pass























