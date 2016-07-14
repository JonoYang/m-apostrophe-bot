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
import sqlite3
import sys
import time
from config_bot import *

def init_db():
   conn = sqlite3.connect("posts_replied_to.sqlite")
   c = conn.cursor()
   c.execute("CREATE TABLE posts (post_id TEXT)")
   conn.commit()
   conn.close()

def insert_db(post_id):
   conn = sqlite3.connect("posts_replied_to.sqlite")
   c = conn.cursor()
   c.execute("INSERT INTO posts VALUES (?)", (post_id,))
   conn.commit()
   conn.close()

def look_up_post_id(post_id):
   conn = sqlite3.connect("posts_replied_to.sqlite") 
   c = conn.cursor()
   c.execute("SELECT post_id FROM posts WHERE post_id = (?)", (post_id,))
   data = c.fetchone()
   conn.close()
   return True if data != None else False

def apostrophify_post(post_body):
   # flag is for determining if post body was modified in any way
   flag = False
   words = post_body.split()
   for i, word in enumerate(words):
      if word[0] == "m" or word[0] == "M":
         words[i] = word[:1] + "'" + word[1:]
         flag = True
   return " ".join(words) if flag == True else None

if __name__ == "__main__":
   if not os.path.isfile("config_bot.py"):
      sys.exit("%s: config_bot.py missing. Create config_bot.py with Reddit credentials" % sys.argv[0])
   if not os.path.isfile("posts_replied_to.sqlite"):
      init_db()

   user_agent = "m-apostrophe-bot 0.1"
   r = praw.Reddit(user_agent = user_agent)
   r.login(REDDIT_USERNAME, REDDIT_PASS)

   for comment in praw.helpers.comment_stream(r, "pythonforengineers", limit = 25):
      if look_up_post_id(comment.id) == False:
         text = apostrophify_post(comment.body)
         insert_db(comment.id)
         if text == None:
            continue
         else:
            comment.reply(text)
         print("Responded to: " + comment.id)
         time.sleep(60)