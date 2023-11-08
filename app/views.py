from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Text



# says that this function can do handle POST requests
@api_view(["POST"])
def summarize_view(request):
	from main import collectData
	import json

	# handle data inputs
	if request.method == "POST":
		
		# # Summarize Text
		# summary_name = collectData()

		# # Turn File Name into JSON Object
		# def string_to_json(input_string):
		# 	try:
		# 		# Parse the input string into a JSON object
		# 		json_object = {"File Name": input_string}
		# 		return json_object
		# 	except json.JSONDecodeError as e:
		# 		print(f"Error decoding JSON: {e}")
		# 		return None

		# # Call Function to Convert FileName to JSON
		# json_obj = string_to_json(summary_name)

		# if json_obj is not None:
		# 	print("JSON object:", json_obj)
		# else:
		# 	print("Unable to convert the string to a JSON object.")

		
		# # return answer & status 200 (meaning everything worked!) 
		# return Response(json_obj, status=200)

		collectData()
		return Response(status=200)




@api_view(["POST"])	
def getData(request):
	from excel import fromExcel
	import json

	# Handle data inputs
	if request.method == "POST":


		# Get the data and provide No value if not given
		date = request.data.get("date", None)
		model = request.data.get("model", None)

		# Converts summary in xlsx file to json
		json_summary = fromExcel(model, date)
		

		

		return Response(json_summary, status=200)
	




@api_view(["POST"])
def sendEmail(request):
	if request.methods == "POST":





		return Response('summary', status=200)
	







@api_view(["POST"])
def test(request):
	
	# handle data inputs
	if request.method == "POST":
		
		# get the data and provide No value if not given
		text = request.data.get("text", None)
		
		# add it to the database and save
		new_addition = Text(text=text)
		new_addition.save()

# 		# pull the text and summarize it
# 		collectData()
		
		# return answer & status 200 (meaning everything worked!) 
		return Response(new_addition, status=200)



@api_view(["POST"])
def makeLog(request):
	import json
	from excel import createLog
	# handle data inputs
	if request.method == "POST":

		createLog()
		

		
		# return answer & status 200 (meaning everything worked!) 
		return Response(status=200)
	


@api_view(["POST"])
def saveJSONFile(request):
	import json
	from excel import saveJson
	# handle data inputs
	if request.method == "POST":
		
		file_name = request.data.get("File Name", None)
		
		saveJson(file_name)

		return Response(status=200)


	

# @api_view(["POST"])
# def testJson(request):
# 	import json
# 	if request.method == "POST":
		
# 		summary_name = "summary02-11-2023.xlsx"
# 		def string_to_json(summary_name):
# 				try:
# 					# Parse the input string into a JSON object
# 					json_object = json.loads(summary_name)
# 					return json_object
				
# 				except json.JSONDecodeError as e:
# 					print(f"Error decoding JSON: {e}")
# 					return None
# 				except Exception as e:
# 					print(f"Unknown Error: {e}")
# 					return None

# 		# Example usage:
# 		json_obj = string_to_json(summary_name)

# 		if json_obj is not None:
# 			print("Able to convert to JSON Object.")
# 		else:
# 			print("Unable to convert to JSON object.")

# 		# return answer & status 200 (meaning everything worked!) 
# 		return Response(summary_name, status=200)






# @api_view(["POST"])
# def test(request):
	
# 	# handle data inputs
# 	if request.method == "POST":
		
# 		# get the data and provide No value if not given
# 		text = request.data.get("text", None)
		
# 		# add it to the database and save
# 		new_addition = Text(text=text)
# 		new_addition.save()

# # 		# pull the text and summarize it
# # 		collectData()
		
# 		# return answer & status 200 (meaning everything worked!) 
# 		return Response(new_addition, status=200)