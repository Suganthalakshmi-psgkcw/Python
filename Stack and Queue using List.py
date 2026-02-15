# -------- Stack --------
stack = []

print("--- Stack ---")

# Push operation
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack:", stack)

# Peek operation
print("Peek:", stack[-1])

# Pop operation
stack.pop()
print("After Pop:", stack)


# -------- Queue --------
queue = []

print("\n--- Queue ---")

# Enqueue operation
queue.append(10)
queue.append(20)
queue.append(30)

print("Queue:", queue)

# Dequeue operation
queue.pop(0)
print("After Dequeue:", queue)
