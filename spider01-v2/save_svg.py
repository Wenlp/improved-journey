# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 15:53:32 2020

@author: asus-pc
"""

import requests
from cairosvg import svg2png

'''
params:
    url: url of the svg file 
    fname: name to save as 
    save_as: 0: *.svg
             1: *.png
    kwargs: receive the http header
return vals:
    no return values
    output one file: 'fname.svg' or 'fname.png'
'''

def save_svg(url,fname,save_as=0,**kwargs):
    #print('...saving svg file...')
    if('headers' in kwargs.keys()):
        headers = kwargs['headers']
    else:
        headers = {}
        #print('func save_svg() got no headers')
        
    html = requests.get(url,headers=headers,timeout=9)
    #print('html successfully get')
    if(save_as == 0):
        with open(fname + '.svg','wb') as f:
            f.write(html.content)
    elif(save_as == 1):
        svg2png(bytestring=html.content,write_to=fname + '.png')
    
if __name__ == '__main__':
    print('hello')
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
        'Cookies':'_zap=b6721637-4451-4274-bf79-396a3dde8df3; _xsrf=DA5vRYhPLbk0GTLmXqFgiqV2vOhVF2z0; d_c0="APAWPA1EERKPTnkPT8LmmwJ3oANBDLw3L2U=|1603176335"; capsion_ticket="2|1:0|10:1603176335|14:capsion_ticket|44:MWQ4ZTNlMDg3MGZmNDA2NjllNjQxZDYwNDVkZjM2YWE=|e446cf3d1c5b18692e1a210068d93318886748b46d20f66723c9c95dd8888265"; r_cap_id="YzQ0YTE1OTQ5YzJlNDYwOGEwODIwYTRkY2VhODAyMDA=|1603176351|98d104f9ea4dc63565124fb12579e3486b1bbd3b"; cap_id="ZmQwYTVlN2E3ODE2NDA4Mjk5ZmI1MjRiNmI4YzczYTk=|1603176351|25d17f0bb158c3d4e1c40bd6c8d5ffcc9669242f"; l_cap_id="NDYxNDVmZGFkYTk5NGNlZjg1MGYzMzE2MTYyNzZiZjg=|1603176351|08577eab21993b76a7eb8d6c8edb2535f8e7455c"; z_c0=Mi4xZVNlVUNBQUFBQUFBOEJZOERVUVJFaGNBQUFCaEFsVk5xdFY3WUFDU25BUjR5X0I4QXFORTVrM0VWMDFBSGVyTzhR|1603176362|a3b29528fb26e78e04d95d2f9c0a5dbdc24c1edc; tst=r; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1603176335,1603209537; KLBRSID=4efa8d1879cb42f8c5b48fe9f8d37c16|1603209675|1603209534; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1603209676'
    }
    save_svg('https://www.zhihu.com/equation?tex=b',fname='b',save_as=0,headers = headers)
    
    