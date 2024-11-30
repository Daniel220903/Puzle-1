import zipfile
import os
from PIL import Image
from collections import Counter
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
zip_path = 'C:\\Users\\dvill\\Downloads\\digits.zip'
unzip_folder = 'C:\\Users\\dvill\\Downloads\\digits_folder'

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(unzip_folder)

digit_counts = Counter()

digits_folder = os.path.join(unzip_folder, 'digits')

if not os.path.exists(digits_folder):
    print("No se encontró la carpeta 'digits' dentro del archivo ZIP.")
else:
    for filename in os.listdir(digits_folder):
        file_path = os.path.join(digits_folder, filename)

        if os.path.isfile(file_path) and filename.endswith('.jpg'):
            try:
                img = Image.open(file_path)

                text = pytesseract.image_to_string(img, config='outputbase digits --psm 6')

                digit_counts.update(c for c in text if c.isdigit())
            except Exception as e:
                print(f"Error al procesar la imagen {filename}: {e}")

    result = [digit_counts.get(str(i), 0) for i in range(10)]

    print("Contador de dígitos (0-9):", result)
