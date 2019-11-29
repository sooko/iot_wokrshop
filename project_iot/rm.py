import os

dirs=os.listdir()

for dir in dirs:
    os.remove(dir)
    print("terhapus")
    
