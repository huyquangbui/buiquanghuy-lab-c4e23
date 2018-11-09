from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import pyexcel

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
connection = urlopen(url)

raw_data = connection.read()
page_content = raw_data.decode("utf-8")

#Find ROI
soup = BeautifulSoup(page_content, "html5lib")
table = soup.find(id="tableContent")
# print(table)


#Extract data
tr_list = table.find_all("tr")
VNM_finance_data = []
count = 0
for tr in tr_list:
    td = tr.find("td")
    title = td[0].text
    fourth_quarter_2016 = td[1].text
    first_quarter_2017 = td[2].text
    second_quarter_2017 = td[3].text
    third_quarter_2017 = td[4].text
    data = OrderedDict({
        "title":title,
        "Q4_2016":fourth_quarter_2016,
        "Q1_2017":first_quarter_2017,
        "Q2_2017":second_quarter_2017,
        "Q3_2017":third_quarter_2017,
    })
    VNM_finance_data.append(data)

print(VNM_finance_data)
# pyexcel.save_as(records=VNM_finance_data,dest_file_name="VNM_fin_data.xlsx")