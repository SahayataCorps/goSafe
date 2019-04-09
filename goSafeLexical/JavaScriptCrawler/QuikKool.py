import requests
from find import Finale
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.wait import WebDriverWait
import bs4 as bs
import urllib2

class MaliNon:
    exists = 0
    url = ''
    feat = []
    def reset(self):
        self.features = {
        "noofsrc": 0,
        "hiddenjs": 0,
        "iframes": 0,
        "subStringjs": 0,
        "fromCharCodejs": 0,
        "evaljs": 0,
        "setTimeoutjs": 0,
        "documentWritejs": 0,
        "createElementjs": 0,
        "escapejs": 0,
        "unescapejs": 0,
        "linkjs": 0,
        "execjs": 0,
        "searchjs": 0,
        "strRev":0,
        "strReplace":0,
        "dbase64":0
        }
    def stringcon(self,no):
        retstr = ''
        for x in no:
            if ord(x)<128 or ord>-128:
                retstr+=x
        return retstr

    def check(self, url):
        try:
            request = requests.get(url)
            self.exists= 1
        except:
            self.exists = 0
        return self.exists

    def Features(self, url):
        a = Finale()

        b = a.getFeatures(url)
        return b

    def hfeatures(self, source):
        # html features
        self.features["noofsrc"] += (source.count("<link") + source.count("<script"))
        self.features["iframes"] += source.count("<iframes")

    def jsfeatures(self, source):
        self.features["hiddenjs"] += (source.count("hidden") + source.count("style.visibility"))
        self.features["subStringjs"] += source.count("subScript(")
        self.features["fromCharCodejs"] += source.count("fromCharCode(")
        self.features["evaljs"] += source.count("eval(")
        self.features["setTimeoutjs"] += source.count("setTimeout(")
        self.features["documentWritejs"] += source.count("document.write(")
        self.features["createElementjs"] += source.count("createElement(")
        self.features["escapejs"] += source.count("escape(")
        self.features["unescapejs"] += source.count("unescape(")
        self.features["linkjs"] += source.count("link(")
        self.features["execjs"] += source.count("exec(")
        self.features["searchjs"] += source.count("search(")
        self.features["strRev"] += source.count("reverse(")
        self.features["strReplace"] += source.count("replace(")
        self.features["dbase64"] += source.count("dbase64(")
        self.hfeatures(source)

    def getSource(self, url):
        options = Options()
        options.add_argument('-headless')
        options.headless = True
        driver = Firefox(executable_path='C:\Users\hp\PycharmProjects\goSafe - Copy\Req\geckodriver', options=options)
        # wait = WebDriverWait(driver, timeout=10)
        driver.get(url)
        # wait.until(expected.visibility_of_element_located((By.NAME, 'q'))).send_keys('headless firefox' + Keys.ENTER)
        # swait.until(expected.visibility_of_element_located((By.CSS_SELECTOR, '#ires a'))).click()
        sauce = driver.page_source

        soup = bs.BeautifulSoup(sauce, "lxml")

        a = []
        internal = []
        int_count = 0
        htmlfeat = soup.find("html")
        htmlfeat = str(htmlfeat)
        self.hfeatures(htmlfeat)
        for script in soup.find_all("script"):
            a.append(script.get("src"))
            txt = script.text
            if txt != '':
                internal.append(txt)
                int_count += 1

        for x in a:
            if x == None:
                for inte in internal:

                    self.jsfeatures(self.stringcon(inte))
            elif x.startswith('/'):

                dummy = url + x
                try:
                    dummy_sauce = urllib2.urlopen(dummy).read()
                    dummy_soup = bs.BeautifulSoup(dummy_sauce, "lxml")
                    div = dummy_soup.find("body")
                    nop = self.stringcon(div)
                    self.jsfeatures(nop)
                except:
                    continue

            elif x.startswith('..'):
                dummy = url + x[2:]
                try:
                    dummy_sauce = urllib2.urlopen(dummy).read()
                    dummy_soup = bs.BeautifulSoup(dummy_sauce, "lxml")
                    div = dummy_soup.find("body")
                    nop = self.stringcon(div)
                    self.jsfeatures(nop)
                except:
                    continue

            elif x.startswith("http"):
                dummy = x
                try:
                    dummy_sauce = urllib2.urlopen(dummy).read()
                    dummy_soup = bs.BeautifulSoup(dummy_sauce, "lxml")
                    div = dummy_soup.find("body")
                    nop = self.stringcon(div)
                    self.jsfeatures(nop)
                except:
                    continue


    def finalAppend(self, url):

        features2 = [self.features["noofsrc"]
        ,self.features["hiddenjs"]
        ,self.features["iframes"]
        ,self.features["subStringjs"]
        ,self.features["fromCharCodejs"]
       ,self.features["evaljs"]
        ,self.features["setTimeoutjs"]
        ,self.features["documentWritejs"]
        ,self.features["createElementjs"]
        ,self.features["escapejs"]
        ,self.features["unescapejs"]
       ,self.features["linkjs"]
        ,self.features["execjs"]
        ,self.features["searchjs"]
        ,self.features["strRev"]
        ,self.features["strReplace"]
        ,self.features["dbase64"]]



        return features2

    


