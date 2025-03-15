import os

def countLinesInFile(filePath):
    try:
        with open(filePath, 'r', encoding='utf-8', errors='ignore') as file:
            linesInFile = sum(1 for line in file)
            print(f'{filePath} Total Lines = {linesInFile}')
            return linesInFile
    except Exception as e:
        print(f'Could not read file {filePath}: {e}')
        return 0

def countLinesInFolder(folderPath, fileExtensions):
    totalLines = 0
    for root, _, files in os.walk(folderPath):
        for file in files:
            if file.endswith(tuple(fileExtensions)):
                filePath = os.path.join(root, file)
                totalLines += countLinesInFile(filePath)
    return totalLines

if __name__ == "__main__":
    folderPath = input('Enter the path of the folder: ')
    fileExtensions = ['.c', '.h', '.cpp', '.hpp']

    totalLines = countLinesInFolder(folderPath, fileExtensions)
    print(f'\nTotal lines of C/C++ code in the folder {folderPath} = {totalLines}')
