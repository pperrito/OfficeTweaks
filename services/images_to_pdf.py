import img2pdf
from .base_service import Action
from . import utils


class ImagesToPdf(Action):
    command = "img2pdf"
    doc = "Преобразовать картинки в PDF"

    def run_action(self):
        files = utils.menu_with_all_files(
            self.params, (".jpeg", ".png", ".jpg"), all_option=True
        )

        with open(f"{self.params / files[0]}.pdf", "wb") as pdf:
            pdf.write(img2pdf.convert(*[str(self.params / f) for f in files]))
