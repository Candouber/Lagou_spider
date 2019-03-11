import requests
import time
import json
from lxml import etree
from selenium import webdriver


item = {}
browser = webdriver.Chrome()
browser.get('https://www.lagou.com/zhaopin/Java/?labelWords=label')
root_url = 'https://www.lagou.com/zhaopin/Java/?labelWords=label'
cookie = {'user_trace_token':'20180731145204-ad3a44b1-2b39-47c1-9f28-2ce62374fae6',
          'ga':'GA1.2.1746439199.1533019926',
          'LGUID':'20180731145205-3c80e580-948e-11e8-a085-5254005c3644',
          'JSESSIONID':'ABAAABAAAGGABCB81DD9CD161946551BF408A01F734F168',
          'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6':'1552044194',
          '_gid':'GA1.2.408680091.1552044194',
           'sensorsdata2015jssdkcross':'%7B%22distinct_id%22%3A%221695d199afb387-0798da9b4b1fdd-36647105-2073600-1695d199afc542%22%2C%22%24device_id%22%3A%221695d199afb387-0798da9b4b1fdd-36647105-2073600-1695d199afc542%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D',
            'ab_test_random_num':'0',
            'showExpriedIndex':'1',
            'showExpriedCompanyHome':'1',
            'showExpriedMyPublish':'1',
            'hasDeliver':'0',
            'index_location_city':'%E5%85%A8%E5%9B%BD',
            'TG-TRACK-CODE':'index_navigation',
            'LGSID':' 20190309112015-41f4949b-421a-11e9-8cf9-5254005c3644',
            'SEARCH_ID':'dfc95c26c63e40bc9aa996c76d2b2d09',
            'gat':'1',
            'LG_LOGIN_USER_ID':'a9666f2af422f275309c964fc85f6bb6b9ea1396f647eeb34c3626c887a9850c',
            '_putrc': '20F1301343E2B5DC123F89F2B170EADC' ,
            'login':'true',
            'unick':'%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B79175',
            'gate_login_token':'f71f6c27b5d08b745bcca4041b91ba41d3cc52b2268714c74b730c22c2ad03f7',
            'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6':'1552106491',
            'LGRID':'20190309124131-9c0c75f1-4225-11e9-8cf9-5254005c3644'}

c_cookie = {'name':'index_location_city', 'value':'%E5%85%A8%E5%9B%BD'}
b_cookie = {'name':'SEARCH_ID', 'value':'e01a4ebb337a46ac80b51c4d6dd3e1a6'}

res_login = requests.get(root_url, cookies = cookie)
n_cookies = res_login.cookies
header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
          'Connection': 'keep-alive',
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
          }

browser.add_cookie(cookie_dict=c_cookie)
browser.add_cookie(cookie_dict=b_cookie)

def parse_url(root_url):
    time.sleep(1.5)
    root_content = requests.get(root_url, headers=header).content
    root_content = root_content.decode(encoding='utf8')
    root_html = etree.HTML(root_content)
    m_url = root_html.xpath('//*[@id="s_position_list"]/ul/li/div[1]/div[1]/div[1]/a/@href')
    return m_url

def parse_data(url):
    browser.get(url)
    time.sleep(5)
    item['job_name'] = browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/span').text
    item['company_name'] = browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div[1]').text
    item['city'] = browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/dd/p[1]/span[2]').text
    item['education'] = browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/dd/p[1]/span[4]').text
    item['expirence'] = browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/dd/p[1]/span[3]').text
    item['full_or_part'] = browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/dd/p[1]/span[5]').text
    item['money'] = browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/dd/p[1]/span[1]').text
    item['adventage'] = browser.find_element_by_xpath('//*[@id="job_detail"]/dd[1]/p').text
    item['describe'] = browser.find_element_by_xpath('//*[@id="job_detail"]/dd[1]/p').text
    with open('/Users/apple/Desktop/DaChuang/lagou.json', 'a', encoding='utf-8') as f:
        json.dump(item,f, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ':'))



for i in range(1,31):
    root_url = 'https://www.lagou.com/zhaopin/Java/'+str(i)+'/?filterOption=3'
    m_url = parse_url(root_url)
    for a in m_url:
        parse_data(a)
    print(i)



browser.close()