import asyncio
import io
import contextlib
import os
from pydantic import BaseModel, Field
from crawl4ai import AsyncWebCrawler, BrowserConfig

__TOOL_META__ = {
    "name": "fetch_web_text",
    "description": "Fetches and extracts text content from a web page given its URL using Crawl4ai. This tool retrieves the rendered content of web pages and returns clean, structured text suitable for LLM consumption. It can only fetch web pages and must not download files.",
    "dependencies": ["crawl4ai", "pydantic"]
}

class InputModel(BaseModel):
    url: str = Field(..., description="The URL of the web page to fetch")

class OutputModel(BaseModel):
    text: str = Field(..., description="Extracted text content from the web page")

def run(input: InputModel) -> OutputModel:
    """
    Fetch and extract text content from a web page.
    
    Args:
        input: InputModel containing the URL to fetch
        
    Returns:
        OutputModel containing the extracted text content
    """
    async def fetch_content():
        f = io.StringIO()
        try:
            with contextlib.redirect_stdout(f):
                async with AsyncWebCrawler(
                    magic=True,
                    config=BrowserConfig(
                        user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
                        headers={
                            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                            "Accept-Language": "en-US,en;q=0.5",
                            "Accept-Encoding": "gzip, deflate, br",
                            "DNT": "1",
                            "Connection": "keep-alive",
                            "Upgrade-Insecure-Requests": "1"
                        }
                    )
                ) as crawler:
                    result = await crawler.arun(url=input.url)
                    
                    if not result.success:
                        error_msg = result.error_message if hasattr(result, 'error_message') else "Unknown error occurred"
                        return f"Failed to fetch content from {input.url}. Error: {error_msg}"
                    
                    content = result.markdown if result.markdown else ""
                    
                    if not content or len(content.strip()) == 0:
                        return f"No text content could be extracted from {input.url}. The page may be empty or require authentication."
                    
                    return content
        except Exception as e:
            return f"Error fetching content from {input.url}: {str(e)}"
    
    # Run the async function
    try:
        text_content = asyncio.run(fetch_content())
    except Exception as e:
        text_content = f"Failed to execute fetch operation: {str(e)}"
    
    return OutputModel(text=text_content)