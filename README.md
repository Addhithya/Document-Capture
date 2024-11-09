# Document-Capture
This project is designed to capture key information from an document/image like Driving License or passport. By using LlamaParse, the script parses the document to extract specific fields such as Document id , name & Expiry date. The extracted text is then saved in a markdown file.

## Prerequisites
- Python 3.6 or later
- LlamaParse API access and API key (Get API key from https://cloud.llamaindex.ai/landing)

## Setup

### Clone the repository:
  ``` bash
      git clone <repository_url>
      cd document-capture
```
### Install dependencies:
```bash
pip install -r requirements.txt
```

### Create a `.env` file in the root directory to securely store your API key:
```bash
LLAMA_CLOUD_API_KEY=your_api_key_here
```

### Run the script:
```bash
python app.py
```

## License 
MIT
