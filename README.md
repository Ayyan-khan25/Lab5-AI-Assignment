# Lab5-AI-Assignment
# Lab 5: Adversarial Search — Minimax & Alpha-Beta Pruning

## Artificial Intelligence Lab

**Week:** 5  
**Lectures:** L11–L12  
**CLO:** CLO2 (C3: Apply)  
**Programming Language:** Python.

---

## Student Information

- **Student Name:** M.Ayyan Khan 
- **Student ID:** 042
- **Course:** Artificial Intelligence Lab
- **Lab Number:** 5

---

## 1. Introduction

This lab focuses on two adversarial search algorithms used in Artificial Intelligence: Minimax and Alpha-Beta Pruning.

Minimax selects the best possible move by assuming that both players act optimally. MAX tries to maximize the score, while MIN tries to minimize it.

Alpha-Beta Pruning improves Minimax by skipping branches that cannot change the final decision. Both algorithms should return the same optimal value for the same game tree.

## 2. Objectives

- Understand MAX and MIN decisions in a game tree.
- Implement the Minimax algorithm in Python.
- Implement Alpha-Beta Pruning in Python.
- Count the number of evaluated leaf nodes.
- Compare both algorithms.
- Observe how branch ordering affects pruning efficiency.

## 3. Tasks Performed

### Task 1: Trace the Game Tree Using Minimax

The following leaf scores are used:

`[3, 5, 2, 9, 0, 7]`

The supplied Minimax implementation pads the scores with zeros to create a complete binary tree:

`[3, 5, 2, 9, 0, 7, 0, 0]`

The algorithm evaluates the tree from the leaves to the root.

**Calculated values:**

- MIN(3, 5) = 3
- MIN(2, 9) = 2
- MIN(0, 7) = 0
- MIN(0, 0) = 0
- MAX(3, 2) = 3
- MAX(0, 0) = 0
- Root MAX(3, 0) = 3

**Result:** The optimal Minimax value is 3.

### Task 2: Add a Leaf-Evaluation Counter

A counter is added to both algorithms to count how many terminal leaf nodes are evaluated.

The counter is incremented whenever the algorithm reaches the target depth and evaluates a leaf.

For the supplied complete tree and left-to-right traversal:

- Minimax evaluates 8 leaves.
- Alpha-Beta Pruning evaluates 7 leaves.
- Both algorithms return the root value 3.

**Reduction in evaluated leaves:**

Reduction = ((8 - 7) / 8) × 100 = 12.5%

This reduction applies to the specific tree and branch ordering used in this test.

### Task 3: Reorder Branches

The branch order is changed to investigate its effect on Alpha-Beta Pruning.

The algorithms are run again using the reordered tree.

The results are compared to verify that:

- Minimax evaluates all leaf nodes.
- Alpha-Beta Pruning may evaluate fewer leaves.
- Both algorithms return the same root value when the same game tree is preserved.
- The number of pruned branches depends on the order in which children are explored.

For a fair test, complete sibling subtrees should be swapped without changing the values or structure of the game tree.

## 4. Important Concepts

### Minimax

Minimax is a decision-making algorithm for two-player games.

- MAX selects the maximum child value.
- MIN selects the minimum child value.
- The final root value represents the optimal decision under the Minimax assumptions.

### Alpha-Beta Pruning

Alpha-Beta Pruning optimizes Minimax by avoiding unnecessary searches.

- **Alpha (α):** The best value MAX can guarantee so far.
- **Beta (β):** The best value MIN can guarantee so far.
- **Pruning condition:** `alpha >= beta`

When the pruning condition is satisfied, the remaining children of that node do not need to be explored.

## 5. Requirements

- Python 3
- Visual Studio Code or another Python editor
- Python extension for VS Code (recommended)

No additional Python packages are required.

## 6. Project File

The main Python file is:

`Lab5_Minimax_AlphaBeta.py`

This file contains the implementations and tests for Minimax, Alpha-Beta Pruning, leaf counting, and branch-order comparison.

## 7. How to Run the Program

1. Install Python 3 if it is not already installed.
2. Open the project folder in Visual Studio Code.
3. Create a file named `Lab5_Minimax_AlphaBeta.py`.
4. Paste the complete Python code into the file.
5. Save the file using `Ctrl + S`.
6. Open the VS Code terminal.
7. Run the following command:

```bash
python Lab5_Minimax_AlphaBeta.py
```

If the `python` command does not work on Windows, try:

```bash
py Lab5_Minimax_AlphaBeta.py
```

## 8. Expected Output

For the original supplied tree, the comparison should produce:

```text
Minimax value: 3
Minimax evaluated leaves: 8
Alpha-Beta value: 3
Alpha-Beta evaluated leaves: 7
Same root value: True
```

The exact leaf count may change when the branch ordering changes. The root value should remain unchanged when the underlying game tree and terminal scores are preserved.

## 9. Results and Discussion

The experiment demonstrates that Minimax and Alpha-Beta Pruning can return the same optimal game-tree value.

Minimax evaluates every leaf in the supplied complete tree. Alpha-Beta Pruning can avoid evaluating some leaves by using alpha and beta bounds.

In the original test, Minimax evaluates 8 leaves, while Alpha-Beta Pruning evaluates 7. This demonstrates a reduction in search effort without changing the root value.

The effectiveness of pruning depends on branch ordering. Better ordering can allow the algorithm to prune more branches.

## 10. Conclusion

Minimax and Alpha-Beta Pruning were implemented to solve a small adversarial game tree. The root value obtained by both algorithms was 3.

Alpha-Beta Pruning evaluated fewer leaves in the original test while preserving the Minimax result. Therefore, it can improve search efficiency in game-playing AI systems.

## 11. Reflection

**What did you learn?**

I learned how Minimax alternates between MAX and MIN nodes and how Alpha-Beta Pruning reduces unnecessary searches.

**How can this be applied in real AI systems?**

These algorithms can be used in game-playing systems such as Tic-Tac-Toe, checkers, and chess.

**What surprised you?**

Alpha-Beta Pruning can skip some leaf evaluations without changing the optimal result.

**What would you do differently?**

I would test different branch orderings and compare the number of evaluated leaves.

## 12. Submission Checklist

Submit the following items according to the instructor's requirements:

1. `Lab5_Minimax_AlphaBeta.py` — Python source code.
2. `README.md` — Lab description, instructions, results, and conclusion.
3. Screenshots showing the program running and its output.
4. Minimax trace table showing calculations from leaves to root.
5. Comparison of evaluated leaves for Minimax and Alpha-Beta Pruning.
6. Evidence of the branch-ordering test.
7. A short interpretation and reflection.

**Important:** Run the code yourself and capture the actual output. Update the README if your branch-ordering test produces different leaf counts.
