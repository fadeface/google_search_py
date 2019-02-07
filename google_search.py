# -*- coding: utf-8 -*-
from googlesearch import search
import requests

def google_search(query, limit=10):
	urls = []
    for url in search(query, lang="jp", num=limit):
        urls.append(url)
	return urls


def main():
    google_search("qiita")


if __name__ == '__main__':
    main()
