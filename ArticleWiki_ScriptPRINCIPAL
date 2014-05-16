print "Starting script ..."

from sys import argv
from datetime import datetime, date, time

try:
  from lxml import etree
  print("running with lxml.etree")
except ImportError:
  try:
    # Python 2.5
    import xml.etree.cElementTree as etree
    print("running with cElementTree on Python 2.5+")
  except ImportError:
    try:
      # Python 2.5
      import xml.etree.ElementTree as etree
      print("running with ElementTree on Python 2.5+")
    except ImportError:
      try:
        # normal cElementTree install
        import cElementTree as etree
        print("running with cElementTree")
      except ImportError:
        try:
          # normal ElementTree install
          import elementtree.ElementTree as etree
          print("running with ElementTree")
        except ImportError:
          print("Failed to import ElementTree from any known place")


#Arguments d'activation du script#         
script, from_xml, to_xml= argv


parser = etree.XMLParser(remove_blank_text=True)
tree = etree.parse(from_xml, parser)

#tree = etree.parse(from_xml, 'w')
root = tree.getroot()

###FORMAT DES TAGS D'ELEMENTS###

def rename_elements():      
    for mediawiki in tree.iter('{http://www.mediawiki.org/xml/export-0.8/}mediawiki'):
        mediawiki.tag = "mediawiki"      
    for page in tree.iter('{http://www.mediawiki.org/xml/export-0.8/}page'):
        page.tag = "page"       
    for revision in tree.iter('{http://www.mediawiki.org/xml/export-0.8/}revision'):
        revision.tag = "revision"       
    for id in tree.iter('{http://www.mediawiki.org/xml/export-0.8/}id'):
        id.tag = "id"
    for parentid in tree.iter('{http://www.mediawiki.org/xml/export-0.8/}parentid'):
        parentid.tag = "parentid"       
    for timestamp in tree.iter('{http://www.mediawiki.org/xml/export-0.8/}timestamp'):
        timestamp.tag = "timestamp"      
    for contributor in tree.iter('{http://www.mediawiki.org/xml/export-0.8/}contributor'):
        contributor.tag = "contributor"       
    for username in tree.iter('{http://www.mediawiki.org/xml/export-0.8/}username'):
        username.tag = "username"
    for ip in tree.iter('{http://www.mediawiki.org/xml/export-0.8/}ip'):
        ip.tag = "ip"        
    for comment in tree.iter('{http://www.mediawiki.org/xml/export-0.8/}comment'):
        comment.tag = "comment"       
    for text in tree.iter('{http://www.mediawiki.org/xml/export-0.8/}text'):
        text.tag = "text"       
    for sha1 in tree.iter('{http://www.mediawiki.org/xml/export-0.8/}sha1'):
        sha1.tag = "sha1"        
    for model in tree.iter('{http://www.mediawiki.org/xml/export-0.8/}model'):
        model.tag = "model"
        
#Appel de la fonction specifique. Reforme les TAG#
rename_elements()

######################################################
####################INTRODUCTION######################
######################################################

###Pour utiliser les donnees, je dois faire trois etapes###
##1.Utiliser la commande d'importation: 
##curl -d "" 'http://en.wikipedia.org/w/index.php?title=Special:Export&pages=NOM_ARTICLE&offset=1&limit=1000&rvprop=ids%7Ctimestamp%7Cuser%7Csize%7Csha1%7Ccomment%7Ccontent&action=submit' > NOM_ARTICLE.xml
##2.Utiliser ce script.
##3.Utiliser la commande pour mettre en spreadsheet:
##xsltproc docmaitrise.xsl NOM_ARTICLE.xml > EXEMPLE.html

##################Projet a venir####################
##Supprimer les elements inutiles
##Rafiner la selection du vocabulaire
##Assembler -API_Wiki -Script_Python -Format_XSLT
##Print de chaque "yes", avec les 5 precedantes, et raw_input stoquer dans nouvelle variable pour la validation manuelle.
##Verifier si on commence pour de vrai a la premiere ligne
##Faire les stats sur Chuthlu
##Clean des donnees, pour les aberantes et apres 2013

