""" Problem:
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

"""


def longest_substr(s, k):
    result = ''
    for i in range(0, len(s)):
        aux = ''
        chars = []
        for c in s[i::]:
            if len(chars) < k and c not in chars:
                chars.append(c)
                aux += c
            elif c in chars:
                aux += c
            else: break
        result = aux if len(aux) > len(result) else result
    return result



if __name__ == '__main__':
    print(longest_substr('abcaaaacaakaa', 2))