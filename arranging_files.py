import shutil,os,pathlib,fnmatch
class Files_Arranger:
    def __init__(self,src,dst,pattern):
        self.src = src
        self.dst = dst
        self.pattern = pattern
    def  __repr__(self):
        return f"{self.src} {self.dst} {self.pattern}"

    def arrange(self):
            count = 0
            if not os.path.isdir(self.dst):
                pathlib.Path(self.dst).mkdir(parents = True, exist_ok=True)
            for p in self.pattern:
                try:
                    for f in fnmatch.filter(os.listdir(self.src),p):
                        if src.find(f):
                            for file in folder_or_file_name:
                                if f.find(file) is not -1:
                                    print(f)
                                    shutil.move(os.path.join(self.src,f),os.path.join(self.dst,f))
                                    count +=1
                                    print(count)
                except FileNotFoundError:  
                    print("YYYYYYIIIIIIIIKKKKKKEEEEESSSSS")

# how the class is initialised
src = "c:\\Users\\Himself\\Downloads"
dst = "c:\\Users\\Himself\\Downloads\\Torrent"
pattern  = ["*"]
path = Files_Arranger(src,dst,pattern)
folder_or_file_name = [".torrent"]
path.arrange()

