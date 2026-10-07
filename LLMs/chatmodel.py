from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage,HumanMessage

load_dotenv()

model=ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

messages=[
     SystemMessage(
        content="You are a Python teacher. Explain everything to beginners."
    ),
    HumanMessage(
        content="What is a Python list?"
    )
]
response =model.invoke(messages)
print(response)
# print(response.content)