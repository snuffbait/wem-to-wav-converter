import subprocess
from pathlib import Path

def ihatewems(folder):
    path = Path(folder)
    
    exe = None
    for name in ['vgmstream-cli.exe', 'vgmstream.exe']:
        if Path(name).exists():
            exe = name
            break
        test = path / name
        if test.exists():
            exe = str(test)
            break
    
    out = Path("output")
    out.mkdir(exist_ok=True)
    
    for wem in path.glob("*.wem"):
        wav = out / f"{wem.stem}.wav"
        
        subprocess.run([exe, "-o", str(wav), str(wem)], capture_output=True)
//reminder put everything in the folder and create a folder called sigma where the wems will be stored durrr..
ihatewems("sigma")
