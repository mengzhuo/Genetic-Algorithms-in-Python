#!/usr/bin/env python
# encoding: utf-8

import random

class Chromosome(object):

    gene_types = []
    size = 10
    
    def __repr__(self):
        return str(self._chromo[:5])

    def __init__(self, init=100):
        
        self.mutated = False
        if isinstance(init, int):
            # Random Chrome
            self._chromo = [random.choice(self.gene_types) for x in xrange(init)]
        else:
            self._chromo = init
    
    def __new__(cls, *args, **kwargs):

        if not cls.gene_types:
            raise Exception('Lack of Gene types')
        else:
            return super(Chromosome, cls).__new__(cls)
    
    def mutate(self, mutation_rate=0.01):
      
        if self.mutated:
            raise TypeError('This Chromo already mutated')

        for x in xrange(self.len):
            if random.random() < mutation_rate:
                self._chromo[x] = random.choice(self.gene_types)
        
        self.mutated = True

    def crossover(self, chromo):

        assert isinstance(chromo, Chromosome), '{0} not a Chromosome'.format(chromo)
        random_pos = random.randint(0, self.len)
        a, b = self._chromo[:random_pos], chromo._chromo[random_pos:]
        if random.choice([0, 1]):
            a, b = b, a
        return self.__class__(a+b)

    @property
    def len(self):
        return len(self._chromo)
    
    def __iter__(self):
        for x in self._chromo:
            yield x

class BitChromosome(Chromosome):

    gene_types = [0, 1]

class VimChromosome(Chromosome):

    gene_types = ['left', 'up', 'down', 'right']
