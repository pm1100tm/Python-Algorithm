"""
0~9까지의 문자로 된 숫자를 입력 받았을 때,
이 입력 값이 0~9까지의 숫자가 각각 한 번 씩만 사용된 것인지 확인하는 함수를 구하시오.

sample inputs:  0123456789 01234 01234567890 6789012345 012322456789
sample outputs: true       false false       true       false
"""
# 입력받은 숫자의 갯수가 0~9 까지 10개이어야 한다.
# 중복 값이 있다면 false, 없다면 true


def judge_duplicate_num(func):
    num_list = func.split(" ")

    # 1
    result_list = list(map(lambda i: len(i) == len(set(i)) == 10, num_list))
    print(result_list)

    # 2
    for i in num_list:
        print("true" if len(i) == len(set(i)) == 10 else "false", end=" ")

    print()

    # 3
    for i in num_list:
        if len(i) != 10:
            print(False, end=" ")
        else:
            print(False, end=" ") if len(set(i)) != 10 else print(True, end=" ")


judge_duplicate_num(input())

# 첫번 째
# num_list = list(input().split(" "))
# for n in num_list:
#     if len(n) != 10:
#         print(False)
#     else:
#         print(False) if len(set(n)) != 10 else print(True)

# 두번 째
# for i in input().split(" "):
#     if len(i) != 10:
#         print(False)
#     else:
#         print(False) if len(set(i)) != 10 else print(True)

#세번 째
# for i in input().split(" "):
#     print("true" if len(i) == len(set(i)) == 10 else "false")


# 네번 째
# result_list = list(map(lambda i: len(i) == len(set(i)) == 10, input().split()))
# print(result_list)