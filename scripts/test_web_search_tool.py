#!/usr/bin/env python3
"""
Test script for web_search dynamic tool.

Usage:
    # Load env vars from .env first
    uv run python scripts/test_web_search_tool.py [path/to/web_search.py]

    # Or with explicit path (default: output/test/private_dynamic_tools/dynamic_tools_0/web_search.py)
    uv run python scripts/test_web_search_tool.py
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

# Load .env if python-dotenv is available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


def test_web_search_tool(tool_path: Path) -> bool:
    """Run web_search tool with a simple query. Returns True if success."""
    if not tool_path.exists():
        print(f"Error: Tool file not found: {tool_path}")
        return False

    api_key = os.environ.get("TAVILY_API_KEY")
    if not api_key:
        print("Error: TAVILY_API_KEY not set. Add it to .env or export it.")
        return False

    # Use isolated venv if available (same as runtime)
    project_root = Path(__file__).resolve().parent.parent
    isolated_python = project_root / ".dynamic_tools_venv" / "bin" / "python"
    python_path = str(isolated_python) if isolated_python.exists() else sys.executable

    test_input = {"query": "Python programming language", "num_results": 3}
    code = f"""
import json
import sys
import importlib.util

file_path = {json.dumps(str(tool_path))}
spec = importlib.util.spec_from_file_location("dynamic_module", file_path)
module = importlib.util.module_from_spec(spec)
sys.modules["dynamic_module"] = module
spec.loader.exec_module(module)

input_data = json.dumps({json.dumps(test_input)})
input_instance = module.InputModel(**json.loads(input_data))
result = module.run(input_instance)
print(result.model_dump_json())
"""

    import subprocess
    try:
        proc = subprocess.run(
            [python_path, "-c", code],
            capture_output=True,
            text=True,
            timeout=30,
            env=os.environ.copy(),
        )
        if proc.returncode != 0:
            print(f"Tool execution failed (exit {proc.returncode}):")
            print(proc.stderr or proc.stdout)
            return False

        data = json.loads(proc.stdout.strip())
        results = data.get("results", [])
        print(f"Success! Got {len(results)} results:")
        for i, r in enumerate(results[:3], 1):
            print(f"  {i}. {r.get('title', 'N/A')[:60]}...")
            print(f"     URL: {r.get('url', 'N/A')}")
        return True

    except subprocess.TimeoutExpired:
        print("Error: Tool execution timed out (30s)")
        return False
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse output: {e}")
        print("Raw output:", proc.stdout[:500] if proc else "N/A")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


if __name__ == "__main__":
    import os
    from langsmith import traceable
    from langchain_anthropic import ChatAnthropic
    from langchain_core.tracers.langchain import wait_for_all_tracers

    # 确保这些环境变量在当前进程里可见
    os.environ["LANGSMITH_TRACING"] = "true"
    os.environ["LANGSMITH_API_KEY"] = "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"
    os.environ["LANGSMITH_PROJECT"] = "YunjueAgent"
    os.environ["ANTHROPIC_API_KEY"] = "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"

    llm = ChatAnthropic(model="claude-sonnet-4-5-20250929", temperature=0)

    @traceable(name="anthropic_debug", project_name="YunjueAgent")
    def run_once():
        return llm.invoke("Say hello in one sentence.").content

    print(run_once())
    wait_for_all_tracers()



    # default_path = Path(__file__).parent.parent / "output" / "test" / "private_dynamic_tools" / "dynamic_tools_0" / "web_search.py"
    # tool_path = Path(sys.argv[1]) if len(sys.argv) > 1 else default_path

    # print(f"Testing web_search tool: {tool_path}")
    # print(f"TAVILY_API_KEY: {'*' * 8 if os.environ.get('TAVILY_API_KEY') else 'NOT SET'}")
    # print(f"PROXY_URL: {os.environ.get('PROXY_URL', '(not set)')}")
    # print("-" * 50)

    # ok = test_web_search_tool(tool_path)
    # sys.exit(0 if ok else 1)
