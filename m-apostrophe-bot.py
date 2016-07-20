#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Written by Jonathan "Jono" Yang - the.jonathan.yang@gmail.com

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

import config_bot
import morse
import os
import praw
import pdb
import sqlite3
import sys
import time

# Creates sqlite3 database with a table named posts with one row named post_id
def init_db():
   conn = sqlite3.connect("posts_replied_to.sqlite")
   c = conn.cursor()
   c.execute("CREATE TABLE posts (post_id TEXT)")
   conn.commit()
   conn.close()

# Inserts a post id into the table posts
def insert_db(post_id):
   conn = sqlite3.connect("posts_replied_to.sqlite")
   c = conn.cursor()
   c.execute("INSERT INTO posts VALUES (?)", (post_id,))
   conn.commit()
   conn.close()

# Looks up a post id to see if the bot has processed it before
# Returns True if the bot has processed the post id before, False otherwise
def look_up_post_id(post_id):
   conn = sqlite3.connect("posts_replied_to.sqlite") 
   c = conn.cursor()
   c.execute("SELECT post_id FROM posts WHERE post_id = (?)", (post_id,))
   data = c.fetchone()
   conn.close()
   return True if data != None else False

# Main bot logic, puts apostrophes after words starting with m or M. 
# Returns the modified post body if any words have been modified, 
# otherwise, it returns None
def apostrophify_post(post_body):
   # flag is for determining if post body was modified in any way
   flag = False
   words = post_body.split()
   for i, word in enumerate(words):
      if word[0] == "m" or word[0] == "M":
         words[i] = word[:1] + "'" + word[1:]
         flag = True
   return " ".join(words) if flag == True else None

# credit to bboe (https://gist.github.com/bboe/1860715)
def handle_ratelimit(func, *args, **kwargs):
    while True:
        try:
            func(*args, **kwargs)
            break
        except praw.errors.RateLimitExceeded as error:
            print "Rate limit exceeded: sleeping for %d seconds" % error.sleep_time
            time.sleep(error.sleep_time)

if __name__ == "__main__":
   if not os.path.isfile("config_bot.py"):
      sys.exit("%s: config_bot.py missing. Create config_bot.py with Reddit credentials" % sys.argv[0])
   if not os.path.isfile("posts_replied_to.sqlite"):
      init_db()

   user_agent = "m-apostrophe-bot 0.1"
   r = praw.Reddit(user_agent = user_agent)
   r.login(config_bot.REDDIT_USERNAME, config_bot.REDDIT_PASS)

   for comment in praw.helpers.comment_stream(r, "pythonforengineers"):
      if look_up_post_id(comment.id) == False:
         text = morse.make_morse(comment.body)
         insert_db(comment.id)
         if text == None:
            continue
         else:
            handle_ratelimit(comment.reply, text)
            print("Responded to: " + comment.id)
            # not sure if this will prevent me from getting rate limited
            time.sleep(60)