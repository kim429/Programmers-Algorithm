def mark(q, n, a):
    k = 0
    result = 0
    if len(a) % 5 != 0:
        q[:n - 1]
    while k < n:
        if a[k] == q[k % 5]:
            result += 1
        k += 1
    return result


def solution(answers):
    n = len(answers)
    s1 = list([i for i in range(1, 6)])
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    k = 0
    sum1 = 0
    if len(answers) % 5 != 0:
        s1[:n]
        print("나누어떨어지지않음", s1, n)
    while k < n:
        if answers[k] == s1[k % 5]:
            print("학생 답:", s1[k % 5], "정답:", answers[k], "총합:", sum1)
            sum1 += 1
        k += 1

    k = 0
    sum2 = 0
    if len(answers) % 5 != 0:
        s2[:5]
        print("나누어떨어지지않음", s2, n)
    while k < n:
        if answers[k] == s2[k % 8]:
            print("학생 답:", s2[k % 8], "정답:", answers[k], "총합:", sum2)
            sum2 += 1
        k += 1

    k = 0
    sum3 = 0
    if len(answers) % 5 != 0:
        s3[:5]
        print("나누어떨어지지않음", s3, n)
    while k < n:
        if answers[k] == s3[k % 10]:
            print("학생 답:", s3[k % 10], "정답:", answers[k], "총합:", sum3)
            sum3 += 1
        k += 1

    mark_list = [0, sum1, sum2, sum3]

    print(mark_list)

    if max(mark_list) == min(mark_list):
        answer = [1, 2, 3]
    else:
        answer = max(mark_list)
        answer = [i for i, v in enumerate(mark_list) if v == answer]

    return answer