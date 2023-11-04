def solution(s):
    answer = ''
    for i in s.split(' '):  #한 단어 씩 자르기
        if i == '': #공백 2번 예외 처리
            answer = answer + ' '
        else:
            answer = answer + i[0].upper() + i[1:].lower() + ' '    #JadenCase - 첫 문자 대문자, 그 외의 알파벳 소문자
    return answer[:-1]  #마지막 단어에 추가되는 불필요한 공백 지우기