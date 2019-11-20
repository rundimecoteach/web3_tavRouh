import justext
import os
import statistics

""" Fichier qui calcule avec just text la moyenne et l'écart type du nombre de caractères 
et fait la comparaison avec le fichier clean """

directory = r'/home/romaric/PycharmProjects/scrapping/Corpus_detourage/html'

save_path = "./JT"
count = 0
ecartypeLigne = 0
moyenneLigne = 0
nbChar = 0
ecartypeChar = 0
moyenneChar = 0

jtStats = []
for filename in os.listdir(directory):
    count += 1
    nbline = 0
    completeName = os.path.join(save_path, filename)

    # Création des fichiers en écriture
    cf = open(completeName, "w+")


    # Parcours des fichiers en lecture
    f = open(directory+"/"+filename, "r",encoding="utf-8",errors='ignore')

    paragraphs = justext.justext(f.read(),justext.get_stoplist("English"))


    # Ecriture de chaques paragraphes dans le fichier d'écriture
    for paragraph in paragraphs:
        if not paragraph.is_boilerplate:
            cf.write("<p>"+paragraph.text+"</p>"+"\n")

f.close()
cf.close()

data = []


#calcul des statistiques justtext
filelist = os.listdir(save_path+"/")
somme = 0
for file in filelist:
    chars = 0
    lines = 0
    fchar =open(save_path+"/" + file,'r')
    for line in fchar.readlines():
        lines +=1
        for char in line:
            chars +=1
    data.append(chars)


def cleanStat():

    path = "./Corpus_detourage/clean/"
    data = []
    filelist = os.listdir(path)
    for file in filelist:
        data.append(len(open(path + file).readlines()))

    return data

def compare(cleanStats,jtStats):
    comparaison = []
    for i in range(len(cleanStats)):
        comparaison.append(abs(cleanStats[i]-jtStats[i]))
    return comparaison

print(compare(cleanStat(),data))
