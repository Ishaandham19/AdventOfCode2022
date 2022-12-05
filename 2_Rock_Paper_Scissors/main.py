def rock_paper_scissors_1(in_file) -> int:
    points = {'R': 1, 'P': 2, 'S': 3}
    conversion = {'A': 'R', 'B' : 'P', 'C' : 'S', 'X' : 'R', 'Y' : 'P', 'Z' : 'S'}
    WIN_SCORE, DRAW_SCORE, LOSS_SCORE = 6, 3, 0
    total_points = 0
    def rpc_sovler(p1, p2):
        p1 = conversion[p1]
        p2 = conversion[p2]
        lost_score = LOSS_SCORE + points[p1]
        win_score = WIN_SCORE + points[p1]
        draw_score = DRAW_SCORE + points[p1]
        if p1 == p2:
            return draw_score
        if p1 == 'R':
            return win_score if p2 == 'S' else lost_score
        if p1 == 'S':
            return win_score if p2 == 'P' else lost_score
        if p1 == 'P':
            return win_score if p2 == 'R' else lost_score
    with open(in_file, 'r') as f:
        for line in f:
            opp, player = line.split(' ')
            player = player.rstrip()
            total_points += rpc_sovler(player, opp)
    return total_points

def rock_paper_scissors_2(in_file) -> int:
    points = {'R': 1, 'P': 2, 'S': 3}
    conversion = {'A': 'R', 'B' : 'P', 'C' : 'S'}
    WIN_SCORE, DRAW_SCORE, LOSS_SCORE = 6, 3, 0
    total_points = 0
    def rpc_predictor(outcome, p1) -> str:
        p1 = conversion[p1]
        win_outcome = {'R' : 'S', 'S': 'P', 'P': 'R'}
        loss_outcome = {'S' : 'R', 'P': 'S', 'R' : 'P'}
        if outcome == 'Y':
            return DRAW_SCORE + points[p1]
        if outcome == 'X':
            return LOSS_SCORE + points[win_outcome[p1]]
        if outcome == 'Z':
            return WIN_SCORE + points[loss_outcome[p1]]
    with open(in_file, 'r') as f:
        for line in f:
            opp, outcome = line.split(' ')
            outcome = outcome.rstrip()
            total_points += rpc_predictor(outcome, opp)
    return total_points

def main():
    part1, part2 = rock_paper_scissors_1('input.txt'), rock_paper_scissors_2('input.txt')
    print(f'Part 1: {part1}, Part 2: {part2}')

if __name__ == "__main__":
    main()