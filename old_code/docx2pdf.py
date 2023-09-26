import os
import subprocess

start = True

while start:
    # Specify the folder path
    folder_path = "docx"

    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Print the names of all files in the folder
    num = 0
    for file in files:
        num += 1
        print(f"{num}. {file}")

    choose = input("Please enter the number of the file you want to choose: ")

    # Convert the chosen input to an integer
    try:
        choose = int(choose)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    # Verify if the chosen number is within the valid range
    if choose < 1 or choose > len(files):
        print("Invalid input. Please enter a valid number.")
        continue

    chosen_file = files[choose - 1]
    file_name = os.path.splitext(chosen_file)[0]
    print("Chosen file:", file_name)

    start = False


def convert_docx_to_pdf(docx_file_path, pdf_file_path):
    subprocess.run(["unoconv", "-f", "pdf", "-o", pdf_file_path, docx_file_path])
    print("Conversion successful!")


# Specifing the input DOCX file path
docx_path = "docx/cv-template-1.docx"

# Specifing the output PDF file path and name
pdf_path = f"pdfs/{file_name}.pdf"

# Convert DOCX to PDF
convert_docx_to_pdf(docx_path, pdf_path)
