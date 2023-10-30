
luc =       "<a href=http://pages.saclay.inria.fr/luc.segoufin/>Luc Segoufin</a>"
arnaud =    "<a href=https://webusers.imj-prg.fr/~arnaud.durand/>Arnaud Durand</a>"
mikolaj =   "<a href=https://www.mimuw.edu.pl/~bojan/>Mikołaj Bojańczyk</a>"
sebi =      "<a href=https://www.uni-bremen.de/en/theorie/team/profiles/prof-dr-sebastian-siebertz>Sebastian Siebertz</a>"
szymon =    "<a href=https://www.mimuw.edu.pl/~szymtor/>Szymon Toruńczyk</a>"
nicoleSchw= "<a href=https://www.informatik.hu-berlin.de/de/forschung/gebiete/loginf/thi/schweikardt/>Nicole Schweikardt</a>"
michal=     "<a href=https://www.mimuw.edu.pl/~mp248287/>Michał Pilipczuk</a>"
nicoleSchi= "<a href=https://www.uni-bremen.de/en/theorie/team>Nicole Schirrmacher</a>"
mario =     "<a href=https://www.uni-bremen.de/en/theorie/team>Mario Grobler</a>"
yiting=     "<a href=https://dblp.org/pid/234/5037.html>Yiting Jiang</a>"
patrice=    "<a href=http://madezhi.free.fr/>Patrice Ossona de Mendez</a>"
niko=       "<a href=https://user.informatik.uni-bremen.de/nikmaehl/>Nikolas Mählmann</a>"
alex=       "<a href=https://www.uni-bremen.de/en/cslog/team/alexander-lindermayr>Alexander Lindermayr</a>"
ozan=       "<a href=https://dblp.uni-trier.de/pid/307/5051.html>Ozan Heydt</a>"
simeon=     "<a href=https://dblp.uni-trier.de/pid/280/3295.html>Simeon Kublenz</a>"
giannos=    "<a href=https://www.lirmm.fr/~gstamoulis/>Giannos Stamoulis</a>"
dimitrios=  "<a href=https://www.lirmm.fr/~thilikosto/>Dimitrios M. Thilikos</a>"
jan=        "<a href=https://www.ac.tuwien.ac.at/people/dreier/>Jan Dreier</a>"
amer=       "<a href=https://www.aub.edu.lb/pages/profile.aspx?MemberId=aa368>Amer E. Mouawad</a>"

teamBremen= "<a href=https://www.uni-bremen.de/en/theorie/team>team</a>"

# TODO
#nothing !

# Initialization list of publi as dictionary
publi = []

# List of publi
DisPath =  { 
   "link":"<a href=\"https://doi.org/10.48550/arXiv.2302.07033\"> Model Checking Disjoint-Paths Logic on Topological-Minor-Free Graph Classes.</a>",
   "authors":"With "+nicoleSchi+", "+sebi+", "+giannos+" and "+dimitrios+".",
   "tag":"Separator Logic"
}
publi.append(DisPath)


DistribDom =  { 
   "link":"<a href=\"https://arxiv.org/pdf/2207.02669.pdf\"> Distributed domination on sparse graph classes.</a>",
   "journal":"<a href=\"https://www.sciencedirect.com/science/article/abs/pii/S0195669823000902\">European Journal of Combinatorics</a>",
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
   "tag":"Separator Logic",
   "top":True
}
publi.append(MCSepLogic)



FoConnDef =  { 
   "link":"<a href=\"https://drops.dagstuhl.de/opus/volltexte/2022/15754/\"> First-Order Logic with Connectivity Operators.</a>",
   "conf":"CSL 2022",
   "journal":"<a href=\"https://dl.acm.org/doi/abs/10.1145/3595922\">ACM ToCL</a>",
   "authors":"With "+nicoleSchi+" and "+sebi+".",
   "tag":"Separator Logic",
   "top":True
}
publi.append(FoConnDef)


LocalDomPla =  { 
   "link":"<a href=\"https://arxiv.org/abs/2111.14506\"> Local planar domination revisited.</a>",
   "authors":"With "+ozan+" and "+sebi+".",
   "conf":"SIROCCO 2022",
   "tag":"Distributed computing"
}
publi.append(LocalDomPla)

Discrepancy =  { 
   "link":"<a href=\"https://arxiv.org/abs/2105.03693\"> Discrepancy and Sparsity.</a>",
   "authors":"With "+mario+", "+yiting+", "+patrice+" and "+sebi+".",
   "tag":"Graph Combinatorics",
}
publi.append(Discrepancy)




