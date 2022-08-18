import subprocess, os, platform
if platform.system() == 'Darwin':       # macOS
    subprocess.call(('open', '/Users/hdquemada/Sync/Hector\ Quemada/Downloads/testfile.pdf'))
elif platform.system() == 'Windows':    # Windows
    os.startfile(filepath)
else:                                   # linux variants
    subprocess.call(('xdg-open', filepath))