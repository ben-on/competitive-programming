class Solution:
    def simplifyPath(self, path: str) -> str:
        subs = path.split('/')
        stack = []
        for i in subs:
            if i in ['', '.']: 
                continue
            elif i == '..':
                if stack: stack.pop()
            else:
                stack.append(i)
        return '/' + "/".join(stack)