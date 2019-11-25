from ex3.cleaneval_tool import *
import langid
import os

eval = {}

pathHtml = "../Corpus_detourage/html/"
pathJT = "../JT/"
pathJT_langid = "../JT_langid/"
pathBS = "../BS/"
pathJT_Truelg = "../JT_trueLg/"

def instrinseque(path):
    pathClean = "../Corpus_detourage/clean/"

    resultats = {
        'el': {'f-score': 0, 'precision': 0, 'recall': 0},
        'en': {'f-score': 0, 'precision': 0, 'recall': 0},
        'pl': {'f-score': 0, 'precision': 0, 'recall': 0},
        'ru': {'f-score': 0, 'precision': 0, 'recall': 0},
        'zh': {'f-score': 0, 'precision': 0, 'recall': 0},
        'all': {'f-score': 0, 'precision': 0, 'recall': 0}
    }

    for f in os.listdir(path):
        if os.stat(pathJT + f).st_size != 0:

            file = open(pathJT + f, 'r', encoding='ISO-8859-1', errors="ignore")
            s = file.read()
        else:
            file = open("../Corpus_detourage/html/" + f, 'r', encoding='ISO-8859-1', errors="ignore")
            s = file.read()

        lang = langid.classify(s)

        print(path + f)
        print(pathClean + f)

        evaluation = evaluate_file(path + f, pathClean + f)

        resultats[lang[0]]['f-score'] += evaluation['f-score']
        resultats[lang[0]]['precision'] += evaluation['precision']
        resultats[lang[0]]['recall'] += evaluation['recall']

        resultats['all']['f-score'] += evaluation['f-score']
        resultats['all']['precision'] += evaluation['precision']
        resultats['all']['recall'] += evaluation['recall']

    for k in resultats:
        for i in resultats[k]:
            resultats[k][i] = resultats[k][i] / len(f)

    return resultats

if __name__ == '__main__':
    eval["JT"] = instrinseque(pathJT)
    eval["JT_langid"] = instrinseque(pathJT_langid)
    eval["JT_trueLg"] = instrinseque(pathJT_Truelg)
