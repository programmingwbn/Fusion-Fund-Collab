import requests
from bs4 import BeautifulSoup
from django.http import JsonResponse
from rest_framework.response import Response
from transformers import BartTokenizer, BartForConditionalGeneration
from requests.structures import CaseInsensitiveDict

maxLength = 600

# Saves all the text in dictionary to be later converted into excel sheet
def summarize(model, url):
    from excel import weeklySummary
    import datetime
    
    command = "This is a text which mentions updates and work about this current ai technology. Identify the points which will help us decide if we should invest in this technology or its products as a venture capitalist:"

    mainText = getContent(url)

    times = int(len(mainText)/maxLength)

    for i in range(times):
        text_to_summarize = mainText[:maxLength]
        print(model)
        print(len(mainText))
		

        # Get the current date
        date = datetime.date.today().strftime('%d-%m-%Y')

        summaryBart = getBart(text_to_summarize, command)
        # summaryRazor = getRazor(text_to_summarize)
        # summaryBart = "test"
        summaryRazor = "test"

        summary = {"Model" : model, 
        "Date" : date, 
        "Collected_Text" : text_to_summarize, 
        "Summary_Bart" : summaryBart, 
        "Summary_TextRazor" : summaryRazor}

        weeklySummary.append(summary)

        if(len(mainText) > maxLength):
            mainText = mainText[maxLength:]
    

def getHeaders(url):
	title = ""

	try:
		response = requests.get(url)
		response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes

		if response.status_code == 200:
			soup = BeautifulSoup(response.text, 'html.parser')
			
			# article_titles = soup.find_all('title', class_='html.parser')  # Use a dictionary for attributes
			article_titles = soup.find_all('title')
			for titles in article_titles:
                
				title += str(titles.text)
			
			return title
			
		else:
			print('Failed. Code:', response.status_code)
		

	except requests.exceptions.RequestException as e:
		print('Request Exception:', e)

	except Exception as e:
		print('An error occurred:', e)

	return


# Accesses html from website, finds all of the content with paragraph tags, returns content from paragraphs without the html tags
def getContent(url):
	content = ""

	try:
		response = requests.get(url)
		response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes

		if response.status_code == 200:
			soup = BeautifulSoup(response.text, 'html.parser')
			
			# article_titles = soup.find_all('title', class_='html.parser')  # Use a dictionary for attributes
			article_paragraphs = soup.find_all('p')
			for paragraph in article_paragraphs:
                
				content += str(paragraph.text)
			
			return content
			
		else:
			print('Failed. Code:', response.status_code)
		

	except requests.exceptions.RequestException as e:
		print('Request Exception:', e)

	except Exception as e:
		print('An error occurred:', e)

	return





# Summarizes text using Bart
def getBart(text, command):
    from transformers import BartTokenizer, BartForConditionalGeneration
    tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
    model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")

    # Tokenize the input text
    inputs = tokenizer(command+text, return_tensors="pt", max_length=maxLength, truncation=True)

    # Generate the summary
    summary_ids = model.generate(inputs["input_ids"], num_beams=4, max_length=300, early_stopping=True)

    # print(len(summary_ids))
    # Decode and print the summary
    summaryBart = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    
    # print(summaryBart)
    return(summaryBart)





# Summarizes text using TextRazor
def getRazor(text):
    # text = getContent(url)
    # print(summary)
    # api_key = os.environ.get('6e2c517a6de0b292efb4bd1962623d5cab64b1269df4c2111ab4b0cb')  # Replace with your TextRazor API key
    url = 'https://api.textrazor.com'  # TextRazor API endpoint
    headers = CaseInsensitiveDict()
    headers["x-textrazor-key"] = "6e2c517a6de0b292efb4bd1962623d5cab64b1269df4c2111ab4b0cb"
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    data = f"extractors=entities,entailments&text={text}"
    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        data = response.json()
        # Process the response from TextRazor as needed
        return data
    else:
        print(response.status_code)