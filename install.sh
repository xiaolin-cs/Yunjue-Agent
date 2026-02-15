# uv sync
# uv venv .dynamic_tools_venv
# source .dynamic_tools_venv/bin/activate
# uv pip install -U crawl4ai
# crawl4ai-setup
# playwright install-deps
apt install -y npm
npm install -g @openai/codex


# uv sync
# uv venv .dynamic_tools_venv
# source .dynamic_tools_venv/bin/activate

# uv pip install -U crawl4ai playwright
# python -m playwright install chromium

# 测试 Playwright 能否运行
# python - << 'PY'
# from playwright.sync_api import sync_playwright
# with sync_playwright() as p:
#     b = p.chromium.launch(headless=True, args=["--no-sandbox","--disable-setuid-sandbox"])
#     page = b.new_page()
#     page.goto("https://example.com", timeout=60000)
#     print(page.title())
#     b.close()
# PY
