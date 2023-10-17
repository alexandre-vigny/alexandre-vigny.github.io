from publications import *


start = open("start.txt", "r")
end = open("end.txt", "r")
f = open("index.html", "w")




# Beginning
for line in start:
    f.write(line) 

# Presentation
f.write("""
      <div class="block">
    		<h2>About me</h2>
    		<p>I am currently a junior professor at the University Clermont Auvergne in France.
      </div>
      <!-- end block -->

      <div class="block">
    		<h2>Past / current positions</h2>
  			<ul>
  				<li> Since October 2023: Junior professor at University Clermont Auvergne.</li>
  				<li> From November 2019 to October 2023: Postdoc at the University of Bremen, in the """+teamBremen+""" of """+sebi+""".</li>
  				<li> From October 2018 to September 2019: Postdoc at the University of Warsaw, with """+mikolaj+""" and """+szymon+""".</li>
  				<li> From October 2015 to September 2018: PhD Student at the IMJ-PRG, in the University Paris Diderot. Under the supervision of """+arnaud+' and '+luc+""".</li>
  				<li> From May 2015 to September 2015: Internship in the LSV, at the ENS Cachan, with """+luc+""".</li>
  			</ul>
      </div>
      <!-- end block -->

      <div class="block">
    		<h2 id="publi"> Publications</h2>
         <a href=publi.html#full>Full list here</a>
         <h3>Highlights</h3> 
         """+besthtml+"""
      </div>
""")




for line in end:
    f.write(line) 
f.close()
start.close()
end.close()