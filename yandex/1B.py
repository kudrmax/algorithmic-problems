def foo(arr):
    match1 = arr[0]
    match2 = arr[1]
    where = arr[2][0]

    score = {
        'team1': match1[0] + match2[0],
        'team2': match1[1] + match2[1]
    }

    if score['team1'] > score['team2']:
        return 0

    score_in_one_match = {
        'team1': {
            'away_game': 0
        },
        'team2': {
            'away_game': 0
        }
    }

    delta = score['team2'] - score['team1']

    if where == 2:  # 1 команда играла 1 игру в гостях
        score_in_one_match['team1']['away_game'] = match1[0]
        score_in_one_match['team2']['away_game'] = match2[1]
    else: # 1 команда играла 2 игру в гостях
        score_in_one_match['team1']['away_game'] = match2[0] + delta
        score_in_one_match['team2']['away_game'] = match1[1]

    is_delta_enough = True
    if score_in_one_match['team1']['away_game'] <= score_in_one_match['team2']['away_game']:
        is_delta_enough = False

    if is_delta_enough:
        return delta
    return delta + 1

f = open('input.txt', 'r')

arr = []
for line in f:
    arr.append(list(map(int, line.split(':'))))
print(foo(arr))