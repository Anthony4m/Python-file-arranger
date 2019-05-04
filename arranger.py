import shutil,os,pathlib,fnmatch

def path(src:str,dst:str,pattern:str="*.mp4"):
    if not os.path.isdir(dst):
        pathlib.Path(dst).mkdir(parents = True, exist_ok=True)
    for f in fnmatch.filter(os.listdir(src), pattern):
        shutil.move(os.path.join(src,f),os.path.join(dst,f))