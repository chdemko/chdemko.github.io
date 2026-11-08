---
description: Soutenance de thèse de Salah
---

# 🗓️ 2022-08-30 — Analyse de séquences avec **GALACTIC**

Salah Eddine Boukhetta a soutenu sa thèse, *Approche générique combinant
l'analyse formelle de concepts et l'extraction de motifs*, le 30 août 2022.
Voici la vidéo de sa présentation et un résumé.

<div style="position: relative; overflow: hidden; width: 100%;
            padding-top: 56.25%;">
  <iframe
    src="https://videos.univ-lr.fr/video/2469-these-de-salah-eddine-boukhetta/?is_iframe=true"
    style="position: absolute; top: 0; left: 0;
           width: 100%; height: 100%;"
    allowfullscreen
  >Votre navigateur ne prend pas en charge les iframes.</iframe>
</div>

Les données séquentielles sont utilisées dans de nombreux domaines pour
analyser et extraire des connaissances. Une séquence est une suite d'éléments
ordonnés, comme une trajectoire ou une succession d'achats. On distingue les
séquences simples, temporelles et d'intervalles.

L'extraction de motifs séquentiels vise à trouver des motifs fréquents dans un
ensemble de séquences, généralement des sous-séquences communes. Un motif est
fréquent lorsqu'il est partagé par un nombre suffisamment représentatif
d'objets. Son support mesure la proportion de données qui le partagent.

De nombreux algorithmes ont été proposés pour extraire ces motifs. La puissance
de calcul accrue a accéléré leur extraction, mais le grand nombre de motifs
produits rend leur lecture et leur interprétation difficiles : c'est le
« déluge de motifs ». Une première approche consiste à ne conserver que les
motifs fermés, qui portent la même information. Leur ensemble peut être
organisé en treillis, structure à la base de l'analyse formelle de concepts
(**AFC**), domaine consacré à l'identification de relations dans les données.

L'AFC classique traite des objets décrits par des ensembles d'attributs,
c'est-à-dire des données binaires. Les structures de motifs et la navigation
conceptuelle abstraite l'étendent à des données complexes telles que les
séquences. Inspiré des structures de motifs, l'algorithme
NᴇxᴛPʀɪᴏʀɪᴛʏCᴏɴᴄᴇᴘᴛ propose une extraction générique pour les données
hétérogènes et complexes, fondée sur des descriptions par prédicats monadiques.
Il permet également d'affiner un ensemble d'objets grâce à des stratégies
d'exploration choisies par l'utilisateur, afin de limiter le nombre de motifs.

La plateforme **GALACTIC** implémente cet algorithme et propose un écosystème
d'extensions pour le traitement de données. Cette thèse étudie l'analyse de
données séquentielles avec **GALACTIC**. Elle propose des descriptions et
stratégies adaptées aux séquences simples, temporelles et d'intervalles. Les
descriptions reposent sur les sous-séquences communes maximales et sur des
descriptions propres à chaque type. Une stratégie naïve génère tous les
concepts ; des stratégies plus élaborées réduisent la taille du treillis.
Des mesures de qualité non supervisées permettent de comparer les treillis
obtenus. Une analyse qualitative et quantitative sur des jeux de données
réels et synthétiques montre l'efficacité de l'approche.
