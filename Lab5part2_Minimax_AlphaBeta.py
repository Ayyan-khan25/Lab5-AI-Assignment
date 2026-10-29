import math

def minimax(depth, index, max_turn, scores, target_depth, counter):
    if depth == target_depth:
        counter[0] += 1
        return scores[index]

    if max_turn:
        left = minimax(depth + 1, index * 2, False,
                       scores, target_depth, counter)
        right = minimax(depth + 1, index * 2 + 1, False,
                        scores, target_depth, counter)
        return max(left, right)
    else:
        left = minimax(depth + 1, index * 2, True,
                       scores, target_depth, counter)
        right = minimax(depth + 1, index * 2 + 1, True,
                        scores, target_depth, counter)
        return min(left, right)


def alphabeta(depth, index, max_turn, scores, target_depth,
              alpha, beta, counter):
    if depth == target_depth:
        counter[0] += 1
        return scores[index]

    if max_turn:
        value = float("-inf")
        for i in range(2):
            child = alphabeta(depth + 1, index * 2 + i, False,
                              scores, target_depth, alpha, beta, counter)
            value = max(value, child)
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float("inf")
        for i in range(2):
            child = alphabeta(depth + 1, index * 2 + i, True,
                              scores, target_depth, alpha, beta, counter)
            value = min(value, child)
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value


scores = [3, 5, 2, 9, 0, 7, 0, 0]
depth = int(math.log2(len(scores)))

mini_count = [0]
mini_value = minimax(0, 0, True, scores, depth, mini_count)

ab_count = [0]
ab_value = alphabeta(0, 0, True, scores, depth,
                     float("-inf"), float("inf"), ab_count)

print("Minimax value:", mini_value)
print("Minimax evaluated leaves:", mini_count[0])
print("Alpha-Beta value:", ab_value)
print("Alpha-Beta evaluated leaves:", ab_count[0])
print("Same root value:", mini_value == ab_value)
