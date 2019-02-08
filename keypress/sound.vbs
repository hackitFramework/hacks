Set Player = CreateObject("WMPlayer.OCX")
Player.URL = "" ' Path to Sound File

Player.controls.play
While Player.playState <> 1
	WScript.Sleep 100
WEnd

Player.close