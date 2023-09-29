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
    		<p>I am currently a postdoc at the University of Bremen, in the """+teamBremen+""" of """+sebi+""".<br>
    			Before that, I was a postdoc at the University of Warsaw, funded by the ERC grant Lipa of """+mikolaj+""".<br>
    			A couple of years earlier, I was a PhD student at the University Paris Diderot under the supervision of """+arnaud+' and '+luc+""".
        </p>
      </div>
      <!-- end block -->

      <div class="block">
    		<h2>Past / current positions</h2>
  			<ul>
  				<li> Since November 2019 : Postdoc at the University of Bremen.</li>
  				<li> From October 2018 to September 2019: Postdoc at the University of Warsaw.</li>
  				<li> From October 2015 to September 2018: PhD Student at the IMJ-PRG, in the University Paris Diderot.</li>
  				<li> From May 2015 to September 2015: Internship in the LSV, at the ENS Cachan.</li>
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