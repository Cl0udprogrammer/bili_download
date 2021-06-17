import requests
import re
'''
用的时候替换一下番剧url，cookie，和headers里的Host
需要用户是大会员才能访问
'''
base_url="https://www.bilibili.com/bangumi/play/ss38627?t=839"
#番剧url

Cookie=""
#填入自己的cookie

base_headers={
	"Host": "www.bilibili.com",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
	"Accept-Encoding": "gzip, deflate, br",
	"Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
	"Origin": "https://www.bilibili.com",
	"Connection": "keep-alive",
	"Cookie": Cookie,
	"Upgrade-Insecure-Requests": "1",
	"Cache-Control": "max-age=0",
	"TE": "Trailers"
}

get_headers={
	"Host": "api.bilibili.com",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
	"Accept": "application/json, text/plain, */*",
	"Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
	"Referer": "https://www.bilibili.com/bangumi/play/ss26801?t=16",
	"Origin": "https://www.bilibili.com",
	"Connection": "keep-alive",
	"Cookie": Cookie
}
headers={
	"Host": "cn-jsyz2-dx-v-04.bilivideo.com",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
	"Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
	"Referer": "https://www.bilibili.com/bangumi/play/ep267851",
	"Origin": "https://www.bilibili.com",
	"Accept-Encoding": "gzip, deflate, br"
}
base_result=requests.get(base_url,headers=base_headers)
cid=[]

ccccc=re.findall(r'"cid":.+?[0-9]+,"',base_result.text)
for i in ccccc:
	qqqqq=i[6:-2]
	cid.append(qqqqq)

for i in range(0,1):
	detail_url="https://api.bilibili.com/pgc/player/web/playurl?cid="+cid[i] #这是获取下载视频的地址
	req=requests.get(detail_url,headers=get_headers)
	download_url=re.findall(r'"url":".+?"',req.text)[0][7:-1]
	print(download_url)
	#下载视频的地址
	
	result=requests.get(download_url,headers=headers,stream=True)
	print("downloading....")
	fp=open("./tmp.flv",'wb')
	for chunk in result.iter_content(chunk_size=40960):#流式传输
	    if chunk:
	        fp.write(chunk)
	print("downloading.....[++++++].....success!")
