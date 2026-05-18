import asyncio
from urllib.parse import quote

from playwright.async_api import async_playwright
from playwright_stealth import Stealth

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, HTMLResponse

app = FastAPI()

@app.get("/google-lens", response_class = PlainTextResponse)
async def google_lens(imageUrl: str):
    encoded_url = quote(imageUrl, safe="")
    lens_url = f"https://lens.google.com/upload?url={encoded_url}"

    async with Stealth().use_async(async_playwright()) as p:
        browser = await p.chromium.launch_persistent_context(
            headless = False,
            user_data_dir = "./user_data",
            args = ["--disable-blink-features=AutomationControlled"])
        page = await browser.new_page()

        await page.goto(lens_url)

        await page.get_by_text("Exact matches").click()
        await page.wait_for_load_state("networkidle")

        html = await page.content()
        await browser.close()

        return html