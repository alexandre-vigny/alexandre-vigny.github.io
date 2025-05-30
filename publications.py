# advisors
luc =       "<a href=http://pages.saclay.inria.fr/luc.segoufin/>Luc Segoufin</a>"
arnaud =    "<a href=https://webusers.imj-prg.fr/~arnaud.durand/>Arnaud Durand</a>"
mikolaj =   "<a href=https://www.mimuw.edu.pl/~bojan/>Mikołaj Bojańczyk</a>"
szymon =    "<a href=https://www.mimuw.edu.pl/~szymtor/>Szymon Toruńczyk</a>"
sebi =      "<a href=https://www.uni-bremen.de/en/theorie/team/profiles/prof-dr-sebastian-siebertz>Sebastian Siebertz</a>"

# co-authors
nicoleSchw= "<a href=https://www.informatik.hu-berlin.de/de/forschung/gebiete/loginf/thi/schweikardt/>Nicole Schweikardt</a>"
michal=     "<a href=https://www.mimuw.edu.pl/~mp248287/>Michał Pilipczuk</a>"
yiting=     "<a href=https://dblp.org/pid/234/5037.html>Yiting Jiang</a>"
patrice=    "<a href=http://madezhi.free.fr/>Patrice Ossona de Mendez</a>"
giannos=    "<a href=https://www.lirmm.fr/~gstamoulis/>Giannos Stamoulis</a>"
dimitrios=  "<a href=https://www.lirmm.fr/~thilikosto/>Dimitrios M. Thilikos</a>"
jan=        "<a href=https://www.ac.tuwien.ac.at/people/dreier/>Jan Dreier</a>"
amer=       "<a href=https://www.aub.edu.lb/pages/profile.aspx?MemberId=aa368>Amer E. Mouawad</a>"

# Bremen
teamBremen= "<a href=https://www.uni-bremen.de/en/theorie/team>team</a>"
nicoleSchi= "<a href=https://www.uni-bremen.de/en/theorie/team>Nicole Schirrmacher</a>"
mario =     "<a href=https://www.uni-bremen.de/en/theorie/team>Mario Grobler</a>"
niko=       "<a href=https://user.informatik.uni-bremen.de/nikmaehl/>Nikolas Mählmann</a>"
alex=       "<a href=https://www.uni-bremen.de/en/cslog/team/alexander-lindermayr>Alexander Lindermayr</a>"
ozan=       "<a href=https://dblp.uni-trier.de/pid/307/5051.html>Ozan Heydt</a>"
simeon=     "<a href=https://dblp.uni-trier.de/pid/280/3295.html>Simeon Kublenz</a>"

# Clermont
mamadou =   "<a href=https://perso.isima.fr/~makante/>Mamadou Kanté</a>"
jona =      "Jona Dirks"

# TODO
#nothing !

# Initialization list of publi as dictionary
publi = []

# List of publi

EDDC={
   "link":"<a href=\"https://arxiv.org/abs/2504.21675\"> Elimination Distance to Dominated Clusters.</a>",
   "authors":"With "+nicoleSchi+" and "+sebi+".",
   "tag":"Graph Combinatorics"
}
publi.append(EDDC)



IsRecDAGs={
   "link":"<a href=\"https://arxiv.org/abs/2504.10671\"> Token Sliding Reconfiguration on DAGs.</a>",
   "authors":"With "+jona+".",
   "tag":"Graph Combinatorics"
}
publi.append(IsRecDAGs)

#    "link":"<a href=\"https://arxiv.org/abs/1903.00505\"> Parameterized Distributed Complexity Theory: A logical approach.</a>",
#    "authors":"With "+sebi+".",
#    "tag":"Distributed computing"
# }
# publi.append(ParaDistrib)


FsttcsSurvey ={
   "link":"<a href=\"https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FSTTCS.2024.2\"> Advances in Algorithmic Meta Theorems.</a> (Invited Paper)",
   "authors":"With "+sebi+".",
   "conf":"FSTTCS 2024",
   "tag":"Graphs and Logic"
}
publi.append(FsttcsSurvey)

DisPath =  { 
   "link":"<a href=\"Papers/MC-disjoint-path_LICS-2024.pdf\"> Model Checking Disjoint-Paths Logic on Topological-Minor-Free Graph Classes.</a>",
   "authors":"With "+nicoleSchi+", "+sebi+", "+giannos+" and "+dimitrios+".",
   "conf":"<a href=\"https://dl.acm.org/doi/10.1145/3661814.3662089\">LICS 2024</a>",
   "tag":"Graphs and Logic"
}
publi.append(DisPath)


