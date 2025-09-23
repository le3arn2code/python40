from collections import deque, Counter

print("=== Deque Example ===")
d = deque()
d.append('task1')
d.append('task2')
print("Deque after appending:", d)
last_task = d.pop()
print("Popped from the right:", last_task)
d.appendleft('task0')
print("Deque after appendleft:", d)
first_task = d.popleft()
print("Popped from the left:", first_task)
print("Final Deque:", d)

print("\n=== Counter Example ===")
words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
word_count = Counter(words)
print("Word Count:", word_count)
print("Most Common Words:", word_count.most_common(2))
