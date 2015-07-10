__author__ = 'sapphire'

import heapq
import yaml

from utils import NGramIterator


class NGramProfile:
    """A class representing a n-gram profile
    """

    def __init__(self, grams, name=None):
        self.profile = dict()
        for k in xrange(len(grams)):
            self.profile[grams[k]] = k
        self.name = name

    def compare(self, other):
        total = 0
        max_score = max(len(self.profile), len(other.profile))
        for gram, position in other.profile.iteritems():
            score = max_score
            if gram in self.profile:
                score = abs(position - self.profile[gram])
            total += score
        return total


def build_profile(f, max_n=5, size=300):
    """Build n-gram character profile from a file

    :param f: input file
    :param max_n: max gram to count
    :param size: size of the profile
    :return: a profile of given size
    """
    counts = dict()
    for n in xrange(1, max_n + 1):
        f.seek(0)
        iterator = NGramIterator(f, n)
        for gram in iterator:
            counts[gram] = counts.get(gram, 0) + 1
    counts = heapq.nlargest(size, counts.iteritems(), key=lambda item: item[1])
    grams = list()
    for count in counts:
        grams.append(count[0])
    return NGramProfile(grams)


def dump_profile(profile, path):
    with open(path, 'w') as f:
        f.write(yaml.dump(profile))


def load_profile(path):
    with open(path, 'r') as f:
        return yaml.load(f)
