from cx_Freeze import setup, Executable
import os

os.environ['TCL_LIBRARY']="C:\\Users\\Max\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY']="C:\\Users\\Max\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tk8.6"

executables = [Executable("playify-transfer.py", base="Win32GUI", targetName="playify-transfer-invisible.exe"), Executable("playify-transfer.py", base=None)]

options = {
    'build_exe': {
        'packages': ["json", "os"],
		'includes': ["gmusicapi", "websocket_server", "validictory", "decorator", "mutagen", "dateutil", "proboscis", "oauth2client", "mock", "appdirs", "gpsoauth", "mechanicalsoup", "six", "future", "google"]
    }
}

setup(
    name = "playify-transfer",
    options = options,
    version = "1.0",
    description = "playify-transfer",
    executables = executables
)