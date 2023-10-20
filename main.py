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
        <p>I am currently a junior professor at the University Clermont Auvergne in France. My topics of interest lie in the intersection of logic, algorithms, and graph theory.
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

        <h2>Some links</h2>
        <ul>
            <li> Theoretical Computer Scientists for Future
            <a href="https://tcs4f.org">
            <img width="80" src="https://tcs4f.org/themes/tcs4f/img/brilliant_tcs_4future.png" alt="TCS 4 Future brillant button">
            </a></li>

            <li>No free view? No review! <a href="https://nofreeviewnoreview.org/"><img width="80" src="img/nfvnr-button.png" style='vertical-align:middle;'></a></li>

            <li> Co-organizer of the <a href="https://podc-dare.github.io/">PODC-DARE</a> workshop.</li>
        </ul>



    <div class="block">
        <h2 id="publi"> Publications</h2>
        <a href=publi.html#full>Full list here</a>
        <h3>Highlights</h3> 
        """+besthtml+"""
    </div>

    <div class="block">
        <h3>Science popularization</h3>
        <ul>
            <li> Article (in french) in the first edition of <a href="https://www.gdr-im.fr/gazette/">la gazzette</a> of the <a href="https://www.gdr-im.fr/">GDR-IM</a>. (PDF <a href = "https://www.gdr-im.fr/wp-content/uploads/2020/07/gazette_01.pdf">here</a>)</li>
        </ul>

        <h2> My PhD defense!</h2>
        I defended my PhD on September the 27th 2018. <a href="Papers/these-vigny.pdf">manuscript</a>, <a href="slides/these-vigny.pdf">slides</a>. <br>
        All the information is <a href="These/defense-en.html">here.</a> <br>
    </div>

    
    <!-- Start Teaching Block -->
    <div class="block">
        <h2> Teaching (in French and English) </h2>
        <h3>In Clermont</h3>
        <details>
            <summary>Soon...</summary>
            Starting December 2023.
        </details>
        
        <h3>In Bremen</h3>
        <ul>
            <li> 2021-2022</li>
            <div><input type="checkbox" id="DGA" style="display:none;">
                <div class="link">
                    Databases Graphs and Algorithms
                    <label for="DGA">&#8600;</label>
                </div>
                <div class="hh">
                    All in <a href="https://elearning.uni-bremen.de/">Stud.IP</a><br>
                </div>
            </div>
            <div><input type="checkbox" id="SMT" style="display:none;">
                <div class="link">
                    Set and Model Theory
                    <label for="SMT">&#8600;</label>
                </div>
                <div class="hh">
                    All in <a href="https://elearning.uni-bremen.de/">Stud.IP</a><br>
                </div>
            </div>

            <li> 2020-2021</li>
            <div><input type="checkbox" id="DGA" style="display:none;">
                <div class="link">
                    Databases Graphs and Algorithms
                    <label for="DGA">&#8600;</label>
                </div>
                <div class="hh">
                    All in <a href="https://elearning.uni-bremen.de/">Stud.IP</a><br>
                </div>
            </div>
            <div><input type="checkbox" id="SMT" style="display:none;">
                <div class="link">
                    Set and Model Theory
                    <label for="SMT">&#8600;</label>
                </div>
                <div class="hh">
                    All in <a href="https://elearning.uni-bremen.de/">Stud.IP</a><br>
                </div>
            </div>

            <li> 2019-2020</li>
            <div><input type="checkbox" id="paraC" style="display:none;">
                <div class="link">
                    Parameterized Complexity
                    <label for="paraC">&#8600;</label>
                </div>
                <div class="hh">
                    All in <a href="https://elearning.uni-bremen.de/">Stud.IP</a><br>
                </div>
            </div>
            <div><input type="checkbox" id="FMT" style="display:none;">
                <div class="link">
                    Finite Model Theory
                    <label for="FMT">&#8600;</label>
                </div>
                <div class="hh">
                    All in <a href="https://elearning.uni-bremen.de/">Stud.IP</a><br>
                </div>
            </div>
        </ul>
        <h3>In Paris</h3> 
        <ul>
            <li> 2017-2018</li>
            <div><input type="checkbox" id="CI2" style="display:none;">
                <div class="link">
                    CI2 : Concepts Informatiques, L1 Math-Info 2nd semestre.
                    <label for="CI2">&#8600;</label>
                </div>
                <div class="hh">
                    Sur moodle.<br>
                </div>
            </div>

            <div><input type="checkbox" id="bd18" style="display:none;">
                <div class="link">
                    Bases de données, L3 MIASHS, M1 ISIFAR, 2eme semestre.
                    <label for="bd18">&#8600;</label>
                </div>
                <div class="hh">
                    Sur moodle.<br>
                </div>
            </div>
            
            <li> 2016-2017</li>
            <div><input type="checkbox" id="EA3" style="display:none;">
                <div class="link">
                    EA3 : Éléments d'Algorithmique, L2 Info 1er semestre.
                    <label for="EA3">&#8600;</label>
                </div>
                <div class="hh">
                    La page du <a href="https://www.irif.fr/~amicheli/Ens/EA3/">cours</a> d'Anne Micheli <br>
                </div>
            </div>

            <div><input type="checkbox" id="bd17" style="display:none;">
                <div class="link">
                    Bases de données, L3 MIASHS, M1 ISIFAR, 2eme semestre
                    <label for="bd17">&#8600;</label>
                </div>
                <div class="hh">
                    <ul>
                        <li> TD1 : <a href="td/2016-2017/bdd_td1.pdf">sujet</a>, <a href="td/2016-2017/bdd_td1-correction.sql">correction</a>. </li>
                        <li> TD2 : <a href="td/2016-2017/bdd_td2.pdf">sujet</a>.</li>
                        <li> TD3 : <a href="td/2016-2017/bdd_td3.pdf">sujet</a>.</li>
                        <li> TD4 : <a href="td/2016-2017/bdd_td4.pdf">sujet</a>.</li>
                        <li> TD5 : <a href="td/2016-2017/bdd_td5.pdf">sujet</a>.</li>
                        <li> TD6 : <a href="td/2016-2017/bdd_td6.pdf">sujet</a>.</li>
                        <li> TD7 : <a href="td/2016-2017/bdd_td7.pdf">sujet</a>.</li>
                        <li> TD8 : <a href="td/2016-2017/bdd_td8.pdf">sujet</a>.</li>
                        <li> TD9 : <a href="td/2016-2017/bdd_td9.pdf">sujet</a>.</li>
                        <li> TD10 : <a href="td/2016-2017/bdd_td10.pdf">sujet</a>.</li>
                        <li> TD11 : <a href="td/2016-2017/bdd_td11.pdf">sujet</a>.</li>
                    </ul>
                </div>
            </div>
            
            <li> 2015-2016 </li>
            IP1 : Initiation à la programation, L1 Math 1er semestre.<br>

            <div><input type="checkbox" id="LA3" style="display:none;">
                <div class="link">
                    LA3 : Langage et Automates, L2 Math-Info 1er semestre.
                    <label for="LA3">&#8600;</label>
                </div>
                <div class="hh">
                    <ul>
                        <li> <a href="td/2015-2016/LA3_TD1.pdf">TD1</a></li>
                        <li> <a href="td/2015-2016/LA3_TD2.pdf">TD2</a></li>
                        <li> <a href="td/2015-2016/LA3_TD3.pdf">TD3</a></li>
                        <li> <a href="td/2015-2016/LA3_TD4.pdf">TD4</a></li>
                        <li> <a href="td/2015-2016/LA3_TD5.pdf">TD5</a></li>
                        <li> <a href="td/2015-2016/LA3_TD6.pdf">TD6</a></li>
                        <li> <a href="td/2015-2016/LA3_TD7.pdf">TD7</a></li>
                        <li> <a href="td/2015-2016/LA3_TD8.pdf">TD8</a></li>
                        <li> <a href="td/2015-2016/LA3_TD9.pdf">TD9</a></li>
                        <li> <a href="td/2015-2016/LA3_regexp.pdf">TD expressions régulières.</a></li>
                    </ul>
                </div>
            </div>
        </ul>
    </div>
    <!-- End Teaching Block -->




""")




for line in end:
    f.write(line) 
f.close()
start.close()
end.close()