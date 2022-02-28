word_num = int(input())
wordlist = list(set(list(input() for i in range(word_num))))
sortword = []
for i in wordlist:
    sortword.append((len(i), i))
sorted_words = sorted(sortword)
for len_word, word in sorted_words:
    print(word)

# list에 set을 하면 중복을 제거할 수 있다.
# 튜플 사용, a,b 파라미터
# sorted를 쓰면 앞 숫자, 뒤 문자 기준으로 정렬