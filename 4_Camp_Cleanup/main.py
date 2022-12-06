def camp_cleanup(in_file):
    total_overlap = 0
    any_overlap = 0
    with open(in_file, 'r') as f:
        for line in f:
            interval1, interval2 = line.split(',')
            interval2 = interval2.rstrip()
            if is_overlap(interval1, interval2): total_overlap += 1
            if is_any_overlap(interval1, interval2): any_overlap += 1
    return total_overlap, any_overlap

def is_any_overlap(interval1, interval2):
    o1, c1 = [int(s) for s in interval1.split('-')]
    o2, c2 = [int(s) for s in interval2.split('-')]
    if o1 == o2:
        return True
    elif o1 < o2:
        return c1 >= o2
    else:
        return c2 >= o1

def is_overlap(interval1, interval2):
    o1, c1 = [int(s) for s in interval1.split('-')]
    o2, c2 = [int(s) for s in interval2.split('-')]
    if o1 == o2:
        return True
    elif o1 < o2:
        return c2 <= c1
    else:
        return c1 <= c2

def main():
    part1, part2 = camp_cleanup('input.txt')
    print(f'Part 1: {part1}, Part2: {part2}')

if __name__ == "__main__":
    main() 