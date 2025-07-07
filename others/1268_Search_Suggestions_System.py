class Trie:
    def __init__(self):
        self.child = dict()
        self.words = list()


class Solution:
    def suggestedProducts(self, products, searchWord):
        def addWord(root, word):
            cur = root
            for ch in word:
                if ch not in cur.child:
                    cur.child[ch] = Trie()
                cur = cur.child[ch]
                cur.words.append(word)
                cur.words.sort()
                if len(cur.words) > 3:
                    cur.words.pop()

        root = Trie()
        for word in products:
            addWord(root, word)

        ans = list()
        cur = root
        flag = False
        for ch in searchWord:
            if flag or ch not in cur.child:
                ans.append(list())
                flag = True
            else:
                cur = cur.child[ch]
                ans.append(cur.words)

        return ans


if __name__ == '__main__':
    sol = Solution()
    products = ["mobile","mouse","moneypot","monitor","mousepad"]
    searchWord = "mouse"
    print(sol.suggestedProducts(products,searchWord))