# google-lens-html-api
This API  performs a Google Lens search (with image URL), returning the full HTML text of the Exact Match results page.

Built using FastAPI and Playwright.

## API Endpoint
### GET /google-lens
**Response:** The raw HTML string of the Google Lens Exact Match results page.

1. Download main.py
2. In the same directory as the saved file, open terminal and run: uvicorn main:app --reload
3. Find the <YOUR LINK> something like: http://127.0.0.1:8000
4. Paste into browser <YOUR LINK>/docs
   Click on GET
   Click on Try It Out
   Paste imageUrl
   Click on Execute
6. OR <YOUR LINK>/google-lens?imageUrl=<imageUrl>
