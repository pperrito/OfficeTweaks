import pdf2image
from .base_service import Action
from . import utils


class PdfToImages(Action):
    command = "pdf2img"
    doc = "Преобразовать PDF в картинки"

    def run_action(self):
        files = utils.menu_with_all_files(self.params, ".pdf", all_option=True)

        for file in files:
            output_path = self.params / file[:-4]
            output_path.mkdir()

            pdf2image.pdf2image.convert_from_path(
                self.params / file, output_folder=output_path, fmt="jpeg"
            )
        
        print("Конвертация завершена")