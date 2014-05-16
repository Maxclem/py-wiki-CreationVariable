from sys import argv
from datetime import datetime, date, time
try:
    import xml.etree.cElementTree as ET
    print "run on cElementTree"
except ImportError:
    import xml.etree.ElementTree as ET
    print "run on simple ElementTree"

script, from_xml, to_xml= argv

tree = ET.parse(from_xml)
root = tree.getroot()

##Stat suplementaire pour excel##
#Bytes et timestamps 50 avant et 50 apres le cas Chuthlu#

for stat in tree.iter('revision'):
    for idChuthlu in stat.findall('comment'):
        #Ceci est le code permettant de choisir directement un attribut#
        if idChuthlu.attrib['expuls'] == 'in' or 'out' or 'self':
            #Selection d'un cas Chuthlu#
            for diff_size in stat.iter('text'):
                dif = int(diff_size.attrib['bytes'])
            for diff_time in stat.iter('timestamp'):
                dift = diff_time.attrib['Time']
            #Creation variables#
            for diff_rev in tree.iter('revision'):
                #Selection de 50 avants#
                if diff_rev.attrib['decompte'] == int(stat.attrib['decompte'])- 50:
                    #Size#
                    for diff_size_avant in diff_rev.findall('text'):
                        rerer = int(diff_size_avant.attrib['bytes'])
                        diff_size.set('bytes_50_avant', str(rerer))
                    #Time#
                    for diff_time_avant in diff_rev.findall('timestamp'):
                        retime = diff_time_avant.attrib['Time']
                        diff_time.set('Time_50_avant', retime)
                #Selection de 50 apres#        
                if diff_rev.attrib['decompte'] == stat.attrib['decompte']+ 50:
                    #Size
                    for diff_size_apres in diff_rev.findall('text'):
                        rerer = int(diff_size_apres.attrib['bytes'])
                        diff_size.set('bytes_50_apres', str(rerer))
                    #Time
                    for diff_time_apres in diff_rev.findall('timestamp'):
                        retime = diff_time_apres.attrib['Time']
                        diff_time.set('Time_50_apres', retime)                                


tree.write(to_xml)
