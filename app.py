import os
from pathlib import Path
from services import services


def menu():
    WORKING_DIR = Path.cwd()
    while True:
        print("Текущий каталог:", WORKING_DIR, "\n")
        print("0. Сменить рабочий каталог")
        for idx, service in enumerate(services, start=1):
            print(f"{idx}. {service.doc}")
        print(f"{len(services) + 1}. Выход\n")
        choice = int(input("Ваш выбор: "))

        if choice == len(services) + 1:
            exit(0)
        elif choice == 0:
            catalog = input("Укажите корректный путь к рабочему каталогу: ")
            WORKING_DIR = Path(catalog)
        elif choice > 0 and choice <= len(services):
            services[choice - 1](WORKING_DIR).run_action()
        else:
            print("Вы куда-то не туда попали")

        input("Нажмите любую кнопку для продложения... ")
        os.system("cls")


if __name__ == "__main__":
    menu()
