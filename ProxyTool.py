import random
import urllib2

def get_proxies():
    return [ "41.216.171.154:8080", "89.22.16.53:8080", "212.138.92.17:8080"]
        
class UrlOpener():
    def __init__(self):
        # getting a list of proxies
        self.proxies = get_proxies()

        # updating proxy 
        self.update_proxy()
        
    def __str__(self):
        # return current proxy ip address
        return self.curr_proxy_ip
        
    def update_proxy(self):
        succeed = False
        # keep trying updating IP until we get one that's working
        while(~succeed):
            try:
                # picking a random IP
                idx = random.randint(0, len(self.proxies) - 1)
                self.curr_proxy_ip = self.proxies[idx]
                proxies = {"http":"http://%s" % self.curr_proxy_ip}
                
                # updating current IP
                proxy_support = urllib2.ProxyHandler(proxies)
                opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler(debuglevel=1))
                urllib2.install_opener(opener)
                
                # testing new proxy
                a = self.open("http://ip-api.com/", reset=True)
                succeed = ~(a==None)
            except:
                pass
        
    def open(self, url, reset=False):
        # update proxy at random
        if random.random()>0.5 and reset:
            self.update_proxy()
        headers={'User-agent' : 'Mozilla/5.0'}
        req = urllib2.Request(url, None, headers)
        content = urllib2.urlopen(req).read()
        return content
        
if __name__=="__main__":
    opener = UrlOpener()
    content = opener.open("http://www.google.com")
    with open("page.html", "w") as f:
        f.write(content)