from ex3.cleanevaluationtool import *
from importlib.metadata import files
import os
import time
import langid


pathHtml = "../Corpus_detourage/html/"
pathClean = "../Corpus_detourage/clean/"
pathJT = "../JT/"
pathJT_langid = "../JT_langid/"
pathBS = "../BS/"
pathJT_Truelg = "../JT_TrueLg/"
lang = langid.classify(s)

def evalIntrin(path):
    results = {
        'el': {'f-score': 0, 'precision': 0, 'recall': 0},
        'en': {'f-score': 0, 'precision': 0, 'recall': 0},
        'pl': {'f-score': 0, 'precision': 0, 'recall': 0},
        'ru': {'f-score': 0, 'precision': 0, 'recall': 0},
        'zh': {'f-score': 0, 'precision': 0, 'recall': 0},
        'all': {'f-score': 0, 'precision': 0, 'recall': 0},
    }

    for f in files:
        if os.path.isfile(path + f) and os.path.getsize(path + f)>0:
            file = open(pathHtml + f, 'r', encoding='utf8', errors="ignore")
            s = file.read()
        else:
            file = open(pathJT + f, 'r', encoding='utf8', errors="ignore")
            s = file.read()

        evaluation = {'f-score': 0, 'precision': 0, 'recall': 0, }

        evaluation = evaluate_file(path + f, pathClean + f)

        results[lg[0]]['f-score'] += evaluation['f-score']
        results[lg[0]]['precision'] += evaluation['precision']
        results[lg[0]]['recall'] += evaluation['recall']

        results['all']['f-score'] += evaluation['f-score']
        results['all']['precision'] += evaluation['precision']
        results['all']['recall'] += evaluation['recall']

    for k in results:
        for i in results[k]:
            results[k][i] = results[k][i] / len(files)

    return results

evaluate["JT"] = evalIntrin(pathJT)
evaluate["JT_langid"] = evalIntrin(pathJT_langid)
evaluate["JT_Truelg"] = evalIntrin(pathJT_Truelg)
