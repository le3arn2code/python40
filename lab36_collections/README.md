# Lab 36: Using Collections (deque, Counter)

## Overview
In this lab, we explored Python’s `collections` module, focusing on **deque** and **Counter**.

## Errors & Fixes
- `python: command not found` → Fixed by using `python3`.
- `pip install` warning due to externally managed environment → Resolved with:
  ```bash
  python3 -m pip install beautifulsoup4 requests --break-system-packages
  ```

## Final Output
- **Deque**: Demonstrated O(1) appends/pops on both ends.
- **Counter**: Simplified counting word frequencies.

## Conclusion
The lab showed how `collections` provides efficient and clear solutions for queues and counting problems. 
We practiced error handling, confirmed outputs, and documented the fixes clearly.

