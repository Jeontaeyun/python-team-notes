# Apache String Compression
# 30m, 1s, 128MB
# https://programmers.co.kr/learn/courses/30/lessons/60057
# 01. 일단 최대한 많은 수를 압축하면 줄어든다.
# - 1단위로 압축을 하면 3개 이상 압축해야 한다.
# - 2단위로 압축하면 2개 이상 압축해야 한다.
# - 3단위 이후로 압축하면
# 02. 문자열은 제일 앞부터 정해진 길이만큼 잘라야 합니다.
# TIP. 문제가 막힐 때는 문제의 입출력 예시 및 제한 사항을 잘 확인하자.
# [Solution] 문자열의 절반의 수까지 완전 탐색

# ! List Chunk Function
def list_chunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]


def compress_string(list):
    buffer = []
    count = 0
    previous = ""
    for i in range(0, len(list)):
        if previous == "":
            previous = list[i]
            continue
        if list[i] == previous:
            count += 1
        else:
            if count == 0:
                buffer.append(previous)
            else:
                buffer.append(str(count+1) + previous)
            count = 0
            previous = list[i]
        if i == len(list)-1:
            if count == 0:
                buffer.append(previous)
            else:
                buffer.append(str(count+1) + previous)

    return "".join(buffer)


def solution(s):
    compressed_string_list = []
    answer = len(s)
    length = len(s)
    half_length = length // 2

    for i in range(1, half_length+1):
        result = list_chunk(s, i)
        compressed_string = compress_string(result)
        answer = min(len(compressed_string), answer)
    return answer


result = solution("abcabcdede")
print(result)
