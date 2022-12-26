from collections import deque
import re

def supply_stack(in_file, num_stacks):
    stacks_1 = [deque() for _ in range(num_stacks)]
    stacks_2 = [deque() for _ in range(num_stacks)]
    num_parse = r"[0-9]+"
    with open(in_file, 'r') as f:
        for line in f:
            if line[0] == 'm':
                # process instructions
                freq, fro, to = re.findall(num_parse, line)
                part_1_policy(stacks_1, freq, to, fro)
                part_2_policy(stacks_2, freq, to, fro)
            else:
                # create stacks
                cur_stack = 0
                for i in range(0, len(line), 4):
                    if line[i] == '[':
                        stacks_1[cur_stack].append(line[i + 1])
                        stacks_2[cur_stack].append(line[i + 1])
                    cur_stack += 1
    # return tops elems of stack
    top_elems_1 = ""
    top_elems_2 = ""
    for stack_1, stack_2 in zip(stacks_1, stacks_2):
        top_elems_1 += stack_1[0] if len(stack_1) else ""
        top_elems_2 += stack_2[0] if len(stack_2) else ""
    return top_elems_1, top_elems_2


def part_1_policy(stacks, freq, to, fro):
    for _ in range(int(freq)):
        to_push = stacks[int(fro) - 1].popleft()
        stacks[int(to) - 1].appendleft(to_push)

def part_2_policy(stacks, freq, to, fro):
    t_stack = deque()
    for _ in range(int(freq)):
        t_stack.append(stacks[int(fro) - 1].popleft())
    for _ in range(len(t_stack)):
        stacks[int(to) - 1].appendleft(t_stack.pop())
 
def main():
    sol1, sol2 = supply_stack('input.txt', 9)
    print(f"Part 1: {sol1}, Part 2: {sol2}")

if __name__ == "__main__":
    main()