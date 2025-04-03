première version scripts.py essaye de scrapper annuaire.sante.fr et de fonctionner par comparaison avec l'existant

> Repertoire Sante

 voir date de dernière maj des données : https://annuaire.sante.fr/web/site-pro/extractions-publiques
se rendre sur : : https://service.annuaire.sante.fr/annuaire-santewebservices/V300/services/extraction/PS_LibreAcces
télécharger le fichier qui servira de base : PS_LibreAcces_Personne_activite_202504020841.txt 
ensuite, le placer dans le répertoire data, en le renommant 1.txt et y ajouter le nouveau fichier du jour qu'on renommera 2.txt. 
ensuite lancer diffExtract.py puis Objet.py et enfin aller récupérer le résultat dans le excel. (chercher code profession 93, libéral par exemple)

> Pages jaunes
Lancer pages jaunes.py pour récupérer les psychologues de Lorraine. Renommer le fichier html obtenu "2.html" et lancer "comparerJ1J2.py pour obtenir la différence dans un excel.

> Projet web
lancer server.py, se rendre a l'adresse locale souvent 127.0.0.1:5000 et importer les fichiers 1 et 2. Télécharger le résultat obtenu. 
