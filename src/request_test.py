import requests
import os
import sys
from dotenv import load_dotenv
load_dotenv()

def test_api_root():
    # Send a GET request
    response = requests.get('http://localhost:8000/')

    # Check the response status code
    if response.status_code == 200:
        # Get the JSON response data
        data = response.json()
        print(data)
    else:
        print("Request failed with status code:", response.status_code)


def call_api_for_file():
    # Step 1: Read the Python file
    base_project_path = os.getcwd().split(os.getenv('PROJECT_NAME'))[0] + os.getenv('PROJECT_NAME')
    undocumented_file_path = base_project_path + '\\src\\test_file\\undocummented_file.py'

    with open(undocumented_file_path, 'r') as file:
        code = file.read()
    
    # Step 2: Send a POST request to the API
    url = "http://localhost:8000/generate_docstring"
    json_data = {"file_contents": code}  # Replace with the actual file contents
    response = requests.post(url, json=json_data)

    if response.status_code == 200:
        result = response.json()
        output_code = result['output_code']
        print(result)
    else:
        print("Request failed with status code:", response.status_code)
        
    # Step 3: Write the output to a file
    documented_file_path = base_project_path + '\\src\\test_file\\docummented_file.py'

    # Save the updated code to a new file
    with open(documented_file_path, 'w') as file:
        file.write(output_code)

if __name__ == "__main__":
    test_api_root()
    
    call_api_for_file()
    pass