import sys, os, subprocess

# file of pdf paths
PDF_FILE = "C:\\Users\\Damian\\Documents\\Programming\\Python\\pdf_scripts\\pdf_files.txt"
PDF_THEME = ""

argList = []

# pdf file names
if len(sys.argv) > 1:
    if sys.argv[1] == "physics":
        PDF_THEME = "[PHYSICS]"
        #append_pdf_list(argList, PHYSICS_PDFS)  
    elif sys.argv[1] == "maths":
        PDF_THEME = "[MATHS]"
        #append_pdf_list(argList, MATHS_PDFS)
    elif sys.argv[1] == "engineering":
        PDF_THEME = "[ENGINEERING]"
        #append_pdf_list(argList, ENG_PDFS)    

    with open(PDF_FILE, "r", encoding="utf8") as file_object:    
        for line in file_object:
            if line.strip() != PDF_THEME:
                next
            else:
                while True:
                    pdf_path = file_object.readline().strip()
                    if pdf_path == "END":
                        break
                    argList.append(pdf_path)
                break
    
    if argList:
        subprocess.Popen(
        ["C:\\Program Files\\SumatraPDF\\SumatraPDF.exe",
        *argList])
    else:
        print("Error: PDF file list is empty.")
else:
    print("Error: Nothing to open.")
#os.system('"C:\\Program Files\\SumatraPDF\\SumatraPDF.exe"')

