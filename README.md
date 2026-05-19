# Google Lens HTML API
This API  performs a Google Lens search (with image URL), returning the full HTML text of the Exact Match results page.

Built using FastAPI and Playwright.

### API Endpoint
#### GET /google-lens
**Response:** The raw HTML string of the Google Lens Exact Match results page.

#### Query Parameter
| Name | Type | Description |
|------|------|-------------|
|imageUrl|str|Full & direct URL of the image to search|

## Hosted API link
https://unweave-commotion-slightly.ngrok-free.dev/docs \
or insert imageUrl directly \
https://unweave-commotion-slightly.ngrok-free.dev/google-lens?imageUrl=&lt;imageUrl&gt;

## Setup and test API locally
*Download main.py and open terminal in the same directory*

### 1. Install dependencies
`pip install fastapi uvicorn playwright playwright-stealth`

### 2. Run the API locally
`uvicorn main:app --reload`

### 3. Locate local host URL in the output
*INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)*

http://127.0.0.1:8000 = &lt;LOCAL HOST URL&gt;

### 4. Paste into browser

#### a. Open interface, OR
&lt;LOCAL HOST URL&gt;/docs
*   Click on GET
*   Click on Try It Out
*   Paste imageUrl
*   lick on Execute

#### b. Directly use API endpoint
&lt;LOCAL HOST URL&gt;/google-lens?imageUrl=&lt;imageUrl&gt;

## Example
#### a. Open interface, OR
http://127.0.0.1:8000/docs

with imageUrl = https://picsum.photos/300/300

#### b. Directly use API endpoint
http://127.0.0.1:8000/google-lens?imageUrl=https://picsum.photos/300/300

##### Returns the raw HTML string of the Google Lens Exact Match results page:
*<!DOCTYPE html><html itemscope="" itemtype="http://schema.org/SearchResultsPage" lang="en"><head><meta charset="UTF-8"><meta content="origin" name="referrer"><link href="//www.gstatic.com/images/branding/searchlogo/ico/favicon.ico" rel="icon"><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"><title>Google Search</title><script nonce="">window._hst=Date.now();</script><script nonce="">(function(){var _g={kEI:'fxcMavbZBs-ymtkPw6qTmQE',kEXPI:'31',kBL:'4PWo',kOPI:89978449};(function(){var a;((a=window.google)==null?0:a.stvsc)?google.kEI=_g.kEI:window.google=_g;}).call(this);})();(function(){google.sn='web';google.kHL='en';google.usb=false;})();(function(){*...

## Approach