DistribDom =  { 
   "link":"<a href=\"Papers/Distrib-domination-sparse-graph-classes_EJC-2023.pdf\"> Distributed Domination on Sparse Graph Classes.</a>",
   "journal":"<a href=\"https://www.sciencedirect.com/science/article/abs/pii/S0195669823000902\">Eur. J. Comb</a>",
   "authors":"With "+ozan+", "+simeon+", "+patrice+" and "+sebi+".",
   "tag":"Distributed computing",
}
publi.append(DistribDom)



MonaStabl =  { 
   "link":"<a href=\"https://doi.org/10.4230/LIPIcs.ISAAC.2022.11\"> Combinatorial and Algorithmic Aspects of Monadic Stability.</a>",
   "authors":"With "+jan+", "+niko+", "+amer+" and "+sebi+".",
   "conf":"ISAAC 2022",
   "tag":"Graph Combinatorics"
}
publi.append(MonaStabl)


MCSepLogic =  { 
   "link":"<a href=\"https://drops.dagstuhl.de/opus/volltexte/2022/16443/\"> Algorithms and data structures for first-order logic with connectivity under vertex failures.</a>",
   "authors":"With "+michal+", "+nicoleSchi+", "+sebi+" and "+szymon+".",
   "conf":"ICALP 2022",
   "tag":"Graphs and Logic",
   "top":True
}
publi.append(MCSepLogic)



FoConnDef =  { 
   "link":"<a href=\"Papers/FO-Conn_Schirrmacher-Siebertz-Vigny_TOCL-2023.pdf\"> First-Order Logic with Connectivity Operators.</a>",
   "conf":"<a href=\"https://drops.dagstuhl.de/opus/volltexte/2022/15754/\"> CSL 2022</a>",
   "journal":"<a href=\"https://dl.acm.org/doi/abs/10.1145/3595922\">ACM Trans. Cpomput. Log</a>",
   "authors":"With "+nicoleSchi+" and "+sebi+".",
   "tag":"Graphs and Logic",
   "top":True
}
publi.append(FoConnDef)


LocalDomPla =  { 
   "link":"<a href=\"https://arxiv.org/abs/2111.14506\"> Local planar domination revisited.</a>",
   "authors":"With "+ozan+" and "+sebi+".",
   "conf":"<a href=\"https://dl.acm.org/doi/abs/10.1007/978-3-031-09993-9_9\">SIROCCO 2022</a>",
   "tag":"Distributed computing"
}
publi.append(LocalDomPla)

Discrepancy =  {
   "link":"<a href=\"https://doi.org/10.1016/j.jctb.2024.06.001\"> Discrepancy and Sparsity.</a>",
   # "arxiv":"<a href=\"https://arxiv.org/abs/2105.03693\"> Discrepancy and Sparsity.</a>",
   "authors":"With "+mario+", "+yiting+", "+patrice+" and "+sebi+".",
   "journal":"<a href=\"https://doi.org/10.1016/j.jctb.2024.06.001\">J. Comb. Theory B</a>",
   "tag":"Graph Combinatorics",
   "dateJournal":2024
}
publi.append(Discrepancy)




LocalDomBE =  { 
   "link":"<a href=\"https://arxiv.org/abs/2012.02701\"> Constant Round Distributed Domination on Graph Classes with Bounded Expansion.</a>",
   "authors":"With "+simeon+" and "+sebi+".",
   "conf":"<a href=\"https://dl.acm.org/doi/abs/10.1007/978-3-030-79527-6_19\">SIROCCO 2021</a>",
   "tag":"Distributed computing"
}
publi.append(LocalDomBE)


RecBack =  { 
   "link":"<a href=\"https://drops.dagstuhl.de/opus/volltexte/2021/14513/\"> Recursive Backdoors for SAT.</a>",
   "authors":"With "+niko+" and "+sebi+".",
   "conf":"MFCS 2021",
   "tag":"Graph Combinatorics"
   # TODO Add video ?
}
publi.append(RecBack)


