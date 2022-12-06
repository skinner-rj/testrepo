import os
from VerificaAmostrasPFE import VerificaAmostrasPFE
from openpyxl import load_workbook, Workbook
cwd = os.getcwd()

#relaciona todos os arquivos de uma pasta e subpastas


import os
def getListOfFiles(dirName, ext):


    # create a list of file and sub directories
    # names in the given directory
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(dirName):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames if file.endswith(ext)]

    return listOfFiles

ext = '.xlsx'
def create_folder()
    for file in getListOfFiles(cwd, ext):
        basedir = file[:-5]

        try:
            os.mkdir(newdir)
        except OSError:
            print('Erro na criação da pasta %s'%path)
        #move os arquivos ja lidos para uma pasta de backup\n",
        arquivo = os.path.basename(file)
        os.rename(file, newdir+"\\"+arquivo)
