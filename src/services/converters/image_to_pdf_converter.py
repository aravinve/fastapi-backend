import img2pdf
import glob

"""
Image to PDF
    - Single image to pdf
    - Multiple Images to pdf
"""

def image_to_pdf_from_file():
    static_folder = "./static"
    image_files = glob.glob(static_folder + ".*png") + glob.glob(static_folder + ".*jpg") + glob.glob(static_folder + ".*jpeg")
    image_files.sort()
    with open("output.pdf", "wb") as f:
        f.write(img2pdf.convert(image_files))
        f.close()
        print("Images converted to PDF successfully")