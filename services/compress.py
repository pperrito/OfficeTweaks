from PIL import Image
from .base_service import Action
from . import utils


class Compres(Action):
    command = "compress"
    doc = "Произвести сжатие изображений"

    def run_action(self):
        files = utils.menu_with_all_files(
            self.params, (".jpeg", ".gif", ".png", ".jpg"), all_option=True
        )
        quality = int(
            input(
                "Введите степень сжатия от 100 до 1, где 100 - минимум, а 1 - максимум: "
            )
        )
        for file in files:
            output = (
                self.params
                / f"compressed_{file[:-4] if file.endswith(('.gif', '.png', '.jpg')) else file[:-5]}.jpg"
            )
            image = Image.open(self.params / file)
            image.save(output, quality=quality)
        print("Сжатие завершено! \n")
