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
vi_stackexchange_good_votes = pd.read_sql_query('SELECT * FROM vi_stackexchange_votes where VoteTypeId in (1,2,5)', engine)
vi_stackexchange_bad_votes = pd.read_sql_query('SELECT * FROM vi_stackexchange_votes where VoteTypeId in (3,4,12)', engine)


vi_stackexchange_votes_v1 = vi_stackexchange_good_votes[['Id', 'PostId', 'VoteTypeId']]
vi_stackexchange_votes_v1 = vi_stackexchange_votes_v1.groupby(['PostId'])
vi_stackexchange_votes_v1 = vi_stackexchange_votes_v1['VoteTypeId'].count()
vi_stackexchange_votes_v1.rename(columns={'count':'total_good'})
vi_stackexchange_votes_v1 = vi_stackexchange_votes_v1.to_frame()

vi_stackexchange_votes_v2 = vi_stackexchange_bad_votes[['Id', 'PostId', 'VoteTypeId']]
vi_stackexchange_votes_v2 = vi_stackexchange_votes_v2.groupby(['PostId'])
vi_stackexchange_votes_v2 = vi_stackexchange_votes_v2['VoteTypeId'].count()
vi_stackexchange_votes_v2.rename(columns={'count':'total_bad'})
vi_stackexchange_votes_v2 = vi_stackexchange_votes_v2.to_frame()

#vi_stackexchange_votes_v3 = vi_stackexchange_votes_v1.merge(vi_stackexchange_votes_v2, how='outer', left_on = 'PostId', right_on = 'PostId' )
print vi_stackexchange_votes_v1
#print vi_stackexchange_votes_v3

