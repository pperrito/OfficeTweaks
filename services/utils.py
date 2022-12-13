import os


def menu_with_all_files(
    path: str, suffix: str | tuple[str], all_option: bool = False
) -> list[str]:
    result = []
    rawfiles = os.listdir(path)
    c = 1
    files = {}
    print(f"Список файлов с расширением {suffix} в данном каталоге:\n")
    for file in rawfiles:
        if file.endswith(suffix):
            print(f"{c}. {file}")
            files.update({c: file})
            c += 1
    choice = int(
        input(
            f"Введите номер файла для преобразования{' ( чтобы преобразовать все файлы из данного каталога, введите 0): ' if all_option else ': '}"
        )
    )
    if choice == 0:
        for v in files.values():
            result.append(v)
    else:
        result.append(files[choice])
    return result
