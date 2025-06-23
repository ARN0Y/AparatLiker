import requests, re, time, threading, os, sys

class AparatLike(object):
    def __init__(self):
        r = '\033[31m'
        g = '\033[32m'
        y = '\033[33m'
        b = '\033[34m'
        m = '\033[35m'
        c = '\033[36m'
        w = '\033[37m'
        rr = '\033[39m'
        self.CountGood = 0
        self.CountBad = 0
        self.cls()
        self.print_logo()
        try:
            FileProxy = open(raw_input('  {}Input Proxy.txt{}>>{} '.format(w, c, y)), 'r').read().splitlines()
            link = raw_input('  {}Input Aparat video Link{}>>{} '.format(w, c, y))
        except Exception, e:
            print('{}        Error:{} {}'.format(r, w, e))
            sys.exit()
        self.Main(FileProxy, link)

    def cls(self):
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])

    def print_logo(self):
        clear = "\x1b[0m"
        r = '\033[31m'
        g = '\033[32m'
        y = '\033[33m'
        b = '\033[34m'
        m = '\033[35m'
        c = '\033[36m'
        w = '\033[37m'
        rr = '\033[39m'

        x = """
        {}              $$$$$$$\           $$$$$$$\         $$$$$$$$\ 
        {}              $$  __$$\          $$  __$$\        \__$$  __|
        {}     $$$$$$\  $$ |  $$ |$$$$$$\  $$ |  $$ | $$$$$$\  $$ |   
        {}     \____$$\ $$$$$$$  |\____$$\ $$$$$$$  | \____$$\ $$ |   github.com/ARN0Y
        {}     $$$$$$$ |$$  ____/ $$$$$$$ |$$  __$$<  $$$$$$$ |$$ |   
        {}    $$  __$$ |$$ |     $$  __$$ |$$ |  $$ |$$  __$$ |$$ | Iran-cyber.Net 
        {}    \$$$$$$$ |$$ |     \$$$$$$$ |$$ |  $$ |\$$$$$$$ |$$ |   
        {}     \_______|\__|      \_______|\__|  \__| \_______|\__|   
               
        {}                 Aparat Liker {}({} Open Source Project{} )
        {}          You Are Free To use this code in Your Projects                                      
    """.format(g, g, g, w, w, w, r, r, r, y, c, y, c, w)
        print(x)

    def GoTLike(self, Link, proxyz):
        try:
            proxy = {'http': proxyz,
                     'https': proxyz}
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0',
                       'Accept': '*/*'}
            Send = requests.get(Link, timeout=5, headers=headers, proxies=proxy)
            GetLike_Link = re.findall('<a href="(.*)" onclick="videoOne_like()', Send.text.encode('utf-8'))[0][0]
            like = requests.get(GetLike_Link, timeout=5, headers=headers, proxies=proxy)
            if 'video_like_add' in like.text.encode('utf-8'):
                self.CountGood = self.CountGood + 1
            else:
                self.CountBad = self.CountBad + 1
        except Exception, e:
            self.CountBad = self.CountBad + 1

    def Main(self, prox, url):
        r = '\033[31m'
        g = '\033[32m'
        y = '\033[33m'
        b = '\033[34m'
        m = '\033[35m'
        c = '\033[36m'
        w = '\033[37m'
        rr = '\033[39m'
        thread = []
        print('\n\n')
        for proxy in prox:
            print('{}     Successfully Likes{}:{} {}').format(w, c, g, self.CountGood),
            print('{}     Not Successfully Likes{}:{} {}').format(w, c, r, self.CountBad),
            sys.stdout.flush()
            print("\r"),
            t = threading.Thread(target=self.GoTLike, args=(url, proxy))
            t.start()
            thread.append(t)
            time.sleep(0.08)
        for j in thread:
            j.join()
        #print('{}({}--------------------------------------------------------------------------{})').format(r, y, r)
        #print('{}     Successfully Likes{}:{} {}').format(w, c, g, self.CountGood)
        #print('{}     Not Successfully Likes{}:{} {}').format(w, c, r, self.CountBad)

AparatLike()
