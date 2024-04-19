# 📄PDF-to-Image-Encryptor

The PDF-to-Image-Encryptor is a Python application designed to securely convert PDF pages to encrypted images. It ensures the privacy and security of the information within the PDF documents by encrypting the output images and also provides the functionality to decrypt them back to their original form.

## Features
- **PDF to Image Conversion**: Converts each page of a PDF document into an image.
- **Encryption**: Utilizes encryption to secure the images derived from PDF pages.
- **Decryption**: Allows the decryption of the encrypted images to revert them to their original state.
- **Batch Processing**: Capable of processing multiple pages up to a specified limit.

## Prerequisites
Before running this script, ensure you have the following installed:
- Python 3.6 or higher
- Cryptography library
- PyMuPDF (fitz)

## Installation
Follow these steps to set up the project on your local machine:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/PDF-to-Image-Encryptor.git
   ```
2. Navigate to the Project Directory
   ```bash
   cd PDF-to-Image-Encryptor
   ```

3. Install Required Libraries
   ```bash
   pip install cryptography PyMuPDF
   ```

## Usage
To use the application, follow these instructions:

1. Save Your PDF Document
- Ensure your PDF file is saved in the root directory of the project.

2. Run the Encryption Script
   ```bash
   python main.py
   ```
- This will convert and encrypt the PDF pages and save them as .enc files.



## Configuration
- The script is currently set to process up to 10 pages of a PDF document. This can be adjusted in the `mains.py` file.

## Contributing
Contributions to the PDF-to-Image-Encryptor are welcome! Here are a few ways you can help:
- Report bugs
- Add new features
- Improve documentation

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.




