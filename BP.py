from boilerpipe.extract import Extractor
import os


directoryEntree = r'/home/romaric/PycharmProjects/scrapping/Corpus_detourage/html/'
outputDirectory = r'/home/romaric/PycharmProjects/scrapping/BP/'


for f in os.listdir(directoryEntree):

    completeName = os.path.join(outputDirectory,f)
    fichierEntree = open(directoryEntree + f, "r", encoding="utf8",errors="ignore")
    fichierSortie = open(outputDirectory + f, "w", encoding="utf8",errors="ignore")
    extracteur = Extractor(extractor='ArticleExtractor', html=fichierEntree.read())
    fichierSortie.write(extracteur.getHTML())

