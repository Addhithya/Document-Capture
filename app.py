import os
from dotenv import load_dotenv
from llama_parse import LlamaParse

load_dotenv()

llama_cloud_api_key = os.getenv("LLAMA_CLOUD_API_KEY")


documents_with_instruction = LlamaParse(
    result_type="markdown",
    parsing_instruction="""
    Extract me just the Document no./id , Name , Expiry date
    """
    ).load_data("/Users/addhithyarh/Desktop/Screenshot 2024-11-08 at 18.54.20.png")

print (documents_with_instruction)


file_name = "captured_doc.md"
with open(file_name, 'w') as file:
    file.write(documents_with_instruction[0].text)





# document = LlamaParse(result_type="markdown").load_data("/Users/addhithyarh/Desktop/Screenshot 2024-11-08 at 18.54.20.png")

# print(document)

# print(document[0].text[:1000])

# file_name = "doc.md"
# with open(file_name, 'w') as file:
#     file.write(document[0].text)