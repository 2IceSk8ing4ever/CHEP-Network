# The function to check the appearance of company name variants in different segments of content.
def check_name_appearance(content, company_variants):
    # Split the content into words
    words = content.split()
    # Calculate the total number of words in the content.
    total_length = len(words)
    
    # Calculate indices for 30%, 50%, and 80% of the total content length.
    index_30 = int(total_length * 0.3)
    index_50 = int(total_length * 0.5)
    index_80 = int(total_length * 0.8)

    # Convert content to lowercase for case-insensitive checking
    content = content.lower()

    # Get content for each segment
    content_30 = ' '.join(words[:index_30])
    content_50 = ' '.join(words[:index_50])
    content_80 = ' '.join(words[:index_80])

    # Check if any company name variant appears in each segment
    appears_30 = any(variant in content_30 for variant in company_variants)
    appears_50 = any(variant in content_50 for variant in company_variants)
    appears_80 = any(variant in content_80 for variant in company_variants)

    return {
        'appears_in_30_percent': appears_30,
        'appears_in_50_percent': appears_50,
        'appears_in_80_percent': appears_80
    }