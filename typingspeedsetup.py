from cx_Freeze import *

includefiles=['typingspeed.ico']
base=None
if sys.platform == "win32":
    base="Win32GUI"

shortcut_table=[
    ("Desktopshortcut", #shortcut
     "DesktopFolder",   #Directory_
     "Typing_speed",    #Name
     "TARGETDIR",       #Component_
     "[TARGETDIR]\Typingspeed.exe",#Target
     None, #Arguments
     None, #Description
     None, #Hotkey
     None, #Icon
     None, #Iconindex
     None, #ShowCmd
     "TARGETDIR", #WkDir
     )
]
msi_data={"Shortcut" :shortcut_table}

bdist_msi_options={'data': msi_data}
setup(
    version="1.0",
    description="Typing Speed Increase Game",
    author="ForCodeCoder",
    name="Typing Speed",
    options={'build_exe':{'include_files':includefiles},"bdist_msi":bdist_msi_options,},
    executables=[
        Executable(
            script="Typingspeed.py",
            base=base,
            icon='typingspeed.ico',
        )
    ]
)    
        
        
