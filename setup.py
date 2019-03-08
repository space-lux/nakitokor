from cx_Freeze import setup, Executable

#build_exe_options = {"packages": []}

setup(
    name = "aki",
    version = "1",
    description = "Nakitokor",
	#options = {"build_exe": build_exe_options},
    executables = [Executable("main.py",base = "Win32GUI")],
)