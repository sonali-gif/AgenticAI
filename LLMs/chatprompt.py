from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model =ChatGoogleGenerativeAI(
    model ="gemini-3.6-flash"
)

chat_prompt=ChatPromptTemplate.from_messages([
    ("system","You are a{role}"),
    ("human","explain {topic} to me")
])

message=chat_prompt.format_messages(
    role="Python teacher",
    topic="lists"
)

response=model.invoke(message)

print(response.content)
