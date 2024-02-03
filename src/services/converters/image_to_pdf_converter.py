import img2pdf
import glob
import io
import tempfile

"""
Image to PDF
    - Single image to pdf
    - Multiple Images to pdf
"""

def image_to_pdf_from_file(image_contents: list[bytes]) -> bytes:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(img2pdf.convert(image_contents))
        with open(temp_file.name, 'rb') as file_content:
            final_content = io.BytesIO(file_content.read())
            temp_file.close()
            return final_content
    

# To be updated more, when storage APIs are done
def image_to_pdf_from_static_folder():
    static_folder = "./static"
    image_files = glob.glob(static_folder + ".*png") + glob.glob(static_folder + ".*jpg") + glob.glob(static_folder + ".*jpeg")
    image_files.sort()
    with open("output.pdf", "wb") as f:
        f.write(img2pdf.convert(image_files))
        f.close()
        print("Images converted to PDF successfully")