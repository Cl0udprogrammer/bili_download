import requests
import re

base_url="https://www.bilibili.com/bangumi/play/ss38262?t=2501"

base_headers={
	"Host": "www.bilibili.com",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
	"Accept-Encoding": "gzip, deflate, br",
	"Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
	"Origin": "https://www.bilibili.com",
	"Connection": "keep-alive",
	"Cookie": "_uuid=3D08BE66-B9EE-B2FB-8C49-A7C43FF1017383524infoc; buvid3=3421E2FD-588A-4236-A780-CC56686B5F0B58489infoc; CURRENT_FNVAL=80; blackside_state=1; rpdid=|(k|kY|))uR|0J'uY|~Rku~m|; PVID=3; bp_video_offset_156890361=536867600581687916; bp_t_offset_156890361=536511105416586945; LIVE_BUVID=AUTO1216074303258508; CURRENT_QUALITY=112; fingerprint3=feec908233851ff2384939fd54d8c841; fingerprint=0968ee1ffc980381de7ae2607fcc980b; fingerprint_s=ac15f4d7f8b1f245e4841d3064a3723e; buivd_fp=3421E2FD-588A-4236-A780-CC56686B5F0B58489infoc; buvid_fp_plain=3421E2FD-588A-4236-A780-CC56686B5F0B58489infoc; buvid_fp=3421E2FD-588A-4236-A780-CC56686B5F0B58489infoc; sid=kj1bodae; DedeUserID=156890361; DedeUserID__ckMd5=a2cbcac8f3ecab85; SESSDATA=5ea8f9e5%2C1638529269%2C2049e*61; bili_jct=531bb9385bb29d31135011f6c3b225c9",
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
	"Cookie": "_uuid=3D08BE66-B9EE-B2FB-8C49-A7C43FF1017383524infoc; buvid3=3421E2FD-588A-4236-A780-CC56686B5F0B58489infoc; CURRENT_FNVAL=80; blackside_state=1; rpdid=|(k|kY|))uR|0J'uY|~Rku~m|; PVID=3; bp_video_offset_156890361=536867600581687916; bp_t_offset_156890361=536511105416586945; LIVE_BUVID=AUTO1216074303258508; CURRENT_QUALITY=112; fingerprint3=feec908233851ff2384939fd54d8c841; fingerprint=0968ee1ffc980381de7ae2607fcc980b; fingerprint_s=ac15f4d7f8b1f245e4841d3064a3723e; buivd_fp=3421E2FD-588A-4236-A780-CC56686B5F0B58489infoc; buvid_fp_plain=3421E2FD-588A-4236-A780-CC56686B5F0B58489infoc; buvid_fp=3421E2FD-588A-4236-A780-CC56686B5F0B58489infoc; sid=kj1bodae; DedeUserID=156890361; DedeUserID__ckMd5=a2cbcac8f3ecab85; SESSDATA=5ea8f9e5%2C1638529269%2C2049e*61; bili_jct=531bb9385bb29d31135011f6c3b225c9"
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
	detail_url="https://api.bilibili.com/pgc/player/web/playurl?cid="+cid[i]
	#detail_url="https://xy120x195x33x203xy.mcdn.bilivideo.cn:4483/upgcxcode/24/28/343922824/343922824_nb2-1-30112.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1622605515&gen=playurlv2&os=mcdn&oi=2026088133&trid=0001302436476b8043218727790b14958c45p&platform=pc&upsig=5e594508605db1021eee168355237a96&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mcdnid=9000317&mid=156890361&bvc=vod&orderid=0,3&agrr=0&logo=A0000100"
	req=requests.get(detail_url,headers=get_headers)
	# print(req.text)
	download_url=re.findall(r'"url":".+?"',req.text)[0][7:-1]
	print(download_url)

	# download_url="https://xy221x181x179x246xy.mcdn.bilivideo.cn:4483/upgcxcode/24/28/343922824/343922824_nb2-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1622605515&gen=playurlv2&os=mcdn&oi=2026088133&trid=0001302436476b8043218727790b14958c45p&platform=pc&upsig=ecb0346fea8b717fccc06765b1dc1ff5&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mcdnid=6000037&mid=156890361&bvc=vod&orderid=0,3&agrr=0&logo=A0000020"
	
	result=requests.get(download_url,headers=headers,stream=True)
	print("downloading....")
	fp=open("./猫和老鼠.flv",'wb')
	for chunk in result.iter_content(chunk_size=40960):
	    if chunk:
	        fp.write(chunk)
	print("downloading.....[++++++].....success!")