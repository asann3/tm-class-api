import asyncio
import os
from pyppeteer import launch
from dotenv import load_dotenv
load_dotenv()

# print(os.environ["MAIL"])
# def main():

# url = 'https://google.com'
mail = os.environ["MAIL"]

async def get_change():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto(url, waitUntil='networkidle0')

    # await page.waitForSelector('input[aria-label="検索"]')
    await page.type('#i0116', mail)
    # await asyncio.wait[{
    #     # page.click('input[type="submit"]'),
    #     page.click('#idSIButton9'),
    #     page.waitForNavigation(),
    # }]
    await asyncio.gather()[{
        # page.click('input[type="submit"]'),
        page.waitForNavigation(),
        page.click('#idSIButton9'),
    }]

    # await page.click('input[id="idSIButton9"')
    # , waitUntil='networkidle')
    # await page.waitForNavigation({waitUntil:'networkidle'})
    await page.waitFor(10000)
    # await page.type('input[aria-label="検索"]', "苫小牧")

    # await browser.close()
    return print(mail)

    # html: str = await page.content()
    # return html
    # mail =


loop = asyncio.get_event_loop()
loop.run_until_complete(get_change())

# if __name__ == "__main__":
#     asyncio.get_event_loop().run_until_complete(main())