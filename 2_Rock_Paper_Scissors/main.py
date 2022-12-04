def rock_paper_scissors(in_file):
    points = {'R': 1, 'P': 2, 'S': 3}
    conversion = {'A': 'R', 'B' : 'P', 'C' : 'S', 'X' : 'R', 'Y' : 'P', 'Z' : 'S'}
    WIN_SCORE, DRAW_SCORE, LOSS_SCORE = 6, 3, 0
    total_points = 0

    def rpc_sovler(p1, p2):
        p1 = conversion[p1]
        p2 = conversion[p2]
        # Draw
        if p1 == p2:
            return DRAW_SCORE + points[p1]
        if p1 == 'R':
            if p2 == 