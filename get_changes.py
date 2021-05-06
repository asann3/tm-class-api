import asyncio
import os
from pyppeteer import launch
from dotenv import load_dotenv
from gen_htop_code import get_totp_code

load_dotenv()

# print(os.environ["MAIL"])

url = "https://kosenjp.sharepoint.com/sites/002967/Lists/List2/view.aspx?FilterField1=%5Fx30af%5F%5Fx30e9%5F%5Fx30b9%5F&FilterValue1=4%2D5"
mail = os.environ["MAIL"]
password = os.environ["pass"]
totp_code = get_totp_code()


async def get_change():
    browser = await launch(headless=False)
    page = await browser.newPage()
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

    # csvダウンロード
    await page.waitFor(4000)
    # await page.click('body > div >div > div > div > div > div > div')
    # await page.click('#exportListCommand')  # data-automationid
    # await page.click('button[data-automationid="exportListCommand"]')
    # await page.click('div.ms-OverflowSet-item item-87 > button.button')
    await page.click('button[name="CSV にエクスポート"]')
    # await page.click(
    # '.ms-Button ms-Button--commandBar ms-CommandBarItem-link root-89')
    #  >id__236')
    # span[type="ms-Button-label  label-91"]')
    # <div data-automationid="FieldRenderer-date" aria-label="2021/06/03" title="2021/06/03" dir="auto" class="fieldText_c4a10d46">2021/06/03</div>
    # <div data-automationid="FieldRenderer-date" aria-label="2021/07/08" title="2021/07/08" dir="auto" class="fieldText_c4a10d46">2021/07/08</div>
    # item = await page.querySelectorAll('#FieldRenderer-date')
    # item = await page.querySelectorAll('div > *')
    # item = await item[0].getPropery('textContent')
    # data = await (await item.getPropery('textContent')).jsonValue()
    await page.waitFor(4000)

    await browser.close()
    # return print()


loop = asyncio.get_event_loop()
loop.run_until_complete(get_change())

# if __name__ == "__main__":
#     asyncio.get_event_loop().run_until_complete(main())