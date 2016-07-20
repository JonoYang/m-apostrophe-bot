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
   temp = []
   for char in string.upper():
      if char in morse_code:
         temp.append(morse_code[char])
      else:
         continue
   return "   ".join(temp)