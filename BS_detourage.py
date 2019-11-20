import os
import statistics

from bs4 import BeautifulSoup

data_dir = './Corpus_detourage/html/'
save_path = 'BS/'
data = []
nbChar =0

# parcours des fichiers & lecture
for file in os.listdir(data_dir):

    nbline = 0
    nbChar += 1


    f = open(data_dir + file, "r", encoding="utf-8", errors='ignore')

    soup = BeautifulSoup(f, 'html.parser')
    paragraphs= soup.get_text().split('\n')

    # création d'un fichier en écriture
    nameBS = os.path.join(save_path, file)
    cf = open(nameBS, "w+")

    # écriture de chaque paragraphes dans le fichier
    for paragraph in paragraphs:
        cf.write("<p>"+paragraph+"</p>"+"\n")
        nbline+=1
    data.append(nbline)

print(nbChar)
print("La moyenne :" + str(statistics.mean(data)))
print("l'écart-type :"+ str(statistics.stdev(data)))
