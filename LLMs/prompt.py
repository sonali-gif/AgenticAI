from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

prompt = PromptTemplate.from_template(
    "Explain {topic} to a {level} student. Give one simple example."
)

formatted_prompt = prompt.format(
    topic="OOP",
    level="beginner"
)

response = model.invoke(formatted_prompt)

print(response.content)