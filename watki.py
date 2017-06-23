from concurrent import futures
from decorator import clock
import requests

workers = 5  # a jak dla 1?? 10??
urls = ['http://www.google.com',
        'http://www.google.pl',
        'https://www.diki.pl/',
        'http://www.onet.pl',
        'https://pl.wikipedia.org',
        'http://getbootstrap.com/',
        'http://www.un.com',
        'http://www.yahoo.com',
        'http://www.bbc.com',
        'https://docs.djangoproject.com']
        
urls = urls # * 2 ??

def f(url):
    resp = requests.get(url)
    print('\n\n\n', url, '\n\n', resp.content[:400])
    if "bootstrap" in str(resp.content): print("\n\n{} uses BOOTSTRAP !!!!!!!!!".format(url))
    return url

@clock
def parallel():
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(f, urls)
    print(list(res))
    
@clock
def sequence():
    for url in urls:
        f(url)
        
if __name__ == '__main__':
    parallel()
    sequence()
    print(':-)')