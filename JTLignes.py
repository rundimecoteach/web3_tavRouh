import justext
import os
import  statistics

""" Fichier qui calcule avec just text la moyenne et l'écart type du nombre de lignes """

directory = r'/home/romaric/PycharmProjects/scrapping/Corpus_detourage/html'

save_path = "./JT"
count = 0
ecartypeLigne = 0
moyenneLigne = 0
nbChar = 0
ecartypeChar = 0
moyenneChar = 0

data = []
jtStats = []
for filename in os.listdir(directory):
    count += 1
    nbline = 0
    completeName = os.path.join(save_path, filename)
    cf = open(completeName, "w+")
    f = open(directory+"/"+filename, "r",encoding="utf-8",errors='ignore')

    paragraphs = justext.justext(f.read(),justext.get_stoplist("English"))

    for paragraph in paragraphs:
        if not paragraph.is_boilerplate:
            cf.write("<p>"+paragraph.text+"</p>"+"\n")
            nbline+=1
    jtStats.append(nbline)


print("La moyenne : " + str(statistics.mean(data)))
print("l'écart-type : " + str(statistics.stdev(data)))



