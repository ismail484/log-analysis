#!/usr/bin/env python

import psycopg2
import bleach
import string


def connect(database_name="news"):
        try:
                """Connect to the PostgreSQL database
                 Returns a database connection."""
                db = psycopg2.connect("dbname={}".format(database_name))
                c = db.cursor()
                return db, c
        except psycopg2.Error as e:
                print "Unable to connect to database"
                # THEN perhaps exit the program
                sys.exit(1)


def get_articles():
    try:
        """Return the most popular three articles of all time
         from the 'database', most popular first."""
        db, c = connect()
        c = db.cursor()
        c.execute("select * from p_articles;")
        posts = c.fetchall()
        db.close()
        print('the most popular three articles are')
        for article, numView in posts:
            print "the article:", article, " has ---> ", numView, "views "
        return posts
    except:
        print("sorry it's a problem")


def get_authors():
    try:
        """Return the most popular article authors of all time
            from the 'database', most popular first."""
        db, c = connect()
        c = db.cursor()
        c.execute("select * from author_total_viewers ;")
        posts = c.fetchall()
        db.close()
        print('--------------------------------------------')
        print('the most popular article authors are')
        for author, numView in posts:
            print "the author", author, "has --->", numView, "views"
        return posts
    except:
        print("sorry it's a problem")


def get_date():
    try:
        """Return days did more than 1% of requests
         lead to errors from the 'database'"""
        db, c = connect()
        c = db.cursor()
        c.execute("""select to_char(date,'MonthDD,YYYY'),
                             error_precentage from error_precentage
                             where error_precentage>1;""")
        posts = c.fetchall()
        db.close()
        print('--------------------------------------------')
        print('the days whcih have request error more than 1%')
        for day, precent in posts:
            print "the day :", day, " has --->", precent, "%"
        return posts
    except:
        print("sorry it's a problem")
if __name__ == '__main__':
    get_articles()
    get_authors()
    get_date()
