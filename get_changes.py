import asyncio
from pyppeteer import launch


# def main():
async def get_change():
    browser = await launch(headless=False)
    page = await browser.newPage()
    # url = "https://kosenjp.sharepoint.com/sites/02tomakomai/students/Lists/test3?viewpath=%2Fsites%2F02tomakomai%2Fstudents%2FLists%2Ftest3"
    url = 'https://google.com'
    await page.goto(url)

    return 1
    # mail =


loop = asyncio.get_event_loop()
loop.run_until_complete(get_change())