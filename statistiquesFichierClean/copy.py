import justext
import os
import statistics



directory = r'/home/romaric/PycharmProjects/scrapping/Corpus_detourage/html'

save_path = "./JT"
count = 0
nbChar = 0

jtStats = []
for filename in os.listdir(directory):
    count += 1
    # Parcours des fichiers en lecture
    f = open(directory + "/" + filename, "r", encoding="utf-8", errors='ignore')

    # Création des fichiers en écriture
    completeName = os.path.join(save_path, filename)
    cf = open(completeName, "w+")

    paragraphs = justext.justext(f.read(), justext.get_stoplist("English"))
    # Ecriture de chaques paragraphes dans le fichier d'écriture
    for paragraph in paragraphs:
        if not paragraph.is_boilerplate:
            cf.write("<p>" + paragraph.text + "</p>" + "\n")

f.close()
cf.close()

# Calcul des statistiques
data = []
filelist = os.listdir(save_path + "/")
somme = 0
for file in filelist:
    chars = 0
    lines = 0
    fchar = open(save_path + "/" + file, 'r')
    for line in fchar.readlines():
        lines += 1
        for char in line:
            chars += 1
    jtStats.append(chars)


def cleanStatChar():
    path = "./Corpus_detourage/clean/"

    filelist = os.listdir(path)
    for file in filelist:
        chars = 0
        lines = 0
        fchar = open(path + file, 'r')
        for line in fchar.readlines():
            lines += 1
            for char in line:
                chars += 1
        jtStats.append(chars)


def compare(cleanStats, jtStats):
    print(len(cleanStats))
    print(len(jtStats))
    result = []
    for i in range(len(cleanStats)):
        result.append(abs(cleanStats[i] - jtStats[i]))
    return result


print(compare(cleanStatChar(), jtStats))

# print("La moyenne : " + str(statistics.mean(data)))
# print("l'écart-type : " + str(statistics.stdev(data)))