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

morse_code = {
   "A": "• −",
   "B": "− • • •",
   "C": "− • − •",
   "D": "− • •",
   "E": "•",
   "F": "• • − •",
   "G": "− − •",
   "H": "• • • •",
   "I": "• •",
   "J": "• − − −",
   "K": "− • −",
   "L": "• − • •",
   "M": "− −",
   "N": "− •",
   "O": "− − −",
   "P": "• − − •",
   "Q": "− − • −",
   "R": "• − •",
   "S": "• • •",
   "T": "−",
   "U": "• • −",
   "V": "• • • −",
   "W": "• − −",
   "X": "− • • −",
   "Y": "− • − −",
   "Z": "− − • •",
   "0": "− − − − −",
   "1": "• − − − −",
   "2": "• • − − −",
   "3": "• • • − −",
   "4": "• • • • −",
   "5": "• • • • •",
   "6": "− • • • •",
   "7": "− − • • •",
   "8": "− − − • •",
   "9": "− − − − •"
}

def make_morse(string):
   word_temp = []
   post_temp = []

   # We set each letter in the post to upper case and break the string
   # into a list of words.
   string = string.upper().split()
   
   for word in string:
      for char in word:
         if char in morse_code:
            # We translate each character of a word and put its Morse 
            # code representation as a string into a list.
            word_temp.append(morse_code[char])
         else:
            # If a character does not have a Morse code representation,
            # we ignore it and move on to the next character
            continue

      # Once we are done converting each caracter of a word into it's
      # Morse code representation, we join the list together to form
      # a whole string and append the word to the post_temp list, that
      # stores the Morse code representation of each word in the post.
      post_temp.append("   ".join(word_temp))

      # We clear the temporary word list for the next word
      word_temp = []

   # We finally join all the words together as a single string, where
   # the words are delimited by 3 spaces, then a slash, followed by 3
   # more spaces
   return "   /   ".join(post_temp)