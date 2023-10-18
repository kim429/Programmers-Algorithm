import re
def solution(s):
    re_s = re.sub('[^0-9]','', s) #s에서 숫자를 제외하고 지우기
    if s==re_s: #원래 문장 s와 re_s의 일치 여부 확인
        if len(s)==4 or len(s)==6: #길이 검사
            return True
    return False