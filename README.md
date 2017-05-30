

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
1-Download the project files:
 
 - newsdata.sql.tar.gz
 - views.sql
 - analysis.py

2-unzip newsdata.sql.tar.gzusing tar xf newsdata.sql.tar  -C /destination.

3-check if I have already imported my newsdata.sql using (psql=> /list), if exists then escape step4 .

4-if no ,then import newsdata.sql into postgres SQL DB using " psql -d news -f newsdata.sql".

5-import all views that I have created ,follow this steps:
  
  a)Log into the psql console by typing: psql
  
  b)Connect to the news database with the command: \c news
  
  c)Once connected to the news database, import the views using: \i views.sql ;

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

1-create view author_articles as select articles.author,articles.slug ,authors.name from articles left join authors on articles.author=authors.id group by articles.author,articles.slug,authors.name order by articles.author ;

2-create view articles_request as select substring(path,10,1000) as article,count(path) from log group by article  order by count desc;

3-create view  author_viewers as select  author_articles.name, articles_request.count from author_articles left join articles_request on author_articles.slug  like articles_request.article;

4-create view author_total_viewers as select name, sum(count)from author_viewers  group by name order by sum desc ;

- For third requirement 'the days did more than 1% of requests lead to errors' I create:

1-create view total_request as select date_trunc('day',time)m,count(status)from log group by m order by m ;

2-create view  total_error as select status,time from log where status like '404%';

3-create view  total_errors as select date_trunc('day',time)d,count(status) from total_error group by d order by d;

4-create view all_request  as select total_request.m  as date, total_request.count as request ,total_errors.count as error from total_request join total_errors on total_request.m=total_errors.d order by total_request.m ;

5-create view error_precentage as select date ,((error::float/request::float)*100)  as error_precentage from all_request order by error_precentage desc;




