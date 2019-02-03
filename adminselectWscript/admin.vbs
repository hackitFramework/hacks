Set oShell = CreateObject("Shell.Application")
oShell.ShellExecute "cmd.exe", , , "runas", 1
oShell.Run "nodepad.exe"
