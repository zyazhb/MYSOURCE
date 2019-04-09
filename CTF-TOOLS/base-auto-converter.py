'''
多次base64,base32,base16编码
自动转换明文
BY-ZYA
'''
import codecs
import base64
import re
basestring = b"R1pDRE1SUldHTTNUSU5SV0c1QkRNUkJUR0UzRElOUlVHWkJUTU5KVklZM0RHTlpTRzQ0VE9NQlhHUVpUQU4yRQ=="

while(1):
    base64_flag=0
    basestring = codecs.decode(basestring,"utf8")
    print(basestring+"\n")
    if '{' in basestring:
        break 
    for i in basestring:
        if(i.islower()):
            basestring = base64.b64decode(basestring)
            print("base64 decode:")
            base64_flag=1
            break
    if(base64_flag):
        continue
    elif(re.match('^[G-Z]',basestring)):
        print("base32 decode:")
        basestring=base64.b32decode(basestring)
        continue
    else:
        print("base16 decode:")
        basestring=base64.b16decode(basestring)
        continue
print ("-"*50+"\nPlain text: "+basestring)
