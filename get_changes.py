import asyncio
import os
from pyppeteer import launch
from dotenv import load_dotenv
from gen_htop_code import get_totp_code

load_dotenv()

# print(os.environ["MAIL"])
# def main():

url = "https://kosenjp.sharepoint.com/sites/002967/Lists/List2/view.aspx?FilterField1=%5Fx30af%5F%5Fx30e9%5F%5Fx30b9%5F&FilterValue1=4%2D5"
# url = "https://login.microsoftonline.com/72fe835d-5e95-4512-8ae0-a7b38af25fc8/oauth2/authorize?client_id=00000003-0000-0ff1-ce00-000000000000&response_mode=form_post&protectedtoken=true&response_type=code%20id_token&resource=00000003-0000-0ff1-ce00-000000000000&scope=openid&nonce=A6F7B418670E914F93219037ABCBF91F00E434DDF7E90D00-9F3B21120A013233308A2E0745FA0A63E47BD335D850F470F7F8F8913FF8B307&redirect_uri=https%3A%2F%2Fkosenjp.sharepoint.com%2F_forms%2Fdefault.aspx&claims=%7B%22id_token%22%3A%7B%22xms_cc%22%3A%7B%22values%22%3A%5B%22CP1%22%5D%7D%7D%7D&wsucxt=1&cobrandid=11bd8083-87e0-41b5-bb78-0bc43c8a8e8a&client-request-id=b218c59f-700e-0000-9815-76e10909e3f5"
# url = 'https://google.com'
mail = os.environ["MAIL"]
password = os.environ["pass"]
# totp_uri = os.environ["TOTP_URI"]
totp_code = get_totp_code()


async def get_change():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto(url, waitUntil='networkidle0')

    # await page.waitForSelector('input[aria-label="検索"]')
    # await asyncio.wait[{
    #     # page.click('input[type="submit"]'),
    #     page.click('#idSIButton9'),
    #     page.waitForNavigation(),
    # }]

    # await asyncio.gather()[{
    #     # page.click('input[type="submit"]'),
    #     page.waitFor(1000)
    #     page.waitForNavigation(waitUntil='networkindle0'),
    #     page.click('#idSIButton9'),
    #     # asyncio.sleep(3)
    # }]

    # mail入力
    await page.type('#i0116', mail)
    await page.waitFor(2000)
    await page.click('#idSIButton9')

    # pass入力
    await page.type('#i0118', password)
    await page.waitFor(2000)
    await page.click('#idSIButton9')

    # コード入力
    await page.type('#idTxtBx_SAOTCC_OTC', totp_code)
    await page.waitFor(2000)
    await page.click('#idSubmit_SAOTCC_Continue')
    await page.click('input[type="submit"]')

    # await page.click('input[type="idSIButton9"]')

    # await page.click('input[id="idSIButton9"')
    # , waitUntil='networkidle')
    # await page.waitForNavigation({waitUntil:'networkidle'})
    await page.waitFor(2000)
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