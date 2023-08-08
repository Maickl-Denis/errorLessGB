import shutil, os
class FileManager:
    def __init__(self, file):
            self.file = file

    def writefile(self):
        try:
            for line in open(file=self.file, encoding='utf8'):
                print(line, end='')
        except FileNotFoundError:
            print(f"Файл {self.file} не обнаружен")

    def readfile(self, text):
        with open(self.file, mode='a', encoding='utf8') as file:
            file.write(f"{text}\n")

    def copyfile(self, new_name):
        os.system("chcp 65001 > nul")
        try:
            if os.path.isfile(self.file):
                shutil.copyfile(self.file, new_name)
            else: raise FileNotFoundError
        except FileNotFoundError:
            print(f"Файл {self.file} не обнаружен или не задано название нового файла")

if __name__ == '__main__':
    f = FileManager('test.txt')
    # f.readfile("")
    # f.writefile()
    f.copyfile("")
