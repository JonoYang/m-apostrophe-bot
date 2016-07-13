#!/usr/bin/python

"""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import os
import praw
import pdb
import re
import sqlite3
import sys
from config_bot import *

def init_db():
   conn = sqlite3.connect("posts_replied_to.sqlite")
   c = conn.cursor()
   c.execute('CREATE TABLE {table_name} ({new_field} {field_type})'\
            .format(table_name = "posts", new_field = "post_id", field_type = "TEXT"))
   c.commit()
   c.close()

def insert_db(post_id):
   conn = sqlite3.connect("posts_replied_to.sqlite")
   c = conn.cursor()
   c.execute('''INSERT INTO posts(post_id) VALUES(?)''', (post_id))
   c.commit()
   c.close()

def look_up_post_id(post_id):
   conn = sqlite3.connect("posts_replied_to.sqlite")
   c = conn.cursor()
   
   cursor.execute('''SELECT name, email, phone FROM users''')
   user1 = cursor.fetchone() #retrieve the first row
   print(user1[0]) #Print the first column retrieved(user's name)

   c.commit()
   c.close()

def main():

   if not os.path.isfile("config_bot.py"):
      sys.exit("%s: config_bot.py missing. Create config_bot.py with Reddit credentials" % sys.argv[0])
   if not os.path.isfile("posts_replied_to.sqlite"):
      init_db()

   user_agent = ("m-apostrophe-bot 0.1")
   r = praw.Reddit(user_agent = user_agent)
   r.login(REDDIT_USERNAME, REDDIT_PASS)

 if __name__ == '__main__':
   main()