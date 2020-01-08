import urllib3 , requests , re
from bs4 import BeautifulSoup
from gen_re import gen_re

url = "http://jyugyou.tomakomai-ct.ac.jp/jyugyou.php?class=J2"

http = urllib3.PoolManager()
r = http.request('GET', url)

soup = BeautifulSoup(r.data, "html.parser")
tables = soup.select('body table')

trs = soup.find_all("table", reversed=False)[9].find_all("tr")[1:]

test = soup.select('body > table')

for tr in trs:
    tds =tr.find_all("td")
    print(tds[0].contents[0])
    print(tds[1].contents[0])

    dates = re.match(r"　([0-9]{1,2})月([0-9]{1,2})日\(.\)\ ([１|２|３|４|５|６|７|８|９|０])(・([１|２|３|４|５|６|７|８|９|０]))?時限目", tds[0].contents[0])
    print(dates.group(1))
    print(dates.group(2))
    print(dates.group(3))


    month = ('{0:02}'.format(int(dates.group(1))))
    day = ('{0:02}'.format(int(dates.group(2))))
    times = str(int(dates.group(3)))
    print('{0:02}{1:02}'.format(int(dates.group(1)), int(dates.group(2))))

    print("{0}{1}".format(month,day))
    print(times)

    f = open("subjects.txt")
    
    subjects = f.read().split()
    print(tds[1].contents[0])
    subjects = re.match(gen_re(subjects),tds[1].contents[0])
    # print(subjects)
    print(subjects.group(1))
    print(subjects.group(2))
    b_sub = subjects.group(1)
    a_sub = subjects.group(2)
    d = {month+day:times+"時限目:"+b_sub+"👉 "+a_sub}
    print(d)

    f.close