#异或计算器BYZYA
import optparse

# console colors
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray
E = '\033[0m'   #end
def work(elem):
    x = 32
    y = 32
    numlist=[]
    print(elem+" xor:\n")
    while y >= 32 and y <= 126:
        while x>=32 and x<=126:
            if chr(x^y) == elem:
                #print("\nx= "+chr(x)+" b=",chr(y))
                numlist.append(chr(x)+"^"+chr(y))
            if x == 47:
                x = 58
            elif x == 64:
                x=91
            elif x == 96:
                x=123
            else:
                x = x+1
        x =32
        if y == 47:
            y = 58
        elif y == 64:
            y=91
        elif y == 96:
            y=123
        else:
            y = y+1
    for i in numlist:
        print(i,end=C+" | "+E)
    print("\n")

def main():
    parser = optparse.OptionParser("xor calculator by ZYA\n useage %prog "+"-o <options> --s1 <string> --s2 <string>")
    parser.add_option('-o', dest='options', type='string', help='specify option (encode decode)')
    parser.add_option('--s1', dest='s1', type='string', help='specify string1')
    parser.add_option('--s2', dest='s2', type='string', help='specify string2')
    (options, args) = parser.parse_args()
    if options.options == 'encode' and options.s1 != None:
        string = options.s1
        arr = list(string)
        print(arr)
        for i in range(arr.__len__()):
            work(arr[i])
        print('done!')
        exit(0)
    elif options.options == 'decode' and options.s1 != None and options.s2 != None:
        string1 = options.s1
        # string1 = '@@@\\'
        list1 = list(string1)
        string2 = options.s2
        # string2 = '&,!;'
        list2 = list(string2)
        print(list1,list2)
        print('The string is: ')
        for i in range(list1.__len__()):
            print(chr(ord(list1[i]) ^ ord(list2[i])), end='')
    else:
        print(parser.usage)
        exit(0)
if __name__ == '__main__':
    main()

'''''
while True:
    print('\n-----xor caluculator by zya!------')
    chfunc = input('|choose a function to use:       |\n|1.str to xor                    |\n|2.xor to str                    |\n----------------------------------')
    if chfunc == '1':
        string = input('pls input a string\n')
        arr = list(string)
        print(arr)
        for i in range(arr.__len__()):
            work(arr[i])
        print('done!')
    elif chfunc == '2':
        string1 = input('pls input xor x:\n')
        #string1 = '@@@\\'
        list1 = list(string1)
        string2 = input('pls input xor y:\n')
        #string2 = '&,!;'
        list2 = list(string2)
        print('The string is: ')
        for i in range(list1.__len__()):
            print(chr(ord(list1[i])^ord(list2[i])),end='')
'''''
