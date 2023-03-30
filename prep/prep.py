import sys

class KmpMatcher:
    def __init__(self, pattern):
        self.pattern = pattern
        self.table = [0] * len(self.pattern)

        for i in range(1, len(self.pattern)):
            j = self.table[i - 1]
            while self.pattern[i] != self.pattern[j] and j > 0:
                j = self.table[j - 1]
            if self.pattern[i] == self.pattern[j]:
                self.table[i] = j + 1 
            else:
                self.table[i] = j

    def match(self, text):
        ret = []
        j = 0
        
        for i in range(len(text)):
            while text[i] != self.pattern[j] and j > 0:
                j = self.table[j - 1]
            if text[i] == self.pattern[j]:
                j += 1
            if j == len(self.pattern): 
                ret.append(i - (j - 1))
                j = self.table[j - 1]

        return ret

if __name__ == "__main__":
    from termcolor import colored
    pattern = sys.argv[1]
    matcher = KmpMatcher(pattern)
    for line in sys.stdin:
        matched = matcher.match(line)
        if len(matched):
            l, m = 0, 0;
            for m in matched:
                print(line[l:m], end="")
                print(colored(pattern, "red", attrs=["bold"]), end="")
                l = m
            print(line[m+len(pattern):], end="")
