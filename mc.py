import memcache
s = memcache.Client(["127.0.0.1:11211"])
s.set("benhua", 'male')
print s.get('benhua')
