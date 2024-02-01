import os

def deleteFiles(directory, prefix):
    files = os.listdir(directory)
    
    for file in files:
        if file.startswith(prefix):
            filePath = os.path.join(directory, file)
            
            os.remove(filePath)
            print(f"Deleted: {filePath}")


downloadsPath = os.path.expanduser('~') + '/Downloads'

prefixes = ["payment", "loan", "cbs", "EFX", "TUN", "EXP", "account_", "Scan"]

for prefix in prefixes:
    deleteFiles(downloadsPath, prefix)
