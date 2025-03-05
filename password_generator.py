import random
import string
import argparse



class PasswordGenerator:
	
	CHARACTER_GROUPS = [
		string.ascii_lowercase,
		string.ascii_uppercase,
		string.digits,
		string.punctuation
	]

	# Excluded characters are brackets, quotes, slashes, semicolon and comma
	EXCLUDED_CHARACTERS = "[]{}()<>\"'`/\\;,"

	MIN_LENGTH = 12
	MAX_LENGTH = sum(map(len, CHARACTER_GROUPS)) - len(EXCLUDED_CHARACTERS)

	def __init__(self, length: int, all_characters=False):

		if not isinstance(length, int):
			raise TypeError("length must be an integer")

		self.length = min(max(length, self.MIN_LENGTH), self.MAX_LENGTH)
		self.all_characters = True if self.length == self.MAX_LENGTH else all_characters

	def generate(self) -> str:
		while True:
			password = self._create_password()
			character_types = list(map(self._character_type, password))

			if character_types.count('punctuation') >= 2 and character_types.count('uppercase') >= 2:
				return password

	def _create_password(self) -> str:
		password = ''
		while len(password) < self.length:
			character = random.choice(self._get_random_sample())

			if password and self._character_type(password[-1]) != self._character_type(character):
				if character not in password:
					password += character

			elif not password and character.isalpha():
				password += character

		return password

	def _get_random_sample(self) -> str:
		if not self.all_characters:
			punctuation = set(string.punctuation) - set(self.EXCLUDED_CHARACTERS)
			character_groups = self.CHARACTER_GROUPS[:-1] + [''.join(punctuation)]
		else:
			character_groups = self.CHARACTER_GROUPS

		result = []
		for index, group in enumerate(character_groups):
			sample_size = 3 if index % 2 == 0 else 2
			result.extend(random.sample(group, k=sample_size))

		return ''.join(result)

	def _character_type(self, character: str) -> str:
		if character.isupper(): return 'uppercase'
		if character.islower(): return 'lowercase'
		if character.isdigit(): return 'digit'
		if character in string.punctuation: return 'punctuation'
		return 'other'


def main():
    parser = argparse.ArgumentParser(description="Generate a secure password.")
    parser.add_argument("-l", "--length", type=int, default=12, help="Specify password length (minimum 12)")
    parser.add_argument("-a", "--all", action="store_true", help="Include all characters, including excluded ones")

    args = parser.parse_args()

    generator = PasswordGenerator(length=args.length, all_characters=args.all)
    password = generator.generate()
    print(password)


if __name__ == "__main__":
	main()
