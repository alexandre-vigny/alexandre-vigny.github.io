SET search_path  TO world, public ;
--permet de remplacer world.table.colone par table.colone


-----------------------------------------------------
--------------------- Section 4 ---------------------
-----------------------------------------------------


--1: les regions
SELECT DISTINCT country.region 
FROM country ORDER BY region;


--2: les regions d'Europe
select distinct region from country
where country.continent= 'Europe' ;


--3: les pays d'Amerique du sud
Select name_country from world.country
where world.country.region = 'Southern Europe' ;


--4: les capitales (par ID) d'Europe de l'ouest
select capital from world.country
where world.country.region = 'Western Europe' ;


--5: Les langues officielles dans au moins un pays
select distinct language from countrylanguage
where countrylanguage.isofficial ;


--6: Les pays ou le francais est une langue officielle
select distinct countrycode from countrylanguage
where countrylanguage.isofficial and language = 'French';


--7: Quelle est la date d’independance de la France ?
select indepyear from country
where countrycode = 'FRA';


--8: Quelles sont les dates d’independance des pays d’Europe ?
SELECT name_country, indepyear FROM world.country
WHERE continent ='Europe' ORDER BY indepyear ;


--9: Quelles sont les villes francaises de plus de 200 000 habitants ?
select name_city ,population_city from city
where population_city > 200000 and countrycode = 'FRA' order by population_city;


--10: Pour chaque pays europeens, calculer la densite, le gnp par habitant,
--		et l’esperance de vie, ordonner par densite decroissante.
select 	name_country,
		population_country / surfacearea as densite,
		gnp / population_country as gnp_par_abitant, 
		lifeexpectancy
from world.country
where continent = 'Europe' order by densite desc;


--11: Quels sont les pays ou l’esperance de vie n’est pas inferieure a 77 ans
--	et le pnb par habitant n’est pas superieur a 0.010 ?
select name_country from country
where not lifeexpectancy < 77 and not gnp / population_country > 0.010;


--12: Quels sont les pays tels que la condition (esperance de vie superieure ou egale a 77
--	ans ou PNB par habitant inferieur a 0.01) n’est pas verifee ?
select name_country from country
where not (lifeexpectancy < 77 or gnp / population_country > 0.010) ;


--13: Quels sont les pays (code) ou une langue est officielle sans être parlee par au moins
--		la moitie de la population ?
select distinct countrycode from countrylanguage
where isofficial and  percentage < 50;


--14: Quels sont les pays qui ont au moins une langue officielle ?
select distinct countrycode from countrylanguage
where isofficial;

--15 Quels sont les noms des pays qui comptent plus de 100 000 000 d’habitants ?
select name_country from country
where population_country > 100000000;






-----------------------------------------------------
--------------------- Section 5 ---------------------
-----------------------------------------------------


--1: Quels sont les noms des capitales Sud-Americaines ?
select name_city from world.country as c, world.city as t
where c.capital = t.id and c.continent = 'South America';

--2: Quels sont les noms des pays ou le francais est langue officielle ?
select name_country from country, countrylanguage
where country.countrycode = countrylanguage.countrycode
and language = 'French' and isofficial;


--3: Quelles sont les pays ou l’espagnol est langue officielle et la
--	forme de gouvernement est federal republic ?
select name_country from country as c, countrylanguage as cl
where c.countrycode = cl.countrycode
and governmentform = 'Federal Republic' and isofficial and language = 'Spanish';


--4: Quels sont les pays qui ont plus de deux langues officielles ?
select distinct name_country
from world.country as c,
world.countrylanguage as l1,
world.countrylanguage as l2
where l1.countrycode = c.countrycode
and c.countrycode = l2.countrycode
and l1.language != l2.language
and l2.isofficial and l1.isofficial = true ;


--5: Quels sont les pays qui n’ont pas de langue officielle ?

-- voir 'EXCEPT' au td2


--6: Quels sont les pays qui comportent au moins deux villes de plus de 1 000 000 habitants ?
select distinct name_country from country as c,
city as c1, city as c2
where c1.countrycode = c2.countrycode and c1.countrycode = c.countrycode
and not c1.id=c2.id and c1.population_city > 1000000 and c2.population_city>1000000;


--7: idem que TP2, section 4.1, question 7. 


--8: idem que TP2, section 4.1, question 3.




--------------------- FIN ---------------------











