import subprocess

# Need to install pandoc and pdflatex for this to work properly
class PandocConverter:
    def __init__(self) -> None:
        pass

    def convert_document(input_file, output_file, input_format, output_format):
        pandoc_command = ["pandoc", f"{input_file}", f"-f{input_format}", f"-o{output_file}", f"-t{output_format}"]
        try:
            subprocess.run(pandoc_command, check=True)
            print(f"Conversion Successful. Output file can be found here: {output_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error occurred during conversion: {e}")