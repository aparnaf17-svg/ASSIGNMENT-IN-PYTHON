feedback_data = {
'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],
'Feedback': [
' Very GOOD Service!!!',
'poor support, not happy ',
'GREAT experience! will come again.',
'okay okay...',
' not BAD',
'Excellent care, excellent staff!',
'good food and good ambience!',
'Poor response and poor handling of issue',
'Satisfied. But could be better.',
'Good support... quick service.'
],
'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}

try:
    num_additional = int(input("Enter how many more feedbacks you want to add: "))
except ValueError:
    num_additional = 0

# Automatically determine the next S_No starting from 11 onward
current_s_no = max(feedback_data['S_No']) + 1 if feedback_data['S_No'] else 1

for i in range(num_additional):
    print(f"\nEntering details for feedback #{current_s_no}:")
    name = input("Enter Name: ")
    feedback_text = input("Enter Written Feedback: ")
    
    while True:
        try:
            rating = int(input("Enter Rating (1–5): "))
            if 1 <= rating <= 5:
                break
            print("Error: Rating must be between 1 and 5.")
        except ValueError:
            print("Error: Please enter a valid integer for the rating.")
            
    feedback_data['S_No'].append(current_s_no)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(feedback_text)
    feedback_data['Rating'].append(rating)
    current_s_no += 1

# ==========================================
# STEP 3: Text Cleaning
# ==========================================
cleaned_feedbacks = []
for text in feedback_data['Feedback']:
    # Remove punctuation (., ,, !, ?)
    for p in ['.', ',', '!', '?']:
        text = text.replace(p, ' ')
    
    # Convert all text to lowercase
    text = text.lower()
    
    # Replace multiple spaces with a single space and remove leading/trailing spaces
    text = ' '.join(text.split())
    cleaned_feedbacks.append(text)

# Update feedback_data with cleaned feedbacks
feedback_data['Feedback'] = cleaned_feedbacks


# ==========================================
# STEP 4: Word Count Insights
# ==========================================
def count_word_in_feedbacks(word):
    """Returns how many feedbacks contain the given word (case-insensitive)."""
    word = word.lower()
    count = 0
    for fb in feedback_data['Feedback']:
        words_list = fb.split()
        if word in words_list:
            count += 1
    return count

print("\n--- Word Count Insights ---")
print(f"Number of feedbacks containing 'good': {count_word_in_feedbacks('good')}")
print(f"Number of feedbacks containing 'poor': {count_word_in_feedbacks('poor')}")
print(f"Number of feedbacks containing 'excellent': {count_word_in_feedbacks('excellent')}")


# ==========================================
# STEP 5: Final Summary & Insights
# ==========================================
print("\n--- Final Cleaned Feedback Data Dictionary ---")
for key, values in feedback_data.items():
    print(f"{key}: {values}")

# Calculate average rating
total_ratings = sum(feedback_data['Rating'])
total_entries = len(feedback_data['Rating'])
avg_rating = total_ratings / total_entries if total_entries > 0 else 0
print(f"\nAverage Rating: {avg_rating:.2f}")

# Find feedback with the longest comment (in terms of word count)
longest_index = 0
max_word_count = 0
for idx, fb in enumerate(feedback_data['Feedback']):
    word_count = len(fb.split())
    if word_count > max_word_count:
        max_word_count = word_count
        longest_index = idx

print(f"\nLongest Comment (Word Count: {max_word_count}):")
print(f"Name: {feedback_data['Name'][longest_index]}")
print(f"Feedback: '{feedback_data['Feedback'][longest_index]}'")
print(f"Rating: {feedback_data['Rating'][longest_index]}")

# Collect unique words used across all feedbacks (avoiding duplicates)
unique_words = set()
for fb in feedback_data['Feedback']:
    unique_words.update(fb.split())

print(f"\nUnique Words Used Across All Feedbacks ({len(unique_words)} words total):")
print(sorted(list(unique_words)))

# Optional: Sort feedbacks by rating (highest to lowest) using zip() and sorted()
print("\n--- Feedbacks Sorted by Rating (Highest to Lowest) ---")
combined_feedbacks = list(zip(
    feedback_data['S_No'],
    feedback_data['Name'],
    feedback_data['Feedback'],
    feedback_data['Rating']
))

# Sort based on rating (index 3) in descending order
sorted_feedbacks = sorted(combined_feedbacks, key=lambda x: x[3], reverse=True)

print(f"{'S_No':<6} | {'Name':<10} | {'Rating':<6} | {'Feedback'}")
print("-" * 65)
for item in sorted_feedbacks:
    print(f"{item[0]:<6} | {item[1]:<10} | {item[3]:<6} | {item[2]}")