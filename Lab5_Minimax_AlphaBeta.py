import math

leaf_count = 0

def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    global leaf_count

    if curDepth == targetDepth:
        leaf_count += 1
        return scores[nodeIndex]

    if maxTurn:
        left = minimax(curDepth + 1, nodeIndex * 2,
                       False, scores, targetDepth)
        right = minimax(curDepth + 1, nodeIndex * 2 + 1,
                        False, scores, targetDepth)
        return max(left, right)
    else:
        left = minimax(curDepth + 1, nodeIndex * 2,
                       True, scores, targetDepth)
        right = minimax(curDepth + 1, nodeIndex * 2 + 1,
                        True, scores, targetDepth)
        return min(left, right)

scores = [3, 5, 2, 9, 0, 7]
treeDepth = math.ceil(math.log2(len(scores)))
scores += [0] * (2**treeDepth - len(scores))

result = minimax(0, 0, True, scores, treeDepth)
print("Optimal Minimax value:", result)
print("Evaluated leaves:", leaf_count)
