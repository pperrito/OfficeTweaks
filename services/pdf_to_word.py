import pdf2docx
from . import utils
from .base_service import Action


class PdfToWord(Action):
    command = "pdf2word"
    doc = "Преобразовать PDF в Docx"

    def run_action(self):
        files = utils.menu_with_all_files(self.params, ".pdf", all_option=True)
        for file in files:
            output = self.params / f"{file[:-4]}.docx"
            conv = pdf2docx.Converter(self.params / file)
            conv.convert(str(output))
        print("Конвертация завершена! \n")