######URGENT######
#Transformer la creation de variables en fonction, ou objet (cela permet de facilement suspendre ses objects
#Completer cette meme creation de variables

####################################################
###################CORPS_DU_SCRIPT##################
####################################################

#Fusion de User et IP#
for contributor in tree.iter("contributor"):
    for username in contributor.xpath("child::username"):
        contributor.set('username', username.text)        
    for userip in contributor.xpath("child::ip"):
        contributor.set('username', userip.text)

###COMPTEUR d'edits et temps###
##Compteurs##
compteur_edits = 1
nmb_edits = []
nmb_jours = []
size_compte = 1
size_ID = []

for rev_all in tree.iter('revision'):
    #Numeroter les edits#
    rev_all.set('decompte', str(compteur_edits))
    nmb_edits.append(compteur_edits)
    compteur_edits += 1 
    #Attrib Time pour tous#
    for decompte_t in rev_all.xpath('child::timestamp'):
        #Temps de la revision#
        tr = datetime.strptime(decompte_t.text, "%Y-%m-%dT%H:%M:%SZ")
        nmb_jours.append(tr)
        decompte_t.set('Time',str(tr))    
        ##ARRETER SELCTION A 01-01-2013##
        temps_max = "2013-01-01 00:00:00"
        strp_temps_max = datetime.strptime(temps_max, "%Y-%m-%d %H:%M:%S")
        if tr > strp_temps_max:
            rev_all.getparent().remove(rev_all)
            del nmb_edits[-1]
            del nmb_jours[-1]
        #Mise en place du temps 0#
        temps_zero = nmb_jours[0]
        #Temps depuis la fondation# 
        diff_time = tr - temps_zero
        decompte_t.set('Since',str(diff_time))             
    ##Calcule du volume en bytes##    
    for revSize in rev_all.xpath('child::text'):
        #Suppression vandalisme#
        if int(rev_all.attrib['decompte']) > 50:
            if int(revSize.attrib['bytes']) < 200:
                rev_all.getparent().remove(rev_all)
        #Diff entre revision#        
        size_unique = revSize.attrib['bytes']
        size_ID.append(size_unique)
        if size_compte != 1:
            size_prec = size_ID[int(rev_all.attrib['decompte']) - 2]
            size_act = size_ID[int(rev_all.attrib['decompte']) - 1]
            diff = int(size_act) - int(size_prec)
            revSize.set('diff', str(diff))           
        size_compte += 1
    
##COMMENT OBTENIR TEMPS QUE CELA PREND POUR ROULER LE PROGRAMME##
    
###DICO SUR LES EXPULSIONS###
dico_inclu = ['merg','fork','split', 'creat', 'to [[', 'from [[', 'subpage', 'subarticle', 'sub-page', 'sub-article', 'sub page', 'sub article']        
dico_exclu = ['remove','removed','removing','undid revision','robot:','reverted to','reverted edits']

##Trouver mots##
for expulsion in tree.iter("comment"):
    expulsion.set('expuls', '-')
    expulsion.text = expulsion.text.lower()
    #Pre-selection#
    move = "mov"
    t = expulsion.find(move)    
    if t >= 0:
        expulsion.set('expuls', 'Chuthlu')
    #Selection negative#    
    for item_e in dico_exclu:
        text_false = expulsion.text.find(item_e)
        if text_false >= 0:
            expulsion.set('expuls', 'No')
    #Selection positive#        
    for item_i in dico_inclu:    
        text_true = expulsion.text.find(item_i)
        if text_true >= 0:
            expulsion.set('expuls', 'Chuthlu')           


###Netoyage pour augmenter la specificite###
###Fait a partir des resultats du dico###

