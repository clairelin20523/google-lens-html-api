# Import required libraries
import asyncio
from urllib.parse import quote

from playwright.async_api import async_playwright
from playwright_stealth import Stealth

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

# Start FastAPI instance
app = FastAPI()

# Set API endpoint using GET /google-lens
# Response type is PlainTextResponse to return raw HTML
@app.get("/google-lens", response_class = PlainTextResponse)
# Function that performs Google lens search and return HTML of exact match tab
# Takes in one required string parameter imageUrl: the full image URL 
async def google_lens(imageUrl: str):
    # Encode URL into safe format to ensure correct results
    encoded_url = quote(imageUrl, safe = "")
    # Attach encoded URL to the Google Lens upload link
    lens_url = f"https://lens.google.com/upload?url={encoded_url}"

    # Run asynchronouly with async to scale & use Stealth to bypass bot detection
    async with Stealth().use_async(async_playwright()) as p:
        # Open chrome brower and wait for page to load
        # Uses launch_persistent_context to load with profile
        browser = await p.chromium.launch_persistent_context(
            # Set user directory to make automated browser like user browser
            user_data_dir = "./user_data",
            # Use headed mode to open real browser instead of running in background
            headless = False,
            # Hide automation flag to aviod bot detection
            args = ["--disable-blink-features=AutomationControlled"])
        page = await browser.new_page()

        # Navigate to appended lens url 
        await page.goto(lens_url)

        # Find exact maxtches button and click, wait for everything to load
        await page.get_by_text("Exact matches").click()
        await page.wait_for_load_state("networkidle")

        # Save full raw HTML & close browser when done
        html = await page.content()
        await browser.close()

        # Return full raw HTML
        return html