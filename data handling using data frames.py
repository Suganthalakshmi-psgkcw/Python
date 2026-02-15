# Original list
nums = [10, 20, 30, 40, 50]
print("Original:", nums)

# List operations
nums.append(60)      # Add element at end
nums.insert(1, 15)   # Insert at index 1
nums.remove(30)      # Remove specific value

nums.pop()           # Remove last element
print("Modified:", nums)

# Sorting
nums.sort()
print("Sorted:", nums)

# Reverse
nums.reverse()
print("Reversed:", nums)

# Built-in functions
print("Length:", len(nums))
print("Max:", max(nums))
print("Min:", min(nums))
print("Sum:", sum(nums))

# Copy list
new_list = nums.copy()
print("Copied List:", new_list)

# Clear list
nums.clear()
print("Cleared List:", nums)
