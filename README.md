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

-Je me fais chier avec leur API, puisqu'il y a une limite à la taille du download que je peux faire en une fois (en plus d'une limite sur le nombre de versions maximal d'un article. Je dois donc recomposer un fichier au complet à partir de ces quelques téléchargement. J'utilise ces commandes afin de le faire:

Afin de télécharger initialement un article:
curl -d "" 'http://en.wikipedia.org/w/index.php?title=Special:Export&pages=ARTICLE_NAME&offset=1&limit=1000&rvprop=ids%7Ctimestamp%7Cuser%7Csize%7Csha1%7Ccomment%7Ccontent&action=submit' > ARTICLE_NAME 1.xml

Afin de télécharger la suite:
curl -d "" 'http://en.wikipedia.org/w/index.php?title=Special:Export&pages=ARTICLE_NAME&offset=TIMESTAMP&limit=1000&rvprop=ids%7Ctimestamp%7Cuser%7Csize%7Csha1%7Ccomment%7Ccontent&action=submit' > ARTICLE_NAMEX.xml

Ensuite, j'utilise les commande BASH suivantes:
POUR Supprimer l'entête (juste pour le premier):
	sed  -i '1,39d' ARTICLE_NAME.xml
POUR Supprimer les deux dernières lignes (juste pour le dernier):
	sed -i 'N;$!P;$!D;$d' ARTICLE_NAME.xml

EXEMPLE:
sed 'N;$!P;$!D;$d' Common_cold1.xml > Common_cold_ALL.xml 
sed '1,39d' Common_cold2.xml > Co_temp.xml 
sed 'N;$!P;$!D;$d' Co_temp.xml >> Common_cold_ALL.xml 
sed '1,39d' Common_cold3.xml > Co_temp.xml 
sed 'N;$!P;$!D;$d' Co_temp.xml >> Common_cold_ALL.xml 
sed '1,39d' Common_cold4.xml > Co_temp.xml 
sed 'N;$!P;$!D;$d' Co_temp.xml >> Common_cold_ALL.xml 
sed '1,39d' Common_cold5.xml >> Common_cold_ALL.xml 

Append:
	cat ARTICLE_NAMEX.xml >> ARTICLE_NAME_ALL.xml
	
	
