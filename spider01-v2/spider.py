# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 23:39:15 2020

@author: asus-pc
"""

import requests
from bs4 import BeautifulSoup
from save_svg import save_svg
import os

#设置请求参数
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'Cookies':'_zap=b6721637-4451-4274-bf79-396a3dde8df3; _xsrf=DA5vRYhPLbk0GTLmXqFgiqV2vOhVF2z0; d_c0="APAWPA1EERKPTnkPT8LmmwJ3oANBDLw3L2U=|1603176335"; capsion_ticket="2|1:0|10:1603176335|14:capsion_ticket|44:MWQ4ZTNlMDg3MGZmNDA2NjllNjQxZDYwNDVkZjM2YWE=|e446cf3d1c5b18692e1a210068d93318886748b46d20f66723c9c95dd8888265"; r_cap_id="YzQ0YTE1OTQ5YzJlNDYwOGEwODIwYTRkY2VhODAyMDA=|1603176351|98d104f9ea4dc63565124fb12579e3486b1bbd3b"; cap_id="ZmQwYTVlN2E3ODE2NDA4Mjk5ZmI1MjRiNmI4YzczYTk=|1603176351|25d17f0bb158c3d4e1c40bd6c8d5ffcc9669242f"; l_cap_id="NDYxNDVmZGFkYTk5NGNlZjg1MGYzMzE2MTYyNzZiZjg=|1603176351|08577eab21993b76a7eb8d6c8edb2535f8e7455c"; z_c0=Mi4xZVNlVUNBQUFBQUFBOEJZOERVUVJFaGNBQUFCaEFsVk5xdFY3WUFDU25BUjR5X0I4QXFORTVrM0VWMDFBSGVyTzhR|1603176362|a3b29528fb26e78e04d95d2f9c0a5dbdc24c1edc; tst=r; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1603176335,1603209537; KLBRSID=4efa8d1879cb42f8c5b48fe9f8d37c16|1603209675|1603209534; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1603209676'
}
url = 'https://www.zhihu.com/question/412799877/answer/1523203315'

#获得请求返回值html
html = requests.get(url,headers=headers)

#按标签提取文字图片
soup = BeautifulSoup(html.text,features='lxml')
paragragh = ''.join([p.get_text() for p in soup.find_all('p')])
#print(paragraph)

img_urls = []
for img in soup.find_all('img'):
    if('class' in img.attrs):
        if(img.attrs['class'][-1] == 'lazy'):
            img_urls.append(img.attrs['data-actualsrc'])
            continue
    img_urls.append(img.attrs['src'])
#print(img_urls)


#懒加载图像前有一个noscript,可以用它来得到src,上面采取另一种方法data-actualsrc属性
'''
这是一段测试代码 忽略它
noscript = [noscript for noscript in soup.find_all('noscript')]
lazy_img = []
for tag in noscript:
    lazy_img.append(tag.nextSibling)
''' 

#写txt文件，仅包含p标签文字
if( not os.path.exists('./text') ):
    os.mkdir('./text')
with open('./text/paragraph.txt','w') as f:
    f.write(paragragh)

#写图片
if(not os.path.exists('./img')):
    os.mkdir('./img')
for i in range(len(img_urls)):
    filename = './img/'+str(i).rjust(3,'0')
    print('saving picture {}...'.format(i))
    if(img_urls[i].startswith('https://www.zhihu.com/equation?tex=')):
        #get svg
        save_svg(img_urls[i],filename,headers=headers,save_as=1)
    else:
        #get jpg
        with open(filename + '.jpg','wb') as f:
            f.write(requests.get(img_urls[i]).content)
    print('saving success...')

#该脚本爬取的链接为
'''https://www.zhihu.com/question/412799877/answer/1523203315'''