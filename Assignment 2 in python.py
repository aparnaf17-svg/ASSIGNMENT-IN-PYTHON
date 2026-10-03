# a. Create age_list with five integer elements
age_list = [24, 25, 26, 27, 28]

# b. Create name_list with five string elements
name_list = ["Aarav", "Diya", "Kiran", "Meera", "Rahul"]

print("Initial age_list:", age_list)
print("Initial name_list:", name_list)

# a. Append the string "Yazhini" to name_list
name_list.append("Yazhini")
print("After append:", name_list)

# b. Insert the element 30 at index 2 in age_list
age_list.insert(2, 30)
print("After insert(2, 30):", age_list)

# c. Remove the string "Yazhini" from name_list
name_list.remove("Yazhini")
print("After remove('Yazhini'):", name_list)

# d. Pop the last element from age_list
popped_element = age_list.pop()
print("Popped element:", popped_element)
print("After pop():", age_list)

# e. Extend the age_list with additional ages [29, 30, 26]
age_list.extend([29, 30, 26])
print("After extend([29, 30, 26]):", age_list)

# f. Sort age_list in descending order
age_list.sort(reverse=True)
print("Sorted age_list (descending):", age_list)

# g. Find Max age, Min age, and sum of all ages from age_list
max_age = max(age_list)
min_age = min(age_list)
total_sum = sum(age_list)

print(f"Max Age: {max_age}")
print(f"Min Age: {min_age}")
print(f"Sum of Ages: {total_sum}")
# a. Print the first element of name_list
print("First element:", name_list[0])

# b. Print the last element of name_list
print("Last element:", name_list[-1])

# c. Print the elements from index 2 to index 4 in name_list
# Note: In Python slicing, the end index is exclusive, so we use 2 to 5 to include index 4.
print("Elements from index 2 to 4:", name_list[2:5])

# d. Print the elements of name_list in reverse order
print("Reverse order:", name_list[::-1])

# a. Create a dictionary named student_marks
student_marks = {
    "Aarav": 88,
    "Diya": 92,
    "Kiran": 75,
    "Meera": 84,
    "Rahul": 68
}
print("Initial student_marks:", student_marks)

# b. Access and print the mark of a specific student
print("Mark of Diya:", student_marks["Diya"])

# c. Add a new student "Janani" with a mark of 80
student_marks["Janani"] = 80
print("After adding Janani:", student_marks)

# d. Update the mark of an older student to 82 (Updating Rahul's mark)
student_marks["Rahul"] = 82
print("After updating Rahul's mark:", student_marks)

# e. Use keys(), values(), and items() methods
print("\n--- Dictionary Methods ---")
print("Keys:", student_marks.keys())
print("Values:", student_marks.values())
print("Items:", student_marks.items())

# Create my_set with duplicate elements
my_set = set(['a', 'e', 'i', 'o', 'u', 'a', 'a', 'i'])
print("my_set output:", my_set)
try:
    my_set[4] = 's'
except TypeError as e:
    print("TypeError caught:", e)

# c. Create two sets
set1 = {1, 3, 5, 7, 9}
set2 = {2, 3, 5, 8, 10}

# d. Compute and print union and intersection
union_result = set1.union(set2)
intersection_result = set1.intersection(set2)

print("Set 1:", set1)
print("Set 2:", set2)
print("Union of set1 and set2:", union_result)
print("Intersection of set1 and set2:", intersection_result)

# Performance Category Program

# 1. Prompt user for input
score = float(input("Enter your score (0 to 10): "))

# 2. Check conditions and print the exact plain text message
if score > 7:
    print("Above Average: Excellent work! You have mastered the concepts.")
elif 4 <= score <= 7:
    print("Average: Good effort! Keep practicing, there's room for improvement.")
elif 0 <= score < 4:
    print("Below Average: Need to improve your performance, consistent practice will lead to better results.")
else:
    print("Invalid score! Please enter a number between 0 and 10.")


