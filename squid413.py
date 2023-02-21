class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def checkV4(s):
            try: return str(int(s)) == s and 0 <= int(s) <= 255
            except: return False
        def checkV6(s):
            try: return len(s) <= 4 and int(s, 16) >= 0
            except: return False
        if queryIP.count(".") == 3 and all(checkV4(i) for i in queryIP.split(".")):
            return "IPv4"
        if queryIP.count(":") == 7 and all(checkV6(i) for i in queryIP.split(":")):
            return "IPv6"
        return "Neither"   
