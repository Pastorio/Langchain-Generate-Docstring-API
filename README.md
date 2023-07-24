# Python Project with LangChain and FastAPI

This is a Python project that utilizes LangChain and FastAPI libraries. LangChain is used to generate docstrings for Python files, and FastAPI is used to call the LangChain generator. The project also utilizes Poetry for managing the virtual environment.

## Project Structure

The project has the following file structure:

```
- config/
- data/
- models/
- notebooks/
    - test_file/   # Contains Python files to test the generation of docstrings
    - langchainAPI.ipynb   # Jupyter Notebook with test code for the LangChain model
    - request_test.ipynb   # Jupyter Notebook with test code for the API
- src/   # Contains the source code
    - test_file/   # Contains Python files to test the generation of docstrings
    - langchain_functions.py   # Python file with LangChain functions
    - request_test.py   # Python file with test code for the API
- main.py   # Python file with the API code
```

## Requirements

To run this project, make sure you have the following dependencies installed:

- LangChain
- FastAPI
- Poetry

## Installation

1. Clone this repository:

```bash
git clone https://github.com/Pastorio/langchain-api.git
```

2. Change into the project directory:

```bash
cd langchain-api
```

3. Set up the virtual environment using Poetry:

```bash
poetry install
```

4. Activate the virtual environment:

```bash
poetry shell
```

## Usage

1. Add your OpenAI key to the .env file
```bash
PROJECT_NAME="langchain-api"
OPENAI_API_KEY="sk-xxx"
```

2. Start the FastAPI server by running the `main.py` file:

```bash
python main.py
```

3. Run the `src/request_test.py` to generate docstring for a specific file.

## More Details

For more detailed information about the project, including setup instructions, usage examples, and additional documentation, please refer to the [project documentation](https://curved-helicopter-e6b.notion.site/Langchain-FastAPI-7a47cafaa67e4df89231bacb0ea4b722?pvs=4) on Notion.

The documentation covers topics such as:

- Installation and dependencies
- Project structure and file organization
- API endpoints and usage
- LangChain and FastAPI integration
- Testing and validation

Please visit the [project documentation](https://curved-helicopter-e6b.notion.site/Langchain-FastAPI-7a47cafaa67e4df89231bacb0ea4b722?pvs=4) for more information.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request in the GitHub repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