ElimDist =  { 
   "link":"<a href=\"https://fi.episciences.org/paper/view/id/13665\"> Elimination Distance to Bounded Degree on Planar Graphs.</a>",
   "authors":"With "+alex+" and "+sebi+".",
   "conf":"<a href=\"https://drops.dagstuhl.de/opus/volltexte/2020/12755/\">MFCS 2020</a>",
   # "long":"<a href = \"https://arxiv.org/abs/2007.02413\"> Arxiv</a> long version.",
   "journal":"<a href=\"https://fi.episciences.org/paper/view/id/13665\">Fundamenta Informaticae</a>",
   # "journal":"<a href=\"https://doi.org/10.3233/FI-242175\">Fundamenta Informaticae</a>",
   "video":" <a href= \"https://www.youtube.com/watch?v=oTKueyUsNwY\">Video presentation.</a>",
   "tag":"Graph Combinatorics",
   "top":True,
   "dateConf":2020,
   "dateJournal":2024
}
publi.append(ElimDist)

ParaDistrib =  { 
   "link":"<a href=\"https://arxiv.org/abs/1903.00505\"> Parameterized Distributed Complexity Theory: A logical approach.</a>",
   "authors":"With "+sebi+".",
   "tag":"Distributed computing"
}
publi.append(ParaDistrib)


SoloUpdate =  { 
   "link":"<a href=\"https://arxiv.org/abs/2010.02982\"> Dynamic Query Evaluation Over Structures with Low Degree.</a>",
   "tag":"Query Enumeration"
}
publi.append(SoloUpdate)


EnumNoWD =  {    
   "link":"<a href=\"Papers/Schweikardt-Segoufin-Vigny_enum-fo-nowhere-dense_JACM_2022.pdf\"> Enumeration for FO Queries over Nowhere Dense Graphs.</a>",
   "authors":"With "+nicoleSchw+" and "+luc+".",
   "journal":"<a href=\"https://dl.acm.org/doi/abs/10.1145/3517035\">J. ACM</a>",
   "conf":"PODS 2018",
   "tag":"Query Enumeration",
   "top":True
}
publi.append(EnumNoWD)


EnumICDT = {
   "link":"<a href=\"Papers/Segoufin-Vigny_Local-bounded-expansion_2017.pdf\"> Constant Delay Enumeration for FO Queries over Databases with Local Bounded Expansion.</a>",
   "authors":"With "+luc+".",
   "conf":"ICDT 2017",
   "tag":"Query Enumeration",
}
publi.append(EnumICDT)



def readmd (pub):
   res= ""
   # Write the name and link
   res+= "* "+pub["link"]+"\n"
   # write coauthors if any
   if "authors" in pub:
      res+=pub["authors"]
   # Write where it was presented
   if "conf" in pub and "journal" in pub:
      res+= " Presented at "+pub["conf"]+" and published in "+pub["journal"]+"."
   elif "journal" in pub:
      if pub["journal"][-1]==".":
         res+= " Published in "+pub["journal"]
      else:
         res+= " Published in "+pub["journal"]+"."
   elif "conf" in pub:
      res+= " Presented at "+pub["conf"]+"."
   else:
      res+= " Only on arXiv."
   res+="\n"
   # Possibly add long version or a video
   if "long" in pub:
      res+=pub["long"]
   if "video" in pub:
      res+=pub["video"]
   if "long" in pub or "video" in pub:
      res+="\n"
   # return the string
   return(res)
#End of Read fonction

def readhtml (pub,type=""):
   res= ""
   box=""  # color of publi
   if "journal" in pub:
      box = "<mark class=\"journal\">&#9632;</mark>"
   elif "conf" in pub:
      box = "<mark class=\"conf\">&#9632;</mark>"
   elif "book" in pub:
      box = "<mark class=\"book\">&#9632;</mark>"
   else:
      box = "<mark class=\"arxiv\">&#9632;</mark>"
   if type != "": #if type is specified, use this instead
         box = "<mark class="+type+">&#9632;</mark>"


   # Write the name and link
   res+= "<li>"+box+pub["link"]+"<br>"
   # write coauthors if any
   if "authors" in pub:
      res+=pub["authors"]
   
   # Write where it was presented
   if "conf" in pub and "journal" in pub:
      res+= " Presented at "+pub["conf"]+" and published in "+pub["journal"]+"."
   elif "journal" in pub:
      res+= " Published in "+pub["journal"]+"."
   elif "conf" in pub:
      res+= " Presented at "+pub["conf"]+"."
   else:
      res+= " Only on arXiv."

   # Possibly add long version or a video
   if "long" in pub:
      res+=pub["long"]
   if "video" in pub:
      res+=pub["video"]

   res+="</li>"
   # return the string
   return(res)
#End of Readhtml fonction

i=0
# Global integer for unique names


# Writing the list of best publi
best="# Highlights\n"
besthtml="<ul class = publi>\n"
for pub in publi:
   if "top" in pub and pub["top"]==True:
      best+=readmd(pub)
      besthtml+="\t"+readhtml(pub)+"\n"

