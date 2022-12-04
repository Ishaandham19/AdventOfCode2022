def count_calories_1(in_file):
    max_calories = float('-inf')
    with open(in_file, 'r') as f:
        cur_calories = 0
        for line in f:
            if line == '\n':
                max_calories = max(max_calories, cur_calories)
                cur_calories = 0
            else:
                cur_calories += int(line)
    return max_calories

def count_calories_2(in_file):
    cal_1 = cal_2 = cal_3 = float('-inf')
    with open(in_file, 'r') as f:
        cur_calories = 0
        for line in f:
            if line == '\n':
                if cur_calories > cal_1:
                    cal_3 = cal_2
                    cal_2 = cal_1
                    cal_1 = cur_calories
                elif cur_calories > cal_2:
                    cal_3 = cal_2
                    cal_2 = cur_calories
                elif cur_calories > cal_3:
                    cal_3 = cur_calories
                cur_calories = 0
            else:
                cur_calories += int(line)
    return cal_1 + cal_2 + cal_3

def main():
    part_1 = count_calories_1('input.txt')
    part_2 = count_calories_2('input.txt')
    print(f"Part 1: {part_1}, Part 2: {part_2}")

if __name__ == "__main__":
    main()
