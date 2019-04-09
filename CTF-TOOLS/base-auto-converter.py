'''
多次base64,base32,base16编码
自动转换明文
BY-ZYA
'''
import codecs
import base64
import re
basestring = b"Vm0weGQxSXlSblJWV0d4WFlUSm9WRll3WkRSV01XeHlXa1pPYUZKc1NsWldSM1JQVmpGS2RHVkVRbFZXYkhCUVdWZHplRll4VG5OWGJGcFhaV3RhU1ZkV1kzaFRNVTVYVW01S2FGSnRhRzlVVm1oRFZWWmFjbHBFVWxSaVZrWTFWa2QwYTJGc1NuUlZiRkphWWtkU2RscFdXbXRXTVZaeVdrWndWMkV6UWpaV01uUnZWakZhZEZOc1dsaGlSMmhvVm1wT2IxTXhjRmhsUjBaWFlrZFNlVll5ZUVOV01rVjNZMFpTVjFaV2NGTmFSRVpEVld4Q1ZVMUVNRDA9="
while(1):
    base64_flag=0
    basestring = codecs.decode(basestring,"utf8")
    print(basestring)
    if '{' in basestring:
        break 
    for i in basestring:
        if(i.islower()):
            basestring = base64.b64decode(basestring)
            # print "base64 encode"           
            base64_flag=1
            break
    if(base64_flag):
        continue
    elif(re.match('^[G-Z]',basestring)):
        # print "base32 encode"       
        basestring=base64.b32decode(basestring)
        continue
    else:
        # print "base16 encode"       
        basestring=base64.b16decode(basestring)
        continue
    print (basestring)
