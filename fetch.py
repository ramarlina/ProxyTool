import mincemeat
import pandas

# list of urls that we want to fetch
data = ["http://www.example.com", "http://www.example.com"]

def save_data(data):
    pass

def mapfn(k, url):
    from Crawler import ProxyTool
    from db import db
    import numpy
    Opener = ProxyTool.UrlOpener()
    data = Opener.open(url)
    save_data(data)
    yield 1, 2
        
def reducefn(k, vs):
    import pandas
    result = 0
    for v in vs:
        result += v
    return result
    
def run_server():
    print "Starting up"
    s = mincemeat.Server()
    print "Prep data"
    s.datasource = dict(enumerate(data))
    s.mapfn = mapfn
    s.reducefn = reducefn
    print "starting server"
    results = s.run_server(password="Asdfg44%")
   
run_server()