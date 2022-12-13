from .images_to_pdf import ImagesToPdf
from .pdf_to_images import PdfToImages
from .pdf_to_word import PdfToWord
from .word_to_pdf import WordToPdf
from .compress import Compres
from .delete_group import DeleteGroup

services = [PdfToWord, WordToPdf, Compres, DeleteGroup, ImagesToPdf, PdfToImages]
