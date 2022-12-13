from docx2pdf import convert
from . import utils
from .base_service import Action


class WordToPdf(Action):
    command = "word2pdf"
    doc = "Преобразовать Docx в PDF"

    def run_action(self):
        files = utils.menu_with_all_files(
            self.params, (".doc", ".docx"), all_option=True
        )
        for file in files:
            output = (
                self.params / f"{file[:-4] if file.endswith('.doc') else file[:-5]}.pdf"
            )
            convert(self.params / file, output_path=output)
        print("Конвертация завершена! \n")
