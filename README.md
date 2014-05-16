py-wiki-CreationVariable
========================

J'ai décidé de mettre public ce script que j'ai écrit l'année passé dans le cadre d'un article avorté de ma maitrise. Il s'agit du premier programme que j'ai écris en python, langage que j'ai appris pour l'occasion. En fait, c'est le seul langage que j'ai appris jusqu'à maintenant (bien que je me suis frotté un peu au XSLT et HTML). De ce fait, je suppose la profonde "non-ergonomie" de celui-ci, bien qu'il fasse bien ce pourquoi il est écrit.

En gros, je travaille sur les communautés sociales retrouvées dans Wikipedia, particulièrement au sein de la version Anglaise. Dans ce premier projet, je voulais analyser plus en détails le transfert de connaissances entre différents articles. Résultat d'un processus social étonnament organisé (particulièrement dans le cas du portail Médicale que j'observais), je voulais observer les normes autorisant ce genre d'action sans que cela passe pour du vandalisme. Le script me permet d'identifier des moments ou l'on retrouve le déplacement d'une section d'un article, souvent pour fonder ou compléter un autre.
 

À partir de l'API de Wikipedia, je télécharge la version XML de l'historique d'un article de WIkipedia. De la, le script tente d'identifier certains indices permettant de suposer un déplacement de contenu. Principalement, cela est basé sur une différence de volume entre deux version d'un article.

Une fois fait, il me présente visuellement chacun des cas, avec certaines variables qui me permetteront de confirmer s'il y a bel et bien un des cas recherchés. Il standardisera l'arborescence et les attributs du fichier afin de faciliter mon travail futur et m'enregistrera la nouvelle version du fichier. À fin d'analyse, le fichier: Stats_supplementaire permet de créer des variables supplémentaires.



-En dernier lieu, j'use de la commande suivante afin de transferer le document XML vers EXCEL:
Ceci avec le but de réaliser une analyse subséquente grâce à un logiciel d'analyse spécialisé. XML vers EXCEL:
	xsltproc docmaitrise.xsl INPUT_FILE.xml > OUTPUT_FILE.ods
	
***NOTE:***

-Je me fais chier avec leur API, puisqu'il y a une limite à la taille du download que je peux faire en une fois (en plus d'une limite sur le nombre de versions maximal d'un article. Je dois donc recomposer un fichier au complet à partir de ces quelques téléchargement. VOIR le fichier nommé: Download_dump

