# Create a list
nums = [10, 20, 30, 40, 50]
print("Original:", nums)

# List modifications
nums.append(60)        # Add 60 at the end
nums.insert(1, 15)     # Insert 15 at index 1
nums.remove(30)        # Remove value 30
nums.pop()             # Remove last element

print("Modified:", nums)

# Sorting
nums.sort()
print("Sorted:", nums)

# Reversing
nums.reverse()
print("Reversed:", nums)

# List operations
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
