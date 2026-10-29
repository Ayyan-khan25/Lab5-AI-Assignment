def swap_children_at_every_level(values):
    # This works for a complete binary tree represented as leaf values.
    # Swap adjacent leaf pairs, then swap adjacent pairs of subtrees at larger levels.
    result = values[:]
    n = len(result)
    block = 2
    while block <= n:
        half = block // 2
        for start in range(0, n, block):
            left = result[start:start + half]
            right = result[start + half:start + block]
            result[start:start + block] = right + left
        block *= 2
    return result

# A simpler, clearly controlled ordering test:
# Keep the original tree and swap the two children at each MIN node.
original = [3, 5, 2, 9, 0, 7, 0, 0]
reordered = []
for i in range(0, len(original), 2):
    reordered.extend([original[i + 1], original[i]])

print("Original leaves:", original)
print("Reordered leaves:", reordered)

# Re-run the comparison code from Task 2 twice:
# 1) scores = original
# 2) scores = reordered
# Reset mini_count = [0] and ab_count = [0] before each run.
