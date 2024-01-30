import re 
import google.generativeai as genai
from creds import GOOGLE_API_KEY

# Defining function for using in main.py file
# ------------------------------------------

# function for processing text(comming from concatenate_text_files) it remove duplication and clean the text 
def filtering_text(input_text):
    # Split the input text into lines
    lines = input_text.splitlines()
    unique_lines = []

    # Remove duplicates
    for line in lines:
        if line not in unique_lines:
            unique_lines.append(line)

    # Clean the text
    cleaned_lines = []

    for line in unique_lines:
        line = re.sub('…', '', line)
        line = re.sub('&amp;', '', line)
        line = re.sub('@[A-Za-z0-9]+', '', line)  # Removing @mentions
        line = re.sub('#', '', line)  # Removing '#' hash tag
        line = re.sub('|', '', line)  # Removing '|' sign
        line = re.sub('-', '', line)  # Removing '-' sign
        line = re.sub('_', '', line)  # Removing '_' sign
        line = re.sub(r'\*', '', line)  # Removing '*' sign
        line = re.sub('=', '', line)  # Removing '=' sign
        line = re.sub('https?:\/\/\S+', '', line)  # Removing hyperlink
        line = re.sub(' +', ' ', line)  # Removing double spaces
        line = re.sub(' {2,}', ' ', line)  # Removing two or more spaces and replacing with a single space
        cleaned_lines.append(line)

    # Join the cleaned lines back into a string
    cleaned_text = '\n'.join(cleaned_lines)

    return cleaned_text


# --------------------------

# function for reading and concatenating  multiple text files 
def concatenate_text_files(uploaded_files):
    concatenated_text = ""
    for uploaded_file in uploaded_files:
        content = uploaded_file.read()
        # Decode content from bytes to string
        decoded_content = content.decode('utf-8')
        concatenated_text += decoded_content + '\n'
        
    # calling the function to filter all text
    filtered_text= filtering_text(concatenated_text)

    return filtered_text



# -----------------------setting gemini model and genrating summary--------------------------

def gen_summary(text):
    # adding api key for gemini
    genai.configure(api_key=GOOGLE_API_KEY)
    # Set up the model
    generation_config = {
    "temperature": 0.8,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
    }

    safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    ]

    # creating moddel instance
    model = genai.GenerativeModel(model_name="gemini-pro",
                                generation_config=generation_config,
                                safety_settings=safety_settings)

    # context input text
    prompt_parts = [
        f"Please provide a summary for the following text and do not add any EXTRA TEXT ONLY PROVIDE SUMMARY an do not provide input text in output. Please use the provided symptoms, procedure,chemo and radiation details(if any), tests and results in the summary and please do not add patients personal information in adition generate, summary in a way a doctor would, for the patient to take it to an other hospital  : {text}",
    ]

    esponse = model.generate_content(prompt_parts)

    return esponse.text


if __name__ == "__main__":
    print("*****--Inside Main Functions--*****")

