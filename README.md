create a requiremets.txt in same path with all necessary libraries
set the LANGCHAIN_API_KEY and  LANGCHAIN_PROJECT in .env file of same path
 
LANGCHAIN_API_KEY=your-api-key-here
LANGCHAIN_PROJECT=your-project-name

then in python check this
from dotenv import load_dotenv
import os

load_dotenv()
print("API KEY:", os.getenv("LANGCHAIN_API_KEY"))
print("PROJECT:", os.getenv("LANGCHAIN_PROJECT"))
