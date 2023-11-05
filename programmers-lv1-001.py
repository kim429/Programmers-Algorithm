def solution(left, right):
    answer = 0
    while left!=right+1: #left에서 right까지 반복
        count = 0 #약수 개수 초기화
        for i in range(1, left+1): #약수 개수 구하기
            if left%i ==0: #i가 left로 나누어 떨어진다면
                count +=1 #약수의 개수 +1
        if count%2==0: #약수의 개수 홀짝 검사
            answer +=left #짝수
        else:
            answer -=left #홀수
        left +=1
    return answer