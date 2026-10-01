from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_agent
from tools import search_tool,wiki_tool

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

llm = ChatGoogleGenerativeAI(model="gemini-3.8-flash", temperature=0.7)

agent = create_agent(
    model=llm,
    tools=[search_tool,wiki_tool],#wiki_tool,
    system_prompt="You are a research assistant that will help generate a research paper. Answer the user query.",
    response_format=ResearchResponse
)

query = input("What can i help you research?")
raw_response = agent.invoke({"messages": [{"role": "user", "content": query}]})
print(raw_response["structured_response"])