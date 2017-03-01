SELECT coureurs.nom, coureurs.dossard, coureurs.taille
FROM coureurs
WHERE taille<180

SELECT nom, dossard, equipe 
FROM coureurs
order by equipe;

SELECT coureurs.nom, coureurs.dossard
FROM coureurs, equipes
WHERE  equipe='LavePlusBlanc'

SELECT CONCAT("nom","equipe") FROM coureurs;

UPPER/LOWER 

Question 1.3

SELECT coureurs.dossard, coureurs.nom
FROM coureurs
WHERE coureurs.nom LIKE 'a%'

SELECT coureurs.dossard, coureurs.nom
FROM coureurs
WHERE coureurs.nom LIKE '%er%'

SELECT coureurs.dossard, coureurs.nom
FROM coureurs
WHERE coureurs.nom LIKE '_____'

SELECT coureurs.dossard, coureurs.nom
FROM coureurs
WHERE coureurs.nom LIKE '%a__'

SELECT coureurs.dossard, coureurs.nom
FROM coureurs
WHERE coureurs.nom LIKE '%a__%'
