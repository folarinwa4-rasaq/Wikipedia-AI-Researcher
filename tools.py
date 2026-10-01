import wikipedia
from langchain_community.tools import WikipediaQueryRun,DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.tools import Tool
from datetime import datetime

wikipedia.set_user_agent("wiki-summarizer/1.0 (contact@example.com)")

search = DuckDuckGoSearchRun()

def search_web(query: str) -> str:
    return search.run(query)

search_tool = Tool(
    name="search",
    func=search_web,
    description="Search the web for information"
)

api_wrapper = WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=100)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)