# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def twoNumberSum(array, targetSum):
    # Write your code here.
    dic = {}
    for n in array:
        dic[n] = targetSum - n
    for complementary in dic.values():
        if complementary in array:
            return [complementary, targetSum + complementary]


def getWrongAnswers(N: int, C: str) -> str:
    # Write your code here
    string = ""
    for c in C:
        if c == "A":
            string += "B"
        else:
            string += "A"
    return string


def getHitProbability(R, C, G) -> float:
    # Write your code here
    battleships = 0
    for c in range(C) - 1:
        for r in range(R) - 1:
            if G[C][R]:
                battleships += 1

    return battleships


def isPalindrome(string):
    # Write your code here.
    return string == string[::-1]


def getMilestoneDays(revenues, milestones):
    # Write your code here
    days_accomplished = []
    total_revenues = 0
    print(len(revenues))
    print(range(len(revenues)))
    for r in range(len(revenues)):
        print(r)
        total_revenues += revenues[r]
        if total_revenues in milestones:
            days_accomplished.append(r + 1)

    return days_accomplished if days_accomplished else -1


def solution(a):
    result = []
    for index in range(len(a)):
        if index == len(a) - 1:
            result.append(a[index][0] + a[0][len(a[0])-1])
        else:
            first_character = a[index][0]
            last_character = a[index + 1][len(a[index + 1])-1]
            result.append(first_character + last_character)

    return result

def solution_number(number):
    count = 0
    res = [number[i: j] for i in range(len(number))
           for j in range(i + 1, len(number) + 1)]
    for r in res:
        if int(r)%3 == 0:
            count += 1

    return count

def permute(a, l, r):
    if l==r:
        print (a)
    else:
        for i in range(l,r):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(solution_number("200"))
    a = ["cat", "dog", "ferret", "scorpion"]
    print(solution(a))

    # revenues = [100, 200, 300, 400, 500]
    # milestones = [300, 800, 1000, 1400]
    # print(getMilestoneDays(revenues, milestones))
    # print("holi" * 5)
    # print(isPalindrome("aba"))
    # battle = [[1, 2, 3], [4, 5, 6]]
    # print(getHitProbability(2,3,battle))
    # print()
    # print(getWrongAnswers(3, "ABA"))
    # array = [3, 5, -4, 8, 11, 1, -1, 6]
    # target = 10
    # print(twoNumberSum(array, target))
    # print(cipher("xyz", 2))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
