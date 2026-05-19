# google-lens-html-api
This API  performs a Google Lens search (with image URL), returning the full HTML text of the Exact Match results page.

Built using FastAPI and Playwright.

## API Endpoint
### GET /google-lens
**Response:** The raw HTML string of the Google Lens Exact Match results page.

### Query Parameter
| Name | Type | Description |
|------|------|-------------|
|imageUrl|str|Full & direct URL of the image to search|

*Download main.py and open terminal in the same directory*

## 1. Install dependencies
`pip install fastapi uvicorn playwright playwright-stealth`

## 2. Run the API locally
`uvicorn main:app --reload`

## 3. Locate local host URL in the output
*INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)*
http://127.0.0.1:8000 = &lt;LOCAL HOST URL&gt;

## 4. Paste into browser

### a. Open interface, OR
&lt;LOCAL HOST URL&gt;/docs
*   Click on GET
*   Click on Try It Out
*   Paste imageUrl
*   lick on Execute

### b. Directly use API endpoint
&lt;LOCAL HOST URL&gt;/google-lens?imageUrl=&lt;imageUrl&gt;
