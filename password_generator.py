# ===================================================================
# MIT License
#
# Copyright (c) 2025 Anthony Cotales <ton.cotales@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ===================================================================

import string
import random
import argparse


def main():
	parser = argparse.ArgumentParser(
		prog="password_generator.py",
		description="Generate a strong random password string.",
		epilog="INFO: The default excluded characters are []{}()\"'` ",
		)
	parser.add_argument("-s", "--size", metavar="",  type=int, default=10, help="length of the password")
	parser.add_argument("-a", "--all", action="store_true", help="use all special characters")
	arguments = parser.parse_args()
	password = PasswordGenerator()
	print(password.generate(arguments.size, all_characters=arguments.all))


class PasswordGenerator:

	MIN_LENGTH = 10
	MAX_LENGTH = 64
	EXCLUDED_CHARACTERS = "[]{}()\"'`"

	def __init__(self):
		self.character_groups = [
			string.ascii_lowercase,
			string.ascii_uppercase,
			string.digits,
			string.punctuation
		]

	def generate(self, length: int, all_characters=False) -> str:
		length = min(max(length, self.MIN_LENGTH), self.MAX_LENGTH)
		password = str()
		while length > len(password):
			character = random.choice(self._sample(all_characters))
			if password:
				if self._char_type(password[-1]) != self._char_type(character):
					if character not in password:
						password += character
			else:
				if character.isalpha():  # Create the password starting with a letter
					password += character
		# Check if the password string has atleast a symbol character.
		if 'symbol' in list(map(self._char_type, list(password))):
			return password
		else:
			return self.generate(length, all_characters)

	def _sample(self, all_characters=False) -> str:
		if not all_characters:
			removed = set(string.punctuation).difference(set(self.EXCLUDED_CHARACTERS))
			self.character_groups.pop()
			self.character_groups.append(''.join(list(removed)))
		result = list()
		for group in self.character_groups:
			result += random.sample(group, k=2)
			random.shuffle(result)
		return ''.join(result)

	def _char_type(self, char: str) -> str:
		if char.isupper(): return 'uppercase'
		if char.islower(): return 'lowercase'
		if char.isdigit(): return 'digit'
		if not char.isalnum(): return 'symbol'
		if char.isspace(): return 'space'


if __name__ == '__main__':
	main()