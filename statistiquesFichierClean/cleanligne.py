import os
import statistics

path = "./Corpus_detourage/clean/"

data = []

filelist = os.listdir(path)

for file in filelist:
    data.append(len(open(path+file).readlines()))

print("La moyenne : " + str(statistics.mean(data)))
print("l'écart-type : " + str(statistics.stdev(data)))