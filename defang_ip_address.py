'''
Given a string that contains an IP address, defang the IP address.

INPUT: "1.1.1.1"
OUTPUT: "1[.]1[.]1[.]1"

INPUT: "192.168.0.1"
OUTPUT: "192[.]168[.]0[.]1"

The task is to replace all of the "." with "[.]". You may not use inbuilt functions to REPLACE the characters, parse the characters out on your own and reconstruct the string. The runtime must not be over O(n)
'''
def defang(ip_address:str) -> str:
    res = ''
    for i in ip_address:
        if i == '.':
            res += '[.]'
        else:
            res += i
    return res
# wow = defang("192.168.0.1")
# print(wow)

'''
With the solution you've created above, create a new solution for the below problem. 
Given a list of IP addresses, there are only a few that are approved IP addresses. Any IP starting with 192, 145, 97, and 306 are approved. Any ending with 31 are approved as well. You must DEFANG and return a list with approved addresses
'''

list_of_ip = [
    '192.168.0.1',
    '1.5.0.1',
    '453.55.0.31',
    '1.1.0.31',
    '50.168.0.1',
    '145.168.0.31',
    '192.168.0.1',
    '306.168.0.1',
    '38.168.0.31',
    '168.168.0.1',
    '97.168.0.1',
]
def parse_defang(list_of_ip:list) -> list:
    res = []
    for i in list_of_ip:
        ip = None
        if i[:3] == '192':
            ip = i
        elif i[:3] == '145':
            ip = i
        elif i[:3] == '306':
            ip = i
        elif i[:2] == '97':
            ip = i
        elif i[-2:] == '31':
            ip = i
        if ip:
            res.append(defang(ip))
    return res
yee = parse_defang(list_of_ip)
print(yee)

