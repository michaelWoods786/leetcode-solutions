class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        hashy = {}
        hashy2 = {}
        for i in range(len(word1)):
            if word1[i] not in hashy:
                hashy[word1[i]] = 0
        
        if (hashy[word1[i]] == 0):
            for j in range(len(word1)):
                if word1[i] == word1[j]:
                    hashy[word1[i]]+=1
        
        for i in range(len(word2)):
            if word2[i] not in hashy2:
                hashy[word2[i]] = 0

            if( hashy[word2[i] == 0]):
                for j in range(len(word2)):
                    if word[i]==word[j]:
                        hashy2[word[i]]+=1
        
        if hashy.keys == hashy2.keys:
            hashySet = [hashy[key] for key in hashy.keys()]
            hashySet2 = [hashy[key] for key in hashy2]
            if set(hashySet) == set(hashySet2):
                return True

        return False