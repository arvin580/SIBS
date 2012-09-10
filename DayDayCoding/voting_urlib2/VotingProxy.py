#coding=utf-8
from _winreg import *
def setProxy(proxy):
    keyVal = 'Software\Microsoft\Windows\CurrentVersion\Internet Settings'
    key = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    SetValueEx(key, 'ProxyEnable', 0,REG_SZ,"1")
    SetValueEx(key, 'ProxyServer', 0, REG_SZ, proxy)
    CloseKey(key)

setProxy('64.212.73.53:8080')




from PAM30 import PAMIE
import cModalPopUp
import winGuiAuto
ie = PAMIE()
ie.navigate("http://gzjd.shenyangsheying.com/View.asp?id=20") 
ie.clickImage("give_ticket.jpg") 
ok=cModalPopUp.handlePopup("Confirm","确定")
ok.start()
ie.quit()

'''
hwnd = winGuiAuto.findTopWindows("Windows Internet Explorer")
for it in hwnd :
	control=winGuiAuto.dumpWindow(it)
	for item in control:
		if item[1]=='确定':
			winGuiAuto.clickButton(item[0])
'''
