class STR(str):
    def compare(self, other):
        ids = ''.join(self.split()[0])
        ido = ''.join(other.split()[0])
        contents = ' '.join(self.split()[1:])
        contentso = ' '.join(other.split()[1:])

        if contents == contentso:
            return ids < ido
        return contents < contentso

    def __lt__(self,  other):
        return self.compare(other)


class Solution:
    def reorderLogFiles(self, logs: List[STR]) -> List[STR]:
        digits = []
        letters = []

        for log in logs:
            nxt = log.split()[1]
            try:
                int(nxt)
                digits.append(log)
            except ValueError:
                letters.append(log)
        letters = sorted(letters, key=STR)
        
        letters.extend(digits)
        
        return letters