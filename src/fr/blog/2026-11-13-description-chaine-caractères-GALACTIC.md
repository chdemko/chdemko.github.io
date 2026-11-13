---
description: Description de chaines de caractères
---

Dans le cadre du projet **GALACTIC**, j’ai développé une fonction Python
pour construire des descriptions de chaînes de caractères sous forme
d’expressions régulières.

À partir d’une liste {math}`l`, la fonction cherche des expressions {math}`e` qui
reconnaissent toutes les chaînes : {math}`l\subseteq L(e)`, noté aussi
{math}`l\sqsubseteq e` par abus de langage. Elle retient les expressions les
plus précises dans une famille définie, c’est-à-dire celles dont le langage
ne peut pas être réduit davantage tout en couvrant les entrées.

L’algorithme recherche des sous-séquences communes, détermine les intervalles
entre leurs caractères, puis compare les langages à l’aide d’automates.
Plusieurs descriptions incomparables peuvent subsister : pour `["abX", "abY"]`
et l'alphabet `ab`, avec au plus un littéral, les résultats sont `.b.` et `a.{2}`.

Les paramètres contrôlent le nombre de littéraux et les intervalles avant,
entre et après ceux-ci. J’ai optimisé les cas du préfixe ou suffixe commun
avec une extrémité opposée illimitée, ainsi que le cas sans littéral, qui
revient à encadrer la longueur des chaînes.


