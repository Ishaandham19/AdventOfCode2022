def rugsack_reorganization_1(in_file):
    total_score = 0
    with open(in_file, 'r') as f:
        for line in f:
            str1, str2 = line[:len(line) // 2], line[len(line) // 2:]
            set1 = set(str1)
            for c in str2:
                if c in set1:
                    total_score += priority(c)
                    break
    return total_score

def rugsack_reorganization_2(in_file):
    total_score = 0
    with open(in_file, 'r') as f:
        while True:
            line1 = f.readline()
            line2 = f.readline()
            line3 = f.readline()
            if not line3: break  # EOF
            set1, set2 = set(line1), set(line2)
            for c in line3:
                if c in set1 and c in set2:
                    total_score += priority(c)
                    break
    return total_score 


def priority(c: str) -> int:
    if c.islower():
        return ord(c) - ord('a') + 1
    return ord(c) - ord('A') + 27

def main():
    part1, part2 = rugsack_reorganization_1('input.txt'), rugsack_reorganization_2('input.txt')  
    print(f'Part 1: {part1}, Part 2: {part2}')

if __name__ == "__main__":
    main()