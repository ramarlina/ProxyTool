ProxyTool
=========

ProxyTool can be used to get web pages anonymously with the urllib2 library in Python. The way it works is it randomly
selects a proxy from a list of proxy and then accesses the page through that proxy.

This code can be used with MapReduce for distributed data scrapping. I created a simple example using <a href="https://github.com/michaelfairley/mincemeatpy">Michael Fairley's Mincemeat.py</a>.
I attached a copy of mincemeat.py but for the latest version of the MapReduce implementation, please <a href="https://github.com/michaelfairley/mincemeatpy">go to his Github profile</a>.

Using ProxyTool:
================
    First, define list of proxy in PoxyTool.py.
    
    # Create an url opener
    opener = ProxyTool.UrlOpener()
    
    # open and read url
    content = opener.open("http://www.example.com")
    
    
Using ProxyTool with MapReduce: see fetch.y