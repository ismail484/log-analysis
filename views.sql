create view p_article as select substring(path,10,1000) as m,count(path) from log group by m order by count desc limit 4;

create view p_articles as select replace(m,'-',' ') as p_article ,count from p_article where m not like '';


create view author_articles as select articles.author,articles.slug ,authors.name from articles left join authors on articles.author=authors.id group by articles.author,articles.slug,authors.name order by articles.author ;

create view articles_request as select substring(path,10,1000) as article,count(path) from log group by article order by count desc;

create view author_viewers as select author_articles.name, articles_request.count from author_articles left join articles_request on author_articles.slug like articles_request.article;

create view author_total_viewers as select name, sum(count)from author_viewers group by name order by sum desc ;


create view total_request as select date_trunc('day',time)m,count(status)from log group by m order by m ;

create view total_error as select status,time from log where status like '404%';

create view total_errors as select date_trunc('day',time)d,count(status) from total_error group by d order by d;

create view all_request as select total_request.m as date, total_request.count as request ,total_errors.count as error from total_request join total_errors on total_request.m=total_errors.d order by total_request.m ;

create view error_precentage as select date ,((error::float/request::float)*100) as error_precentage from all_request order by error_precentage desc;