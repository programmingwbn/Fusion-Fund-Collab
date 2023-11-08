import pandas



# Example Dictionary:
# {
    #   "Model" : "OpenAi",
    #   "Date": "01/01/01",
    #   "Collected text": " ",
    #   "summary_bart": "",
    #   "summary_textrazor": ""
    # }
# summary = {"Model" : "model", 
#     "Date" : "date", 
#     "Collected_Text" : "text_to_summarize", 
#     "Summary_Bart" : "summaryBart", 
#     "Summary_TextRazor" : "summaryRazor"}

# weeklySummary = [summary, summary]



def toExcel(summary, model):
    import datetime

    # Create a pandas DataFrame
    df = pandas.DataFrame(summary)

    #Get today's date
    date = datetime.date.today().strftime('%d-%m-%Y')

    # Get the current time
    current_time = datetime.datetime.now().time()

    # Format the current time as a string
    time = current_time.strftime("%H-%M-%S")

    # Creates file name
    summary_name = f"SummarySheets\Summary_{date}_{time}.xlsx"

    # Create an Excel writer object
    excel_writer = pandas.ExcelWriter(summary_name, engine = "openpyxl")

    # Write the DataFrame to the Excel file
    df.to_excel(excel_writer, sheet_name=f"Summary{date}", index=False)

    # Save the Excel file
    excel_writer.close()

    print("Excel file created successfully.")
    logSave(summary_name, model, date)
    




    
def logSave(summary_name, model, date):
    # Step 1: Read Excel file as a DataFrame
    excel_file = 'SummarySheets\SummaryList.xlsx'  # Replace with the path to your Excel file
    df = pandas.read_excel(excel_file)

    # Step 2: Increment the serial number column by one
    df['SerialNumber'] = df['SerialNumber'] + 1

    # Step 3: Add an entry to the DataFrame
    new_entry = {'SerialNumber': max(df['SerialNumber']) + 1, 'File Name': summary_name, 'Date': date, 'model' : model}
    df = df.append(new_entry, ignore_index=True)

    # Step 4: Update the Excel file with the updated DataFrame
    with pandas.ExcelWriter(excel_file, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name='Sheet1', index=False)

    print("Updated Excel file successfully.")


def fromExcel(date, model):


    sheet_name = "Sheet1"  # Replace with the name of the sheet you want to read
    cell_address = ('A', 1)  # Replace with the cell address you want to retrieve

    cell_value = get_cell_value_from_xlsx(file_path, sheet_name, cell_address)

    if isinstance(cell_value, str) and cell_value.startswith("Error"):
        print(f"An error occurred: {cell_value}")
    else:
        print(f"Value at cell {cell_address[0]}{cell_address[1]}: {cell_value}")





    # # Replace 'your_file.xlsx' with the path to your Excel file
    # xlsx_file = f"SummarySheets\{summary_name}"

    # # Read the Excel file into a Pandas DataFrame
    # df = pandas.read_excel(xlsx_file)

    # # Convert the DataFrame to a JSON file
    # # Replace 'output.json' with the desired output JSON file path
    # json_data = df.to_dict(orient='records')

    # print(f"Excel file {xlsx_file} has been successfully converted to JSON object")
    # return json_data

def saveJson(summary_name):
    import json

    # Your JSON object (as a Python dictionary)
    json_obj = fromExcel(summary_name)


    # Specify the file path where you want to save the JSON data
    file_path = "test.json"

    # Write the JSON data to the file
    with open(file_path, 'w',) as json_file:
        json.dump(json_obj, json_file, indent=4)

    print(f"JSON data saved to {file_path}")




def createLog():
    data = {
    "SerialNumber": [],
    "File Name": [],
    "date": [],
    "model": []
    }

    df = pandas.DataFrame(data)

    # Specify the output file name
    output_file = "SummarySheets\SummaryLogs.xlsx"

    # Write the DataFrame to an XLSX file
    df.to_excel(output_file, index=False)

    print(f"DataFrame has been saved to {output_file}")

    import pandas as pd


def get_cell_value_from_xlsx(file_path, sheet_name, cell_address):
    """
    Reads an XLSX file, extracts the value from the specified cell, and returns it.

    :param file_path: The path to the XLSX file.
    :param sheet_name: The name of the sheet in the XLSX file.
    :param cell_address: The cell address (e.g., 'A1', 'B2', 'C3').
    :return: The value from the specified cell.
    """
    try:
        # Read the XLSX file into a DataFrame
        df = pandas.read_excel(file_path, sheet_name=sheet_name)
        
        # Get the value from the specified cell
        cell_value = df.at[cell_address[0], cell_address[1]]
        
        return cell_value
    except Exception as e:
        return f"Error: {str(e)}"

# Example usage:
file_path = "your_file.xlsx"  # Replace with the path to your XLSX file
sheet_name = "Sheet1"  # Replace with the name of the sheet you want to read
cell_address = ('A', 1)  # Replace with the cell address you want to retrieve

cell_value = get_cell_value_from_xlsx(file_path, sheet_name, cell_address)

if isinstance(cell_value, str) and cell_value.startswith("Error"):
    print(f"An error occurred: {cell_value}")
else:
    print(f"Value at cell {cell_address[0]}{cell_address[1]}: {cell_value}")
