Set Player = CreateObject("WMPlayer.OCX")
Player.URL = "C:\Users\chans\Downloads\Yee.wav"

Player.controls.play
While Player.playState <> 1
	WScript.Sleep 100
WEnd

Player.close