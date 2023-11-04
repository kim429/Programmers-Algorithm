def solution(s):
    answer = ''
    s_list = list(map(int, s.split()))
    answer_list = min(s_list), max(s_list)
    answer = ' '.join(str(s) for s in answer_list)
    return answer