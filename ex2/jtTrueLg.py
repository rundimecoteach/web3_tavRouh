import os
import justext
import json
jtFilesdir = r'/home/romaric/PycharmProjects/scrapping/JT/'

htmlFilesdir = r'/home/romaric/PycharmProjects/scrapping/Corpus_detourage/html/'

fichierNettoyes = r'/home/romaric/PycharmProjects/scrapping/JT_trueLg/'

htmlFiles = []
jtFiles = []



with open('doc_lg.json') as json_file:
    langJsonData = json.load(json_file)

for htmlFile in os.listdir(htmlFilesdir):
    htmlFiles.append(htmlFile)

for jtFile in os.listdir(jtFilesdir):
    jtFiles.append(jtFile)

for i in range(len(jtFiles)):
    if langJsonData[htmlFiles[i]] == "Chinese":
        langJsonData[htmlFiles[i]] = "English"

    # Création des fichiers en écriture
    wf = open(fichierNettoyes+jtFiles[i], "w+")

    if os.stat(jtFilesdir+jtFiles[i]).st_size != 0:

        # Parcours des fichiers en lecture
        jtf = open(jtFilesdir+jtFiles[i], "r", encoding="utf-8", errors='ignore')
        try:
            paragraphs = justext.justext(jtf.read(), justext.get_stoplist(langJsonData[jtFiles[i]]))
            # Ecriture de chaques paragraphes dans le fichier d'écriture
            for paragraph in paragraphs:
                if not paragraph.is_boilerplate:
                 wf.write("<p>" + paragraph.text + "</p>" + "\n")

        except ValueError:
            print("Erreur in jtfile : mauvaise reconnaissance de langue")

    else:

        # Parcours des fichiers en lecture
        hf = open(htmlFilesdir+htmlFiles[i], "r", encoding="utf-8", errors='ignore')
        try:
            paragraphs = justext.justext(hf.read(), justext.get_stoplist(langJsonData[htmlFiles[i]]))
            # Ecriture de chaques paragraphes dans le fichier d'écriture
            for paragraph in paragraphs:
                if not paragraph.is_boilerplate:
                 wf.write("<p>" + paragraph.text + "</p>" + "\n")

        except ValueError:
            print(langJsonData[htmlFiles[i]]+"  mauvaise reconnaissance de langue")
