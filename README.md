

Project: Log analysis  - [Mohamed Ismail]
================================

Description
-----------------------------------

'''get statistics from Postgres SQL database and analyse it using python query'''

'''it shows the most popular three articles of all time '''

''then shows the most popular article authors of all time '''

'''finally shows the days did more than 1% of requests lead to errors '''

Required Libraries and Dependencies
-----------------------------------

it just needs ,Postgres SQL DB and pyton 2.7v or higher to run the application 


How to Run Project
------------------
1-Download the project files(newsdata.sql.tar.gz,analysis.py)

2-unzip newsdata.sql.tar.gzusing tar xf newsdata.sql.tar  -C /destination

3-importnewsdata.sql into postgres SQL DB using " psql -d news -f newsdata.sql".

4- run analysis.py using "python analysis.py"


Extra Credit Description
------------------------
the following features are implemented:

1-Python datastructure (functions, dictionaries,tuples)

2-Postgres SQL DB statements to manipulate the data .

3-create some views as stores to save some queries


Miscellaneous
-------------
the views which I have created are :

- For first requirement 'the most popular three articles of all time' I create:

1- create view p_article as  select substring(path,10,1000) as m,count(path) from log group by m order by count desc limit 4;

2-create view p_articles as select replace(m,'-',' ') as p_article ,count from p_article where m not like '';

- For second requirement 'the most popular article authors of all time' I create:

1-create view test3 as select substring(path,10,1000) as m,count(path) from log group by m order by count desc ;

2-create view test4  as select replace(m,'-',' ') as p_article ,count from test3 where m not like '';

3-create view my_author as select articles.author,articles.title ,authors.name from articles left join authors on articles.author=authors.id group by articles.author,articles.title,authors.name order by articles.author ;

4--create view all_author as select author,lower(my_author.title),name from my_author;

5--create view the_authors as select  all_author.name, test4.count from all_author left join test4  on all_author.lower  like concat(test4.p_article ,'%');

6-select name, sum(count)from the_authors group by name order by sum desc ;

- For third requirement 'the days did more than 1% of requests lead to errors' I create:

1-create view total_request as select date_trunc('day',time)m,count(status)from log group by m order by m ;

2-create view total_error as select status,time from log where status like '404%';

3-create view total_errors as select date_trunc('day',time)d,count(status) from total_error group by d order by d;

4-create view all_request  as select total_request.m  as date, total_request.count as request ,total_errors.count as error from total_request join total_errors on total_request.m=total_errors.d order by total_request.m ;

5-create view error_precentage as select date ,((error::float/request::float)*100)  as error_precentage from all_request order by error_precentage desc;