besthtml+="</ul>\n"
# End of best publication


# Writing the list of publi by apparition
# TODO : Add uses of dates in publi
app="# Publication by apparition\n"
apphtml="""<div id="full" class="hidden">
               <h2>Publications by apparition</h2>
               <ul class = publi>\n"""
for pub in publi:
   app+=readmd(pub)
   apphtml+="\t"+readhtml(pub)+"\n"
apphtml+="</ul></div>\n"
# End of publication by apparition order



# Writing the list of publi on topics
top="# Publication by topics\n"
tophtml="<h2>Publication by topics</h2>\n"
for x in ["Graphs and Logic","Graph Combinatorics", "Distributed computing", "Query Enumeration"]:
   top+="\n ## "+x+"\n"
   # tophtml+="\t<h3>"+x+"</h3>\n\t<ul>\n"
   tophtml+="<h3>"+x+"""</h3>\n 
      <div><input type="checkbox" id=\""""+str(i)+"""\"style="display:none;"> 
         <div class="link">
            Full list
            <label for=\""""+str(i)+"""\">&#8600;</label>
         </div>
      <div class="hh">
         <ul>\n"""
   i=i+1
   for pub in publi:
      if "tag" in pub and pub["tag"]==x:
         top+=readmd(pub)
         tophtml+="\t\t\t\t\t"+readhtml(pub)+"\n"
   tophtml+="\t\t</ul>\n</div></div>\n\n\n"

# End publi by topics

# Writing new  list of publi on topics
# newTop=""" <div><input type="checkbox" id="1"style="display:none;"> 
newTop="""  <div id="topics" class = "hidden">
               <h2>Publications by Topics</h2>\n"""
for x in ["Graphs and Logic","Graph Combinatorics", "Distributed computing", "Query Enumeration"]:
   newTop+="<h3>"+x+"""</h3>\n
               <ul class = publi>\n"""
   for pub in publi:
      if "tag" in pub and pub["tag"]==x:
         newTop+="\t\t\t\t\t"+readhtml(pub)+"\n"
   newTop+="\t\t</ul>\n"
newTop+="</div>\n\n\n"

# Writing list of publi by types
byTypes="""  <div id="types" class = "hidden">
               <h2>All Publications</h2>\n"""
byTypes+="""<h3> Journals </h3>\n
               <ul class = publi>\n"""
for pub in publi:
   if "journal" in pub :
      byTypes+="\t\t\t\t\t"+readhtml(pub,"journal")+"\n"
byTypes+="\t\t</ul>\n"
# fin journal
byTypes+="""<h3> Conferences </h3>\n
               <ul class = publi>\n"""
for pub in publi:
   if "conf" in pub :
      byTypes+="\t\t\t\t\t"+readhtml(pub,"conf")+"\n"
byTypes+="\t\t</ul>\n"
# fin conf

byTypes+="""<h3> Unpublished </h3>\n
               <ul class = publi>\n"""
for pub in publi:
   if "conf" not in pub and "journal" not in pub :
      byTypes+="\t\t\t\t\t"+readhtml(pub,"arxiv")+"\n"
byTypes+="\t\t</ul>\n"
# fin arxiv
byTypes+="</div>\n\n\n"


md = open("publi.md", "w")
html = open("publi.html", "w")

# md.write(app+"\n"+top)

html.write("""
   <!DOCTYPE html>
   <html lang="en">
   <head>
      <meta charset="utf-8">
      <link rel="shortcut icon" href="image.ico" type="image/x-icon">
      <title>Alexandre Vigny </title>
      <link rel="stylesheet" media="screen" type="text/css" title="Design" href="test.css" />
   </head>

              
   <body>
   <div class = stickytop>
      <div class="topnav">
         <div class="container">
            <a class="navbar-brand" href=index.html> Alexandre Vigny </a>
            <a class="active" href=publi.html#types> Publications </a>
            <a class="navbar-brand" href=cv_vigny.pdf> CV </a>
         </div>
      </div>
      <div class="menu">
         <div class="container">
            <a href=#types> Full list &#8600;</a>
            <a href=#topics> By topics &#8600;</a>
         </div>
      </div>
   </div>
   <br>

   <div class="jumbotron">
      <div class="container">
           
   """+newTop+"\n\n\n"+byTypes+"\n</div>\n</div>\n</body>\n</html>\n")

   # """+apphtml+"\n\n\n"+newTop+"\n\n\n"+byTypes+"\n</div>\n</div>\n</body>\n</html>\n")


md.close()
html.close()