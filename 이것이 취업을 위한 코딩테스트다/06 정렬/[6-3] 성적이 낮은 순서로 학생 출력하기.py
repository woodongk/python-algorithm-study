"""
학생의 이름과 점수를 입력받았을때

점수가 낮은 순서대로 "이름" 을 출력하는 방법

입력
2
홍길동 95
이순신 77
출력
이순신 홍길동
"""

if __name__ == '__main__':
    n = int(input())

    students = []
    for i in range(n):
        name, score = input().split()
        students.append((name, int(score)))

    students = sorted(students, key = lambda x: x[1])
    for s in students:
        name, score = s
        print(name, end =' ')