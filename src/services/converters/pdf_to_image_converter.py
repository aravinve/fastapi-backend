from pdf2image import convert_from_path

"""
PDF to Image
    - Single page pdf means single image
    - Multiple page pdf means multiple images
"""

def pdf_to_image_from_file():
    input_pdf_file = "input.pdf"
    output_image_format = "png"
    convert_from_path(input_pdf_file, fmt=output_image_format, output_folder="./images-out/")
    print("PDF converted to images successfully")