import os
import statistics

def retrieveValue(directory: str):
    lines = []
    chars = []
    for filename in os.listdir(directory):
        completeName = os.path.join(directory, filename)
        nbLines = 0
        nbChars = 0
        f = open(completeName, "r", encoding="utf-8", errors='ignore')
        for line in f.readlines():
                nbLines += 1
                for char in line:
                    nbChars += 1

        lines.append(nbLines)
        chars.append(nbChars)
    return lines,chars

if __name__ == '__main__':
    bp = retrieveValue("web3_tavRouh/BP/")

    print ("-------Résultats pour les lines bp------")
    print("Le nombre total de lignes est: " + str(sum(bp[0])))
    print("La moyenne : " + str(statistics.mean(bp[0])))
    print("l'écart-type : " + str(statistics.stdev(bp[0])))
    print("-------Résultats pour les caractères bp ------")
    print("Le nombre total de charactères  est: " + str(sum(bp[1])))
    print("La moyenne : " + str(statistics.mean(bp[1])))
    print("l'écart-type : " + str(statistics.stdev(bp[1])))

    jt = retrieveValue("web3_tavRouh/JT/")

    print ("-------Résultats pour les lines jt------")
    print("Le nombre total de lignes est: " + str(sum(jt[0])))
    print("La moyenne : " + str(statistics.mean(jt[0])))
    print("l'écart-type : " + str(statistics.stdev(jt[0])))
    print("-------Résultats pour les caractères jt ------")
    print("Le nombre total de charactères  est: " + str(sum(jt[1])))
    print("La moyenne : " + str(statistics.mean(jt[1])))
    print("l'écart-type : " + str(statistics.stdev(jt[1])))

    jtLangID = retrieveValue("web3_tavRouh/JT_langid/")
    print ("-------Résultats pour les lines jtLangID------")
    print("Le nombre total de lignes est: " + str(sum(jtLangID[0])))
    print("La moyenne : " + str(statistics.mean(jtLangID[0])))
    print("l'écart-type : " + str(statistics.stdev(jtLangID[0])))
    print("-------Résultats pour les caractères jtLangID ------")
    print("Le nombre total de charactères  est: " + str(sum(jtLangID[1])))
    print("La moyenne : " + str(statistics.mean(jtLangID[1])))
    print("l'écart-type : " + str(statistics.stdev(jtLangID[1])))
    
    jtTrueLg = retrieveValue("web3_tavRouh/JT_trueLg/")
    print ("-------Résultats pour les lines jtTrueLg------")
    print("Le nombre total de lignes est: " + str(sum(jtTrueLg[0])))
    print("La moyenne : " + str(statistics.mean(jtTrueLg[0])))
    print("l'écart-type : " + str(statistics.stdev(jtTrueLg[0])))
    print("-------Résultats pour les caractères jtTrueLg ------")
    print("Le nombre total de charactères  est: " + str(sum(jtTrueLg[1])))
    print("La moyenne : " + str(statistics.mean(jtTrueLg[1])))
    print("l'écart-type : " + str(statistics.stdev(jtTrueLg[1])))

    bs = retrieveValue("web3_tavRouh/BS/")
    print ("-------Résultats pour les lines bs------")
    print("Le nombre total de lignes est: " + str(sum(bs[0])))
    print("La moyenne : " + str(statistics.mean(bs[0])))
    print("l'écart-type : " + str(statistics.stdev(bs[0])))
    print("-------Résultats pour les caractères bs ------")
    print("Le nombre total de charactères  est: " + str(sum(bs[1])))
    print("La moyenne : " + str(statistics.mean(bs[1])))
    print("l'écart-type : " + str(statistics.stdev(bs[1])))

    uf = retrieveValue("web3_tavRouh/UF/")
    print ("-------Résultats pour les lines uf------")
    print("Le nombre total de lignes est: " + str(sum(uf[0])))
    print("La moyenne : " + str(statistics.mean(uf[0])))
    print("l'écart-type : " + str(statistics.stdev(uf[0])))
    print("-------Résultats pour les caractères uf ------")
    print("Le nombre total de charactères  est: " + str(sum(uf[1])))
    print("La moyenne : " + str(statistics.mean(uf[1])))
    print("l'écart-type : " + str(statistics.stdev(uf[1])))

    clean = retrieveValue("web3_tavRouh/Corpus_detourage/clean")
    print ("-------Résultats pour les lines clean------")
    print("Le nombre total de lignes est: " + str(sum(clean[0])))
    print("La moyenne : " + str(statistics.mean(clean[0])))
    print("l'écart-type : " + str(statistics.stdev(clean[0])))
    print("-------Résultats pour les caractères clean ------")
    print("Le nombre total de charactères  est: " + str(sum(clean[1])))
    print("La moyenne : " + str(statistics.mean(clean[1])))
    print("l'écart-type : " + str(statistics.stdev(clean[1]))+'\n')

    jtcomparaison = []
    bscomparaison = []
    jtLangIDcomparaison = []
    jtTrueLgcomparaison = []
    ufcomparaison = []


    
    print("---Comparaison avec clean pour les charactères---")
    for i in range(len(clean[1])):
        jtcomparaison.append(abs(jt[1][i] - clean[1][i]))
        bscomparaison.append(abs(bs[1][i] - clean[1][i]))
        jtLangIDcomparaison.append(abs(jtLangID[1][i] - clean[1][i]))
        jtTrueLgcomparaison.append(abs(jtTrueLg[1][i] - clean[1][i]))
        ufcomparaison.append(abs(uf[1][i] - clean[1][i]))

    print("moyenne just text différence " + str(statistics.mean(jtcomparaison)))
    print("ecart type just text différence " + str(statistics.stdev(jtcomparaison))+'\n')

    print("moyenne bs différence " + str(statistics.mean(bscomparaison)))
    print("ecart type bs différence " + str(statistics.stdev(bscomparaison))+'\n')

    print("moyenne jtlangid différence " + str(statistics.mean(jtLangIDcomparaison)))
    print("ecart type jtlangid différence " + str(statistics.stdev(jtLangIDcomparaison))+'\n')

    print("moyenne jt true lg différence " + str(statistics.mean(jtTrueLgcomparaison)))
    print("ecart type jt true lg  différence " + str(statistics.stdev(jtTrueLgcomparaison))+'\n')

    print("moyenne uf différence " + str(statistics.mean(ufcomparaison)))
    print("ecart type uf différence " + str(statistics.stdev(ufcomparaison))+'\n')
