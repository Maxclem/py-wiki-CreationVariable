py-wiki-CreationVariable
========================

J'ai décidé de mettre public ce script que j'ai écrit l'année passé dans le cadre d'un article avorté de ma maitrise. 

Je travaille sur les communauté retrouvé dans Wikipedia, particulièrement la version Anglaise. Dans ce premier projet, je voulais analyse plus en détails le transfert de connaissances entre les articles. Résultat d'un processus social étonnament organisé (particulièrement dans le cas du portail Médicale que j'observais). Le script me permet d'identifier des moments ou l'on retrouve le déplacement d'une section d'un article, souvent transferé au sein d'un autre.
 

À partir de l'API de Wikipedia, de télécharge la version XML de l'historique d'un article de WIkipedia. De la, le script tente d'identifier certains indices permettant de suposer un déplacement de contenu. Principalement, cela est basé sur une différence de volume entre deux version d'un article.

Une fois fait, il me présente visuellement chacun des cas, avec certaines variables qui me permetteront de confirmer s'il y a bel et bien un des cas recherché. Chez ceux-ci, il produira par défaut quelques variables supplémentaires et m'enregistrera le fichier afin que je puisse le transferer vers Excel. Ceci avec le but de réaliser une analyse subséquente grâce à un logiciel d'analyse spécialisé.  

-En dernier lieu, j'use de la commande suivant afin de transferer XML vers EXCEL:
XML vers EXCEL:
	xsltproc docmaitrise.xsl INPUT_FILE.xml > OUTPUT_FILE.ods
	
***NOTE:***

-Je me fais chier avec leur API, puisqu'il y a une limite à la taille du download que je peux faire en une fois (en plus d'une limite sur le nombre de versions maximal d'un article. Je dois donc recomposer un fichier au complet à partir de ces quelques téléchargement. VOIR le fichier nommé: Download_dump
