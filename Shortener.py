import pyshorteners
import validators
url=input("Enter a link: ")
def shorten_url(url):
    s=pyshorteners.Shortener()
    if not validators.url(url):
        print('Url is not valid')
    else:
        print(s.tinyurl.short(url))
shorten_url(url)
