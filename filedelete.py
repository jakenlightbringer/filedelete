import os


def deleteFiles(directory, prefix):
    files = os.listdir(directory)
    
    for file in files:
        if file.startswith(prefix):
            filePath = os.path.join(directory, file)
            
            os.remove(filePath)
            print(f"Deleted: {filePath}")
            
directoryPath = 'C:/Users/jacob/Downloads'
prexifes = ["payment", "loan", "cbs", "EFX", "TUN", "EXP", "account", "Scan"]

for prefix in prexifes:
    deleteFiles(directoryPath, prefix)
