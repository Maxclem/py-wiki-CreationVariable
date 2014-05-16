from sys import argv
from datetime import datetime, date, time
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

script, from_xml, numero = argv

tree = ET.ElementTree(file=from_xml)
root = tree.getroot()


###FORMAT DES TAGS D'ELEMENTS###

def rename_elements():            
    for revision in tree.iter('{http://www.mediawiki.org/xml/export-0.8/}revision'):
        revision.tag = "revision"       
    for id in tree.iter('{http://www.mediawiki.org/xml/export-0.8/}id'):
        id.tag = "id"
    for parentid in tree.iter('{http://www.mediawiki.org/xml/export-0.8/}parentid'):
        parentid.tag = "parentid"       
    for timestamp in tree.iter('{http://www.mediawiki.org/xml/export-0.8/}timestamp'):
        timestamp.tag = "timestamp"      
        
#Appel de la fonction specifique. Reforme les TAG#
rename_elements()

###Corps du script###
##Compteur d'edits##
compteur_edits = 1
nmb_edits = []

for indic in tree.iter('revision'):
    indic.set('decompte', compteur_edits)
    nmb_edits.append(compteur_edits)
    compteur_edits += 1
    
###Variable indiquant le temps absolue###
compteur_jours = 0
nmb_jours = []
nmb_jours_non_format = []

#Date d'origine de l'article#
for revTime in tree.iter('revision'):
    #Va chercher le premier edit#
    if revTime.attrib['decompte'] == 1:
        #Lui applique une transfo pour lire le temps#
        for temps_from_0 in revTime.iter('timestamp'):
            tm = datetime.strptime(temps_from_0.text, "%Y-%m-%dT%H:%M:%SZ")
            temps_from_0.set('Time', tm)
            #Date initiale#
            Time= temps_from_0.attrib['Time']
    
    #Attrib Time pour tous#
    for decompte_t in revTime.iter('timestamp'):
        tr = datetime.strptime(decompte_t.text, "%Y-%m-%dT%H:%M:%SZ")
        nmb_jours.append(tr)
        nmb_jours_non_format.append(decompte_t.text)
        decompte_t.set('Time',str(tr))
        diff_time = tr - tm
        decompte_t.set('Since', str(diff_time))


#######################################
###Si un autre export est necessaire###
dernier_time = nmb_jours_non_format[-1]
article_name = from_xml[:-5]

#Si taille maximal est atteinte:#
if nmb_edits[-1] == 1000:
    print "\n\n\nIl y a plus de 1000 edits, doit donc utiliser offset avec:", dernier_time
    print "\n\tUtilise la commande suivante:"
    #Permet d'associer les different element pour que la commande curl fonctionne#    
    lists = ["curl -d \"\" 'http://en.wikipedia.org/w/index.php?title=Special:Export&pages=", article_name, "&offset=", dernier_time, "&limit=5000&rvprop=ids%7Ctimestamp%7Cuser%7Csize%7Csha1%7Ccomment%7Ccontent&action=submit' > ", article_name, numero, ".xml\n\n\n"]       
    print "".join(lists)

#Si la fin est reellement atteinte#    
else:
    print "\n\n\nTout le monde descent, il y a ", nmb_edits[-1], "edits"
    print "Pour rejoindre les fichiers ensemble:\t","cat INPUT1.xml INPUT2.xml >> OUTPUT.xml"
    print "\n\n\nCeci etait la fin de cette article, passez au script suivant: parsingWiki.py\n\n\n"
 
