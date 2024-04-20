n = input()
arr = list(map(int, input().split()))
n = len(arr)

if n < 7:
    print(-1)
else:
    p1, p2 = 0, 7
    max_count_best_marks = -1
    while p2 <= n:
        count_best_marks = 0
        is_good_week = True
        for a in arr[p1:p2]:
            if a == 2 or a == 3:
                is_good_week = False
                break
            if a == 5:
                count_best_marks += 1
        if is_good_week:
            max_count_best_marks = max(max_count_best_marks, count_best_marks)
        p1 += 1
        p2 += 1
    print(max_count_best_marks)