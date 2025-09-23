# Interview Q&A - Lab 37 BFS/DFS

### 1. What is BFS?
BFS is Breadth-First Search, which explores neighbors level by level using a queue.

### 2. What is DFS?
DFS is Depth-First Search, which explores as deep as possible before backtracking, typically using recursion or a stack.

### 3. Which data structure does BFS use?
A queue (FIFO).

### 4. Which data structure does DFS use?
A stack (explicitly) or recursion (implicitly).

### 5. Use case for BFS?
Finding shortest path in an unweighted graph.

### 6. Use case for DFS?
Exploring all possible paths, backtracking problems like Sudoku.

### 7. Time complexity of BFS and DFS?
Both are O(V + E), where V = vertices and E = edges.

### 8. Space complexity difference?
- BFS: O(V) due to queue storage.
- DFS: O(V) due to recursion stack.

### 9. What happens if graph has cycles?
Need a visited set to avoid infinite loops.

### 10. Key difference summary?
- BFS explores level by level.
- DFS explores depth before breadth.
