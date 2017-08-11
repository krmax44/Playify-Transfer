from cx_Freeze import setup, Executable
import os

executables = [Executable("playify-transfer.py", base="Win32GUI", targetName="playify-transfer-invisible.exe"), Executable("playify-transfer.py", base=None), Executable("password.py", base=None)]

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
