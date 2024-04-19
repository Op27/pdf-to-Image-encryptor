# PDF-to-Image-Encryptor: This script converts PDF pages to encrypted images for secure handling and storage, and includes functionality to decrypt these images.

# Please ensure to save your PDF file in the root folder of this project before running this code.

from cryptography.fernet import Fernet # Import Fernet for encryption functionalities
import fitz  # Import fitz (PyMuPDF) for handling PDF files

# Generate a key and instantiate a Fernet instance
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Open the PDF file
pdf_path = r'C:\PATH-TO-YOUR-PDF-FILE\image.pdf'
doc = fitz.open(pdf_path)

# Specify the number of pages to convert
num_pages = min(10, len(doc))  

# Convert and encrypt each page of the PDF to an image
for i in range(num_pages):
    page = doc.load_page(i)  # Load each page
    pix = page.get_pixmap()  # Convert page to an image pixmap
    img_bytes = pix.tobytes("png")  # Convert image to bytes
    encrypted_img = cipher_suite.encrypt(img_bytes)  # Encrypt image bytes
    with open(f'page_{i+1}.enc', 'wb') as f:
        f.write(encrypted_img)  # Write encrypted image to file

print("Images have been encrypted and saved.")

# Decrypt the previously encrypted images
for i in range(num_pages):
    with open(f'page_{i+1}.enc', 'rb') as f:
        encrypted_img = f.read()
    decrypted_img = cipher_suite.decrypt(encrypted_img)
    with open(f'decrypted_page_{i+1}.png', 'wb') as f:
        f.write(decrypted_img)  # Save the decrypted image as PNG

print("Decryption completed.")
