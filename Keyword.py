# The function to count the occurrences of each keyword in a given content.
def keyword_occurrences(keywords, content):
    # Initialize an empty dictionary to store the count of each keyword.
    result = {}

    # Iterate through each keyword in the provided list of keywords.
    for keyword in keywords:
        # Count the occurrences of the keyword in the content. 
        # The counting is case-insensitive to ensure all variations are counted.
        count = content.lower().count(keyword.lower())  # case-insensitive count
        # If the keyword is found in the content, add it to the result dictionary.
        if count > 0:
            result[keyword] = count
    
    # Check if the result dictionary is empty (no keywords found).
    if not result:
        return "None" # Return the string "None" if no keywords were found.
    
    return result


