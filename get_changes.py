import asyncio
import os
from pyppeteer import launch
from dotenv import load_dotenv
from gen_htop_code import get_totp_code
# from pyppeteer.launcher import launch
# from pyppeteer.page import Page, Request
# from pyppeteer.element_handle import ElementHandle
# from pyppeteer.browser import Browser
# from typing import Union, List, Dict

load_dotenv()
# auto-waiting playwright
# print(os.environ["MAIL"])

url = "https://kosenjp.sharepoint.com/sites/002967/Lists/List2/view.aspx?FilterField1=%5Fx30af%5F%5Fx30e9%5F%5Fx30b9%5F&FilterValue1=4%2D5"
mail = os.environ["MAIL"]
password = os.environ["pass"]
totp_code = get_totp_code()


async def get_change():
    browser = await launch(headless=False)
    # , args=['--no-sandbox'])
    page = await browser.newPage()
    file_path = './'  # file storage path, but also to detect whether the download is successful, it is recommended to download a unique path to prevent conflict

    await page.goto(url, waitUntil='networkidle0')

    # mail入力
    await page.type('#i0116', mail)
    await page.waitFor(2000)
    await page.click('#idSIButton9')

    # pass入力
    await page.type('#i0118', password)
    await page.waitFor(2000)
    await page.click('#idSIButton9')
    await page.waitFor(2000)

    # コード入力
    await page.type('#idTxtBx_SAOTCC_OTC', totp_code)
    # await page.waitFor(2000)
    await page.click('#idSubmit_SAOTCC_Continue')
    await page.waitFor(2000)
    # await page.click('input[type="submit"]')
    # await page.click('input[type="idSIButton9"]')

    # await page.click('input[id="idSIButton9"')
    # , waitUntil='networkidle')
    # await page.waitForNavigation({waitUntil:'networkidle'})

    # await page.click('#idSIButton9')
    await page.click('#idBtn_Back')

    cdp = await page.target.createCDPSession()
    await cdp.send('Page.setDownloadBehavior', {
        'behavior': 'allow',
        'downloadPath': file_path
    })  # Set download path

    # csvダウンロード
    await page.waitFor(3000)
    await page.click('button[name="CSV にエクスポート"]')
    # await download(
    #     'https://kosenjp.sharepoint.com/sites/002967/Lists/List2/view.aspx?viewid=b5a50204%2D0719%2D432b%2D9e97%2Def23c36980d5&id=%2Fsites%2F002967%2FLists%2FList2',
    #     'button[name="CSV にエクスポート"]')
    # '.ms-Button ms-Button--commandBar ms-CommandBarItem-link root-89')
    await page.waitFor(3000)

    await browser.close()
    # return print()


# async def download(target_url: str, selector: str):
#     browser: Browser = await launch(headless=True)
#     try:
#         page: Page = await browser.newPage()
#         await asyncio.gather(page.goto(target_url),
#                              page.waitForNavigation())  # 対象ページに移動
#         cookies: List[Dict[str,
#                            Union[str, int,
#                                  bool]]] = await page.cookies()  # cookieを取得

#         await page.setRequestInterception(True)  # リクエストをインターセプト
#         page.on('request', lambda request: asyncio.create_task(
#             send_request(request, cookies)))  # キャプチャした内容で別途リクエストを送信

#         link: ElementHandle = await page.querySelector(selector)
#         await link.click()  # 対象リンクをクリック

#     finally:
#         await browser.close()

# async def send_request(request: Request,
#                        cookies: List[Dict[str, Union[str, int, bool]]]):
#     response: Response = requests.request(
#         url=request.url,
#         method=request.method,
#         headers=request.headers,
#         cookies=dict(
#             map(lambda cookie: (cookie['name'], cookie['value']), cookies)),
#         data=request.postData,
#     )
#     extension: str = guess_extension(response.headers.get("content-type"))
#     output_path: str = f'downloads/{uuid4()}{extension}'
#     with open(output_path, mode='wb') as file:
#         file.write(response.content)

loop = asyncio.get_event_loop()
loop.run_until_complete(get_change())

# if __name__ == "__main__":
#     asyncio.get_event_loop().run_until_complete(main())
