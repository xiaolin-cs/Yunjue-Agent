import os
from typing import List, Optional
from pydantic import BaseModel, Field, field_validator
import requests

__TOOL_META__ = {
    "name": "web_search",
    "description": "Search the web for information using a query string and return relevant results with URLs and snippets. This tool uses the Tavily search API to provide high-quality web search results. It returns a list of search results, each containing a title, URL, and snippet of the content.",
    "dependencies": ["requests", "pydantic"]
}

class SearchResult(BaseModel):
    title: str = Field(..., description="The title of the search result")
    url: str = Field(..., description="The URL of the search result")
    snippet: str = Field(..., description="A snippet or summary of the content")

class InputModel(BaseModel):
    query: str = Field(..., description="The search query string")
    num_results: int = Field(default=10, description="Maximum number of search results to return")
    
    @field_validator('query', mode='before')
    @classmethod
    def validate_query(cls, v):
        if not v or not str(v).strip():
            raise ValueError("Query cannot be empty")
        return str(v).strip()
    
    @field_validator('num_results', mode='before')
    @classmethod
    def validate_num_results(cls, v):
        num = int(v) if v is not None else 10
        if num < 1:
            raise ValueError("num_results must be at least 1")
        if num > 100:
            raise ValueError("num_results cannot exceed 100")
        return num

class OutputModel(BaseModel):
    results: List[SearchResult] = Field(..., description="List of search results")

def run(input: InputModel) -> OutputModel:
    api_key = os.environ.get("TAVILY_API_KEY")
    if not api_key:
        raise ValueError("TAVILY_API_KEY environment variable is not set")
    
    url = "https://api.tavily.com/search"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "query": input.query,
        "max_results": input.num_results,
        "search_depth": "basic",
        "include_answer": False,
        "include_images": False,
        "include_raw_content": False
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=30)
        response.raise_for_status()
        data = response.json()
        
        results = []
        if "results" in data:
            for item in data["results"][:input.num_results]:
                result = SearchResult(
                    title=item.get("title", ""),
                    url=item.get("url", ""),
                    snippet=item.get("content", "")
                )
                results.append(result)
        
        return OutputModel(results=results)
    
    except requests.exceptions.Timeout:
        raise Exception("Search request timed out after 30 seconds")
    except requests.exceptions.HTTPError as e:
        raise Exception(f"HTTP error occurred: {e.response.status_code} - {e.response.text}")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Network error occurred during search: {str(e)}")
    except Exception as e:
        raise Exception(f"Unexpected error during web search: {str(e)}")