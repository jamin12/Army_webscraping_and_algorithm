import collections
import re
def solution(bridge_length, weight, truck_weights):
    answer = 1
    t = collections.deque()
    truck_weights.reverse()
    deq = collections.deque()
 
    while True:
        if t:
            t = collections.deque(map(lambda x: x+1,t))
            answer += 1
        if truck_weights and sum(deq) + truck_weights[-1] <= weight:
            deq.append(truck_weights.pop())
            t.append(0)
        if t[0] == bridge_length:
            t.popleft()
            deq.popleft()
        if not deq and not truck_weights:
            return answer
        
def panrindrom(pan_str):
    pan_str = pan_str.lower()
    pan_str = re.sub('[^a-z0-9]','',pan_str) # 정규식 : 숫자랑 문자가 아닌것을 공백으로 바꾼다
    return pan_str == pan_str[::-1]

def reverse_String(list_str):
    left, right = 0, len(list_str)-1
    while left < right:
        #temp 안만들고 변수 서로 바꾸기
        list_str[left] , list_str[right] = list_str[right] , list_str[left] 
        left += 1
        right -=1
    # list_str.reverse() 사실 이렇게 하면 한번에 뒤집어짐

def alignment(log_str):
    letter, digits = [] , []
    for log in log_str:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letter.append(log)
    letter.sort(key=lambda x: (x.split()[1:],x.split()[0]))
    return letter + digits

def mostCommonWord(paragraph,banned):
       word = [word for word in re.sub("r[^\w]",' ',paragraph).lower().split() if word not in banned]
       counter = collections.Counter(word) # Counter: 튜플 리스트로 ("값","개수")로 저장된다
       counter.most_common(1)[0][0]

def group_Anagrams(strs):
    anagrams = collections.defaultdict(list)
    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    return anagrams.values()
if __name__ == '__main__':
    # 프로그래머스 다리위를 지나는 트럭
    # solution(2,10,[7,4,5,6])
    # solution(100,100,[10,10,10,10,10,10,10,10,10,10])
    # solution(100,100,[10])

#####################################################################################################
#####################################################################################################
    #팰린드롬(거꾸로 뒤집어도 같은 글자)    
    # panrindrom("A man, a plan, a canal: Panama")

#####################################################################################################
#####################################################################################################
    #투 포인터 이용해 문자열 뒤집기
    # reverse_String(["H","E","L","L","O"])

#####################################################################################################
#####################################################################################################
    #로그 파일 재정렬
    # alignment(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"])

#####################################################################################################
#####################################################################################################
    #가장 흔한 단어
    # mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])

#####################################################################################################
#####################################################################################################
    #그룹 애너그램
    group_Anagrams(["eat","tea","tan","ate","nat","bat"])