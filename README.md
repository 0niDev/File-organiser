# File Organizer - Automatically Sort Files by Extension

This Python script helps you organize your files by sorting them into specific directories based on their file extensions. It categorizes files into documents, videos, music, pictures, executables, and others.

## Usage

1. Clone or download this repository to your local machine.
2. Place the `main.py` script in the directory containing the files you want to organize.
3. Run the script `main.py`.
4. The script will create directories (if they don't exist) named `documents`, `videos`, `music`, `pictures`, `executables`, and `other`.
5. Files will be moved to their corresponding directories based on their extensions.

## Supported Extensions

- **Documents**: doc, docx, txt, pdf, rtf, odt, csv, xlsx, xls, pptx, ppt, odp, html
- **Videos**: mp4, avi, mkv, mov, wmv, flv, webm, m4v, mpeg, mpg, 3gp, 3g2
- **Music**: mp3, wav, ogg, flac, aac, wma, m4a, alac, aiff, mid, midi
- **Pictures**: jpg, jpeg, png, gif, bmp, tiff, webp, svg, ico, jfif, heif, raw
- **Executables**: exe, dmg, app, apk, msi, bat, sh
- **Others**: Any file with an extension not listed above

## Note

- Make sure you have Python installed on your system.
- Before running the script, review and edit the `GetNames` function if you want to target specific directories other than the current working directory.

### Fee free to make any changes
