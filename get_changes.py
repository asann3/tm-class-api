import asyncio
import os
from pyppeteer import launch
from dotenv import load_dotenv
from gen_htop_code import get_totp_code

load_dotenv()

url = "https://kosenjp.sharepoint.com/sites/002967/Lists/List2/view.aspx?FilterField1=%5Fx30af%5F%5Fx30e9%5F%5Fx30b9%5F&FilterValue1=4%2D5"
mail = os.environ["MAIL"]
password = os.environ["pass"]
totp_code = get_totp_code()


async def get_change():
    browser = await launch(headless=False)
    page = await browser.newPage()
    file_path = './'  # file storage path, but also to detect whether the download is successful, it is recommended to download a unique path to prevent conflict

    # ページアクセス
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

    # TOTPコード入力
    await page.type('#idTxtBx_SAOTCC_OTC', totp_code)
    await page.click('#idSubmit_SAOTCC_Continue')
    await page.waitFor(2000)
    await page.click('#idBtn_Back')
    await page.waitFor(3000)

    cdp = await page.target.createCDPSession()
    await cdp.send('Page.setDownloadBehavior', {
        'behavior': 'allow',
        'downloadPath': file_path
    })  # Set download path

    # csvダウンロード
    await page.click('button[name="CSV にエクスポート"]')
    await page.waitFor(3000)

    await browser.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(get_change())

# if __name__ == "__main__":
#     asyncio.get_event_loop().run_until_complete(main())
