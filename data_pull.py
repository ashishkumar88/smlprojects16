import pandas as pd
from pandas.io import sql
import os
import time
from datetime import datetime
from urllib2 import urlopen, URLError, HTTPError
from sqlalchemy import create_engine
import subprocess
import urllib
import MySQLdb
import re

engine = create_engine("mysql+mysqldb://root:&RQQz6;_xv}37HHa@personaldb1.cacsnunleniu.us-west-2.rds.amazonaws.com/sml_project?charset=utf8&use_unicode=0")

vi_stackexchange_posts = pd.read_sql_query('SELECT * FROM vi_stackexchange_posts', engine)
vi_stackexchange_badges = pd.read_sql_query('SELECT * FROM vi_stackexchange_badges', engine)
vi_stackexchange_comments = pd.read_sql_query('SELECT * FROM vi_stackexchange_comments', engine)
vi_stackexchange_post_links = pd.read_sql_query('SELECT * FROM vi_stackexchange_post_links', engine)
vi_stackexchange_posts_history = pd.read_sql_query('SELECT * FROM vi_stackexchange_posts_history', engine)
vi_stackexchange_tags = pd.read_sql_query('SELECT * FROM vi_stackexchange_tags', engine)
vi_stackexchange_users = pd.read_sql_query('SELECT * FROM vi_stackexchange_users', engine)
vi_stackexchange_votes = pd.read_sql_query('SELECT * FROM vi_stackexchange_votes', engine)


         
