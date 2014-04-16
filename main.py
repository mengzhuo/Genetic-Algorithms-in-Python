#!/usr/bin/env python
# encoding: utf-8

import random
from maps import Map, TEST_MAP
from chromo import VimChromosome


CROSSOVER_RATE = 0.618
MUTATION_RATE = 0.001

START_GRID = (0, 2)
END_GRID = (14, 7)

GRIDS = Map(TEST_MAP)

def wheel_select(groups):

    pass

def cal_fitness(chromo):
    x, y = START_GRID
    path = []
    for vet in chromo:
        if vet == 'left':
            x -= 1
        elif vet == 'down':
            y += 1
        elif vet == 'up':
            y -= 1
        elif vet == 'right':
            x += 1
        else:
            raise ValueError('Mutation is beyond HJKL')

        try:
            grid = GRIDS[y][x]
        except IndexError:
            break
        if (x,y ) in path:
            return 0 
        if grid.point == 0:
            path.append((x,y))
        elif grid.point == 8:
            path.append((x,y))
            return 1
        elif grid.point in (5, 1):
            break

    if path and path[-1]:
        return 1/float(abs(END_GRID[0] - path[-1][0])+abs(END_GRID[1] - path[-1][1])+1)
    return 0

def weigth_choice(groups):

    total_p = reduce(lambda s, x:s+x, [ x[0] for x in groups])

    seed = random.uniform(0, total_p)

    upto = 0

    for weigth, content  in groups:
        if upto+weigth >= seed:
            return content
        upto += weigth
    raise Exception('No!!')

def main():
    winner = None
    init_group = [VimChromosome(70) for x in xrange(100)]
    fit_group = sorted([(cal_fitness(x),x) for x in init_group],
                        key=lambda x:-x[0])
    print "start"
    epoch = 0
    while not winner:
        # Epoch
        print "Epoch:{0}---Population:{1}".format(epoch, len(fit_group) )

        children = []

        best = fit_group[0]
        if best[0] >= 1:
            winner = best
            print "We have a winner {0}:{1._chromo}".format(best[0], best[1])
            break
        print "Current Best:{0}\n{1}".format(best[0], best[1]._chromo)
       
        while len(children) <= 100:
            if  random.uniform(0, 1) <= CROSSOVER_RATE:
                father = weigth_choice(fit_group)
                mother = weigth_choice(fit_group)
            
                new_borned = father.crossover(mother)
                children.append(new_borned)

        fit_group = sorted([(cal_fitness(x),x) for x in children],
                        key=lambda x:-x[0])
        print children[:2]
        epoch += 1

if __name__ == '__main__':
    main()
