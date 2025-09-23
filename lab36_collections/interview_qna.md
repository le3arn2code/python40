# Lab 36 - Interview Q&A

### 1. What is a deque?
A deque is a double-ended queue that allows O(1) appends and pops from both ends.

### 2. Why use deque over list?
Deque is optimized for operations on both ends, unlike lists where insert/pop at start is O(n).

### 3. Common use cases of deque?
Queues, BFS algorithms, browser history, sliding window problems.

### 4. What is Counter?
Counter is a subclass of dict that counts hashable objects.

### 5. When would you use Counter?
When frequency analysis is needed (e.g., most common words).

### 6. How to get the most common items in Counter?
Using `.most_common(n)`.

### 7. What happens if you pop from an empty deque?
It raises an `IndexError`.

### 8. Can Counter handle negative counts?
Yes, if you subtract counts, negative values can appear.

### 9. Performance advantage of deque?
Append and pop are O(1), while list’s pop(0) is O(n).

### 10. Real-world use of Counter?
Counting log file errors, word frequencies in text, inventory counts.