LocalDomBE =  { 
   "link":"<a href=\"https://arxiv.org/abs/2012.02701\"> Constant Round Distributed Domination on Graph Classes with Bounded Expansion.</a>",
   "authors":"With "+simeon+" and "+sebi+".",
   "conf":"SIROCCO 2021",
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
   "link":"<a href=\"https://drops.dagstuhl.de/opus/volltexte/2020/12755/\"> Elimination Distance to Bounded Degree on Planar Graphs.</a>",
   "authors":"With "+alex+" and "+sebi+".",
   "conf":"MFCS 2020",
   "long":"<a href = \"https://arxiv.org/abs/2007.02413\"> Arxiv</a> long version.",
   "video":" <a href= \"https://www.youtube.com/watch?v=oTKueyUsNwY\">Video presentation.</a>",
   "tag":"Graph Combinatorics",
   "top":True
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
   "journal":"<a href=\"https://dl.acm.org/doi/abs/10.1145/3517035\">J.ACM</a>",
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

def readhtml (pub):
   res= ""
   # Write the name and link
   res+= "<li>"+pub["link"]+"<br>"
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
   # res+="<br>"
   # Possibly add long version or a video
   if "long" in pub:
      res+=pub["long"]
   if "video" in pub:
      res+=pub["video"]
   # if "long" in pub or "video" in pub:
   #    res+="<br>"
   res+="</li>"
   # return the string
   return(res)
#End of Readhtml fonction

i=0
# Global integer for unique names


# Writing the list of best publi
best="# Highlights\n"
besthtml="<ul>\n"
for pub in publi:
   if "top" in pub and pub["top"]==True:
      best+=readmd(pub)
      besthtml+="\t"+readhtml(pub)+"\n"

besthtml+="</ul>\n"
# End of best publication


# Writing the list of publi by apparition
app="# Publication by apparition\n"
apphtml="""<div id="full" class="hidden">
               <h2>Publications by apparition</h2>
               <ul>\n"""
for pub in publi:
   app+=readmd(pub)
   apphtml+="\t"+readhtml(pub)+"\n"
apphtml+="</ul></div>\n"
# End of publication by apparition order



# Writing the list of publi on topics
top="# Publication by topics\n"
tophtml="<h2>Publication by topics</h2>\n"
for x in ["Separator Logic","Graph Combinatorics", "Distributed computing", "Query Enumeration"]:
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
for x in ["Separator Logic","Graph Combinatorics", "Distributed computing", "Query Enumeration"]:
   newTop+="<h3>"+x+"""</h3>\n
               <ul>\n"""
   for pub in publi:
      if "tag" in pub and pub["tag"]==x:
         newTop+="\t\t\t\t\t"+readhtml(pub)+"\n"
   newTop+="\t\t</ul>\n"
newTop+="</div>\n\n\n"



md = open("publi.md", "w")
html = open("publi.html", "w")

md.write(app+"\n"+top)
# html.write("""
#            <!DOCTYPE html>
#            <html lang="en">
#            <head>
#             <link rel="stylesheet" media="screen" type="text/css" title="Design" href="test.css" />
#            </head>
#            <body>
#            <div class = stick>
#                <div class="topnav">
#                   <a class="navbar-brand" href=test.html> Alexandre Vigny </a>
#                   <a class="navbar-brand" href=test.html#contact> Contact </a>
#                   <a class="active" href=test.html#publi> Publications </a>
#                   <a class="navbar-brand" href=cv_vigny.pdf> CV </a>
#                </div><br>
#                <div>
#                   <label for="0">Full list &#8600;</label>
#                   <label for="1">By topics &#8600;</label>
#                </div>
#             </div>
           
#            """+apphtml+"\n\n<br><br><br>\n\n"+apphtml2+"""

#             """+tophtml+"\n</body>\n</html>\n")

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
            <a class="active" href=publi.html#full> Publications </a>
            <a class="navbar-brand" href=cv_vigny.pdf> CV </a>
         </div>
      </div>
      <div class="menu">
         <div class="container">
            <a href=#full> Full list &#8600;</a>
            <a href=#topics> By topics &#8600;</a>
         </div>
      </div>
   </div>
   <br>

   <div class="jumbotron">
      <div class="container">
           

   """+apphtml+"\n\n\n"+newTop+"\n</div>\n</div>\n</body>\n</html>\n")


md.close()
html.close()