from random import SystemRandom


class CodeGenerator:

    def __init__(self):
        self.generator = SystemRandom()

    def generate_token(self, count):
        alphabet = u'9ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return self.generate(alphabet, count)

    def generate_number_code(self, count):
        alphabet = u'0123456789'
        return self.generate(alphabet, count)

    def generate(self, alphabet, count):
        return u''.join(self.generator.choice(alphabet) for _ in range(count))
