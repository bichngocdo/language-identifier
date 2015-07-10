__author__ = 'sapphire'


class CharacterIterator:
    """An iterator that reads from a file char by char
    """

    def __init__(self, f):
        self.file = f
        self.line = None
        self.pos = -1

    def __iter__(self):
        return self

    def next(self):
        if self.line is None:
            self.line = self.file.readline()
            self.pos = 0
            if self.line is None:
                raise StopIteration
        c = self.line[self.pos]
        self.pos += 1
        if self.pos == len(self.line):
            self.line = None
        return c


class NGramIterator:
    """An iterator that reads from a file a gram of n characters each time, normalizes every blank space to a dash,
     discard other characters except letters and apostrophes
    """

    def __init__(self, f, n):
        self.iterator = CharacterIterator(f)
        self.no_grams = n
        self.blank_symbol = '_'
        self.gram = self.blank_symbol * self.no_grams
        self.include = '\''

    def __iter__(self):
        return self

    def next(self):
        try:
            c = self.iterator.next()
        except:
            c = None
        if c is None:
            if self.gram[1:] == self.blank_symbol * (self.no_grams - 1):
                raise StopIteration
            else:
                self.gram = self.gram[1:] + self.blank_symbol
        elif c.isspace():
            self.gram = self.gram[1:] + self.blank_symbol
        elif c.isalpha() or c in self.include:
            self.gram = self.gram[1:] + c
        else:
            return self.next()
        return self.gram
