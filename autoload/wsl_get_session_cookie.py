# -*- coding: utf-8 -*-

"""
File: wsl_get_seeion_cookie.py
Author: xdcn4066
Email: xdcn4066@corp.netease.com
Description:
	获取cookie
"""

import keyring
import browser_cookie3
import pickle


def get_cookie(browser, lc_base):
	session_cookie_raw = ""
	cookies = getattr(browser_cookie3, browser)(domain_name=lc_base.split('/')[-1])
	for cookie in cookies:
		if cookie.name == 'LEETCODE_SESSION':
			session_cookie_raw = pickle.dumps(cookie, protocol=0).decode('utf-8')
			break
	else:
		print('Leetcode session cookie not found. Please login in browser.')
		return ""
	return session_cookie_raw


if __name__ == "__main__":
	import sys
	browser = sys.argv[1]
	lc_base = sys.argv[2]
	cookie = get_cookie(browser, lc_base)
	print(cookie)