nbr_selection = 0
for select_rev in tree.iter('revision'):
    for Chuth in select_rev.xpath('child::comment'):
        #Selection de Chuthlu!!!#
        if Chuth.attrib['expuls'] == 'Chuthlu':
            #Print des infos de cette revision#
            print "\n\nInfos generales-->", "\n\nNumero chronologique:", select_rev.attrib['decompte']
            for x in select_rev.xpath('child::timestamp'):
                print "Date:", x.attrib['Time']
            for x in select_rev.xpath('child::contributor'):
                print "Contributeur:", x.attrib['username']
            #Precedante#    
            taille_prec = size_ID[int(select_rev.attrib['decompte']) - 2]
            print "\n\nTaille de l'edition precedante:", taille_prec, "bytes." 
            #Celle-ci#
            for taille_act in select_rev.xpath('child::text'):
                print "Taille de l'edition:", taille_act.attrib['bytes'], "bytes"                  
            #Diff#
            print "Difference entre tailles d'editions:", taille_act.attrib['diff']    
            for x in select_rev.xpath('child::id'):
                dico_id = ["http://en.wikipedia.org/w/index.php?title=ARTICLE&diff=prev&oldid=", x.text]
                print "Visualisation diff:", "".join(dico_id)
            
            #Comment en tant que tel#    
            print "\n\nComment ---->", Chuth.text
            print "Est-ce que l'on conserve cette selection? \n\t- in (d'un autre article); \n\t- out (vers autre article); \n\t- self (vers Talk); \n\t- n (No)"
            decision = raw_input("Reponse:\n>")
            
            #Conserve la selection#
            if decision == "in":
                Chuth.set('expuls', 'in')
                print "Attrib set as:", Chuth.attrib
                print "Classe comme matiere entrante, maintenant la prochaine:"
                nbr_selection += 1
            elif decision == "out":
                Chuth.set('expuls', 'out')
                nbr_selection += 1
                print "Attrib set as:", Chuth.attrib
                print "Classe comme matiere sortante, maintenant la prochaine:"
            elif decision == "self":
                Chuth.set('expuls', 'self')
                nbr_selection += 1
                print "Attrib set as:", Chuth.attrib
                print "Classe comme echange a meme l'article, maintenant la prochaine:"
    
            #Annule la selection#    
            elif decision == "n":
                Chuth.set('expuls', 'No')
                print "Attrib set as:", Chuth.attrib
                print "That selection have been expelled. Here's the next one:"
                
            else:
                print "!" * 50
                print "Conserve le numero d'edit car il va falloir que tu verifie qu'il n'y a pas d'erreurs"  
                print "Fait attention a ce que tu ecris!"

##Correction erreur decompte: du a l'expulsion par vandalisme##
compteur_edits = 1
nmb_edits = []
for rev_all in tree.iter('revision'):
    #Numeroter les edits#
    rev_all.set('decompte', str(compteur_edits))
    nmb_edits.append(compteur_edits)
    compteur_edits += 1 
    
###Impression d'informations generales###

print "\n\n\n\n\n\n\nCOMPLETE"
print "Voici les stats generales de cet article:"
print "L'article commence le", temps_zero
print "Le dernier du document est le", nmb_jours[-1]
print nmb_edits[-1], "differents edits"
print nbr_selection, "avec deplacement" 

        
print """
            Fin du script. Si tu veux exporter vers .xls ou .html
            Tu peux utiliser cette ligne de commande dans un terminal: 
            xsltproc FILE.xsl INPUT_ARTICLE.xml > OUTPUT_NAME.html
            """
print "Sauvegarde sous le nom:", to_xml
          
###PRINT DES TRANSFORMATIONS###
        
##Print un iter d'element specifique##        
#for elem in tree.iter(tag="timestamp"):
#    print elem.tag, elem.attrib, elem.text
     
##Print l'ensemble du tree##    
#for elem in tree.iter():
    #print elem.tag, elem.attrib
    #print elem.tag, elem.attrib, elem.text    

###OUTPUT###
      
##Pour enregistrer a meme le document (JAMAIS TENTER):
#tree.write(sys.stout)  

##Exporter les resultats vers le fichier x ## 
tree.write(to_xml)

    
