import sys, os, subprocess, re

# file of pdf paths
PDF_FILE = "C:\\Users\\Damian\\Documents\\Programming\\Python\\PDF_Related\\pdf_session_loader\\pdf_scripts\\pdf_files.txt"
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
    elif sys.argv[1] = "NT" or sys.argv[1] = "nt"
        PDF_THEME = "[NACHRICHTENTECHNIK]"
    elif sys.argv[1] = "RT" or sys.argv[1] = "rt"
        PDF_THEME = "[REGELUNGSTECHNIK]"
    elif sys.argv[1] = "HT" or sys.argv[1] = "ht"
        PDF_THEME = "[HOCHFREQUENZTECHNIK]"
    elif sys.argv[1] = "ALGO" or sys.argv[1] = "algo" or sys.argv[1] = "alg"
        PDF_THEME = "[ALGORITHMEN UND DATENSTRUKTUREN]"

    with open(PDF_FILE, "r", encoding="utf8") as file_object:    
        for line in file_object:
            if line.strip() != PDF_THEME:
                next
            else:
                while True:
                    pdf_path = file_object.readline().strip()
                    #if pdf_path == "END" or pdf_path == "":
                    if re.fullmatch(r"\[.*\]", pdf_path) or pdf_path == "":
                        break
                    if not os.path.exists(pdf_path):
                        print("Error: The file \"{}\" does not exist".format(pdf_path))
                        exit(1)
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

