from QuikKool import MaliNon
url = "http://40.84.141.218/test.html"
working = []
a = MaliNon()
if (a.check(url)):
    a.Features(url)
    a.getSource(url)
    a.finalAppend()
    working.append(a.getResult())
print(working)