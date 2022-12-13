import os
from .base_service import Action


class DeleteGroup(Action):
    command = "delete"
    doc = "Удалить группу файлов"

    def startwith(self, text):
        files = os.listdir(self.params)
        for file in files:
            if file.startswith(text) and os.path.isfile(self.params / file):
                os.remove(self.params / file)
    def endwith(self, text):
        files = os.listdir(self.params)
        for file in files:
            if file.endswith(text) and os.path.isfile(self.params / file):
                os.remove(self.params / file)

    def inname(self, text):
        files = os.listdir(self.params)
        for file in files:
            if text in file and os.path.isfile(self.params / file):
                os.remove(self.params / file)
    
    def run_action(self):
        print("Выберите действие:\n")
        print("1. Удалить все файлы, начинающиеся на определенную подстроку")
        print("2. Удалить все файлы, заканчивающиеся на определённую подстроку")
        print("3. Удалить все файлы, содержащие определенную подстроку")
        print("4. Удалить все файлы по расширению")
        action = input("Введите действие: ")
        match action:
            case "1":
                self.startwith(input("Введите подстроку: "))
            case "2":
                self.endwith(input("Введите подстроку: "))
            case "3":
                self.inname(input("Введите подстроку: "))
            case "4":
                self.endwith("."+ input("Введите расширение: "))
