import psycopg2, bleach
import string

DBNAME = "news"
try:
  def get_articles():
    """Return the most popular three articles of all time from the 'database', most popular first."""
    db = psycopg2.connect(database=DBNAME)
    #print("successfully executed  step one")
    c = db.cursor()
    c.execute("select * from p_articles;")
    posts = c.fetchall()
    db.close()

    print('the most popular three articles are')
    for a, b in posts:
      print  "the article:" ,a, " has --->", b ,"views"
    return posts
except:
  print("sorry it's a problem")
get_articles()


try:
  def get_authors():
    """Return the most popular article authors of all time from the 'database', most popular first."""
    db = psycopg2.connect(database=DBNAME)
    #print("successfully executed  step one")
    c = db.cursor()
    c.execute("select name, sum(count)from the_authors group by name order by sum desc ;")
    posts = c.fetchall()
    db.close()

    print('--------------------------------------------')
    print('the most popular three articles are')
    for a, b in posts:
      print  "Mr.:" ,a, " has --->", b ,"views"
    return posts
except:
  print("sorry it's a problem")
get_authors()

try:
  def get_date():
    """Return days did more than 1% of requests lead to errors from the 'database'"""
    db = psycopg2.connect(database=DBNAME)
    #print("successfully executed  step one")
    c = db.cursor()
    c.execute("select to_char(date,'MonthDD,YYYY'),error_precentage from error_precentage where error_precentage>1;")
    posts = c.fetchall()
    db.close()

    print('--------------------------------------------')
    print('the days whcih have request error more than 1%')
    for a, b in posts:
      print  "the day :" ,a, " has --->", b ,"%"
    return posts
except:
  print("sorry it's a problem")
get_date()



