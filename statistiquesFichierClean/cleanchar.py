import os
import statistics

path = "./Corpus_detourage/clean/"

data = []

filelist = os.listdir(path)

for file in filelist:
    f =open(path + file,'r')
    for line in f.readlines():
        data.append(len(line))

print("La moyenne : " + str(statistics.mean(data)))
print("l'écart-type : " + str(statistics.stdev(data)))