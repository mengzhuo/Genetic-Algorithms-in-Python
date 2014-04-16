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

def print_map(chromo, path):
   
    smap = TEST_MAP[:]
    for row in xrange(len(smap)):
        for col,val in enumerate(smap[row]):
            
            if val == 1:
                smap[row][col] = u"#"
            if val == 0:
                smap[row][col] = u' '

    for x,y in path:
        try:
            smap[y][x] = '.'
        except IndexError:
            pass

    result = ""
    for row in smap:
        result += u"{0}\n".format(u''.join([str(col) for col in row]))
    return result


def cal_fitness(chromo, result_path=False):
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

        if (x,y) in path:
            break
        if grid.point == 0:
            path.append((x,y))
        elif grid.point == 8:
            path.append((x,y))
            if result_path:
                return path
            return 1
        elif grid.point == 1:
            break
        elif grid.point == 5:
            return 0

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
    init_group = [VimChromosome(20) for x in xrange(100)]
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
            smap = print_map(best[1], cal_fitness(best[1], True))
            print smap
            break
        print "Current Best:{0}\n{1}".format(best[0], best[1]._chromo)
       
        while len(children) < 100:
            if  random.uniform(0, 1) <= CROSSOVER_RATE:
                father = weigth_choice(fit_group)
                mother = weigth_choice(fit_group)
            
                new_borned = father.crossover(mother)
                new_borned.mutate()
                children.append(new_borned)

        fit_group = sorted([(cal_fitness(x),x) for x in children],
                        key=lambda x:-x[0])
        epoch += 1

if __name__ == '__main__':
    main()
