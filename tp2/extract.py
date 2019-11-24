import requests

valeurId = 30000
valeurIdend = 30500
save_path_tournois = 'html/tournois/'
save_path_stats = 'html/stats/'
save_path_resultats = 'html/resultats/'
save_path_participants = 'html/participants/'

tournois = 'http://echecs.asso.fr/FicheTournoi.aspx?Ref='
tournois_id ='http://echecs.asso.fr/Resultats.aspx?URL=Tournois/Id/'

for id in range(valeurId,valeurIdend):

    response_tournois = requests.get(tournois+str(id))
    html_tournois = open(save_path_tournois+str(id)+".html","w")
    html_tournois.write(str(response_tournois.content))
    html_tournois.close()

    response_statistiques = requests.get(tournois_id+ str(id) + "/" + str(id) + "&Action=Stats")
    html_statistiques = open(save_path_stats+str(id)+".html","w")
    html_statistiques.write(str(response_statistiques.content))
    html_statistiques.close()

    response_resultats = requests.get(tournois_id+ str(id) + "/" + str(id) + "&Action=Ga")
    html_resultats = open(save_path_resultats + str(id) + ".html", "w")
    html_resultats.write(str(response_resultats.content))
    html_resultats.close()

    response_participants = requests.get(tournois_id+ str(id) + "/" + str(id) + "&Action=Ls")
    html_participants = open(save_path_participants + str(id) + ".html", "w")
    html_participants.write(str(response_participants.content))
    html_participants.close()
