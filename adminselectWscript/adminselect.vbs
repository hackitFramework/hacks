set shellobj = CreateObject("WScript.Shell")
shellobj.sendkeys("^{Esc}")
wscript.sleep 1
shellobj.sendkeys "cmd"
wscript.sleep 100
shellobj.sendkeys ("+{F10}")
wscript.sleep 200
shellobj.sendkeys "{DOWN}"
wscript.sleep 1
shellobj.sendkeys "{ENTER}"
wscript.sleep 4000
'we assume now that the user does LEFT Arrow then ENTER\
2
