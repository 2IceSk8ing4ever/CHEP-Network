import requests
import json

# The function to determine the overall sentiment of a text body using an API
def sentiment_from_api(text_body, folder_name):

    # Define the maximum number of tokens that can be sent to the API in one request.
    MAX_TOKENS = 4097 - 20  # Reserve some tokens for system message and other overheads
    
    # If the text is too long, chunk it
    if len(text_body) > MAX_TOKENS:
        # Split the text_body into chunks
        chunks = [text_body[i:i + MAX_TOKENS] for i in range(0, len(text_body), MAX_TOKENS)]
        # Analyze the sentiment of each chunk individually.
        sentiments = [individual_sentiment_from_api(chunk, folder_name) for chunk in chunks]
        
        # Combine results - if any chunk is negative, return 'Negative'
        if 'Negative' in sentiments:
            return 'Negative'
        # If all chunks are positive, return 'Positive'.
        return 'Positive'
    
    else:
        # If the text is within the token limit, analyze sentiment directly.
        return individual_sentiment_from_api(text_body, folder_name)
    
# The function to analyze the sentiment of an individual chunk of text.
def individual_sentiment_from_api(text_chunk, folder_name):
    # API endpoint for sentiment analysis.
    url = "https://api.openai.com/v1/chat/completions"
    # Headers for the API request, including the authorization token.
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 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"  # Replace with your actual API key
        # "Authorization": "Bearer APIKEY"  # Replace with your actual API key
    }
    # Data payload for the API request, including the model and message.
    data = {
        # "model": "gpt-3.5-turbo",
        "model": "gpt-4", # Specify the model to use.
        "messages": [
            {
                "role": "system",
                "content": f"the flybuys company has a product named onepass. evaluate the below message and answer yes or no if the sentiment of the piece towards flybuys and onepass is positive.\n{text_chunk}"
            }
        ]
    }
    # Make the POST request to the API.
    response = requests.post(url, headers = headers, data = json.dumps(data))
    # Save the API response to a file in the specified folder.
    with open(f'{folder_name}/response.json', 'w') as fileout: 
        json.dump(response.json(), fileout, indent = 4)
    # Extract the answer from the API response and determine the sentiment.
    answer = response.json()['choices'][0]['message']['content'].lower()
    
    return 'Positive' if answer.startswith('y') else 'Negative'
