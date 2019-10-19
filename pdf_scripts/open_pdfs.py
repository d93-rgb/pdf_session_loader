import sys, os, subprocess, re

# file with the pdf paths, create it manually if it's not existing
PDF_FILE = ('C:\\Users\\Damian\\Documents\\Programming\\Python\\PDF_Related\\'
    'pdf_session_loader\\pdf_scripts\\pdf_files.txt')
# type of pdfs to open
PDF_THEME = ""

# specify alternative SumatraPDF appdata folder to allow some multiple session functionality
NO_SESSION_DIRECTORY = "C:\\Users\\Damian\\Documents\\SumatraPDF\\No Session\\"

NO_SESSION = False
argList = []

# processing arguments
if len(sys.argv) > 1:
    print(sys.argv)
    for args in sys.argv:
        if args == "nosession":
            NO_SESSION = True
        elif args == "physics":
            PDF_THEME = "[PHYSICS]"
            #append_pdf_list(argList, PHYSICS_PDFS)  
        elif args == "maths":
            PDF_THEME = "[MATHS]"
            #append_pdf_list(argList, MATHS_PDFS)
        elif args == "engineering":
            PDF_THEME = "[ENGINEERING]"
            #append_pdf_list(argList, ENG_PDFS)
        elif args == "NT" or args == "nt":
            PDF_THEME = "[NACHRICHTENTECHNIK]"
        elif args == "RT" or args == "rt":
            PDF_THEME = "[REGELUNGSTECHNIK]"
        elif args == "HT" or args == "ht":
            PDF_THEME = "[HOCHFREQUENZTECHNIK]"
        elif args == "EDS" or args == "eds":
            PDF_THEME = "[ENTWURF DIGITALER SYSTEME]"
        elif args == "ALGO" or args == "algo" or args == "alg" or args == "ads":
            PDF_THEME = "[ALGORITHMEN UND DATENSTRUKTUREN]"

# utf8 encoding for german letters like äöüß
    with open(PDF_FILE, "r", encoding="utf8") as file_object:    
        for line in file_object:
            if line.strip() != PDF_THEME:
                next
            else:
                while True:
                    pdf_path = file_object.readline().strip()
                    #if pdf_path == "END" or pdf_path == "":
                    if re.fullmatch(r"\[.*\]", pdf_path) or pdf_path == "" \
                        or pdf_path[0] == '#':      
                        break
                    if not os.path.exists(pdf_path):
                        print("Error: The file \"{}\" does not exist".format(pdf_path))
                        exit(1)
                    argList.append(pdf_path)
                break
    
    if not argList and not NO_SESSION:
        print("Error: PDF file list is empty.")
        exit(1)
    if NO_SESSION:
        argList.insert(0, NO_SESSION_DIRECTORY)
        argList.insert(0, "-appdata")
    subprocess.Popen(
    ["C:\\Program Files\\SumatraPDF\\SumatraPDF.exe",
    *argList])
else:
    print("Error: Nothing to open.")
#os.system('"C:\\Program Files\\SumatraPDF\\SumatraPDF.exe"')

