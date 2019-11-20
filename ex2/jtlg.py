import os
import langid
import justext
jtFilesdir = r'/home/romaric/PycharmProjects/scrapping/JT/'

htmlFilesdir = r'/home/romaric/PycharmProjects/scrapping/Corpus_detourage/html/'

fichierNettoyes = r'/home/romaric/PycharmProjects/scrapping/JT_langid/'

htmlFiles = []
jtFiles = []

lang = {
    'el': 'Greek',
    'en': 'English',
    'pl': 'Polish',
    'ru': 'Russian',
    'zh': 'English'
}

for htmlFile in os.listdir(htmlFilesdir):
    htmlFiles.append(htmlFile)

for jtFile in os.listdir(jtFilesdir):
    jtFiles.append(jtFile)

for i in range(len(jtFiles)):
    langid.set_languages(lang)
    # Création des fichiers en écriture
    wf = open(fichierNettoyes+jtFiles[i], "w+")

    if os.stat(jtFilesdir+jtFiles[i]).st_size != 0:

        # Parcours des fichiers en lecture
        jtf = open(jtFilesdir+jtFiles[i], "r", encoding="utf-8", errors='ignore')

        try:
            paragraphs = justext.justext(jtf.read(), justext.get_stoplist(lang.get(langid.classify(jtFiles[i])[0])))
            # Ecriture de chaques paragraphes dans le fichier d'écriture
            for paragraph in paragraphs:
                if not paragraph.is_boilerplate:
                 wf.write("<p>" + paragraph.text + "</p>" + "\n")

        except ValueError:
            print("mauvaise reconnaissance de langue")

    else:

        # Parcours des fichiers en lecture
        hf = open(htmlFilesdir+htmlFiles[i], "r", encoding="utf-8", errors='ignore')
        try:
            paragraphs = justext.justext(hf.read(), justext.get_stoplist(lang.get(langid.classify(htmlFiles[i])[0])))
            # Ecriture de chaques paragraphes dans le fichier d'écriture
            for paragraph in paragraphs:
                if not paragraph.is_boilerplate:
                 wf.write("<p>" + paragraph.text + "</p>" + "\n")

        except ValueError:
            print("mauvaise reconnaissance de langue")
