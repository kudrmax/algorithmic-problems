import collections
import re

total_goals_for_pattern = re.compile(r'Total goals for "?([^"]+)"?')
mean_goals_per_game_for_pattern = re.compile(r'Mean goals per game for "?([^"]+)"?')
total_goals_by_pattern = re.compile(r'Total goals by "?([^"]+)"?')
mean_goals_per_game_by_pattern = re.compile(r'Mean goals per game by "?([^"]+)"?')
goals_on_minute_pattern = re.compile(r'Goals on minute (\d+) by "?([^"]+)"?')
goals_on_first_t_minutes_pattern = re.compile(r'Goals on first (\d+) minutes by "?([^"]+)"?')
goals_on_last_t_minutes_pattern = re.compile(r'Goals on last (\d+) minutes by "?([^"]+)"?')
score_opens_by_team_pattern = re.compile(r'Score opens by "?([^"]+)"?')
score_opens_by_player_pattern = re.compile(r'Score opens by "?([^"]+)"?')
match_score_pattern = re.compile(r'"(.*?)" - "(.*?)" (\d+):(\d+)')
goal_pattern = re.compile(r'"?([^"]+)"? (\d+)\'')

with open('input.txt', 'r') as file:
    lines = file.readlines()
commands = []
for command in lines:
    commands.append(command.strip())
commands.reverse()

players = collections.defaultdict(dict)
teams = collections.defaultdict(lambda: collections.defaultdict(int))


def add_data_to_players(name: str, time, match_id, team_name):
    score = {'match_id': match_id, 'time': time}
    if 'scores' not in players[name]:
        players[name]['scores'] = []
    if 'count_first_scores' not in players[name]:
        players[name]['count_first_scores'] = 0
    players[name]['scores'].append(score)
    players[name]['team_name'] = team_name


# teams['HSE']['score_sum'] += 1
# teams['HSE']['count_of_matches'] += 1
# teams['HSE']['count_first_scores'] += 1
# teams['HSE']['count_first_scores'] += 1


print(players)
print(teams)

while len(commands) > 0:
    command = commands.pop()

    match = match_score_pattern.match(command)
    if match:
        team1_name = match.group(1)
        team2_name = match.group(2)
        score1 = int(match.group(3))
        score2 = int(match.group(4))
        match_id = f"{team1_name} - {team2_name} {score1}:{score2}"

        print(f"Done: {team1_name} - {team2_name} {score1}:{score2}")

        time1, time2 = 0, 0
        player1_name, player2_name = '', ''
        for score, team_name in zip([score1, score2], [team1_name, team2_name]):
            for i in range(score):
                command = commands.pop()
                match = goal_pattern.match(command)
                if match:
                    player_name = match.group(1)
                    time = int(match.group(2))
                    add_data_to_players(name=player_name, time=time, match_id=match_id, team_name=team_name)
                    print(f"Done: {player_name} {time}")
                    if i == 0 and team_name == team1_name:
                        time1 = time
                        player1_name = player_name
                    if i == 0 and team_name == team2_name:
                        time2 = time
                        player2_name = player_name

        teams[team1_name]['score_sum'] += score1
        teams[team1_name]['count_of_matches'] += 1

        if time1 < time2:
            teams[team1_name]['count_first_scores'] += 1
            if 'count_first_scores' not in players[player1_name]:
                players[player1_name]['count_first_scores'] = 0
            players[player1_name]['count_first_scores'] += 1
        else:
            teams[team2_name]['count_first_scores'] += 1
            if 'count_first_scores' not in players[player2_name]:
                players[player2_name]['count_first_scores'] = 0
            players[player2_name]['count_first_scores'] += 1

    match = total_goals_for_pattern.match(command)
    if match:
        team_name = match.group(1)
        total_goals = teams[team_name]['score_sum']
        print(f"Done: Total goals for '{team_name}' ---> {total_goals}")

    match = mean_goals_per_game_for_pattern.match(command)
    if match:
        team_name = match.group(1)
        score_count = teams[team_name]['score_sum']
        match_count = teams[team_name]['count_of_matches']
        mean_goals = score_count / match_count if match_count != 0 else 0
        print(f"Done: Mean goals per game for {team_name} ---> {mean_goals}")

    match = total_goals_by_pattern.match(command)
    if match:
        player_name = match.group(1)
        scores = players[player_name]['scores'] if 'scores' in players[player_name] else []
        score_count = len(scores)
        print(f"Done: Total goals by {player_name} ---> {score_count}")

    match = mean_goals_per_game_by_pattern.match(command)
    if match:
        player_name = match.group(1)
        scores = players[player_name]['scores']
        team_name = players[player_name]['team_name']
        match_count = teams[team_name]['count_of_matches']
        score_count = len(scores)
        mean_goals = score_count / match_count if match_count != 0 else 0
        print(f"Done: Mean goals per game by {player_name} ---> {mean_goals}")

    match = goals_on_minute_pattern.match(command)
    if match:
        time = int(match.group(1))
        player_name = match.group(2)

        scores = players[player_name]['scores'] if 'scores' in players[player_name] else []
        scores_sum = 0
        for score in scores:
            print(score)
            t = score['time']
            if t == time:
                scores_sum += 1
        print(f"THIS: Goals on minute {time} by {player_name} ---> {scores_sum}")

    match = goals_on_first_t_minutes_pattern.match(command)
    if match:
        print(f"Goals on first {match.group(1)} minutes by {match.group(2)}")

    match = goals_on_last_t_minutes_pattern.match(command)
    if match:
        print(f"Goals on last {match.group(1)} minutes by {match.group(2)}")

    match = score_opens_by_team_pattern.match(command)
    if match:
        team_or_player_name = match.group(1)

        is_team = False
        if team_or_player_name in teams:
            is_team = True

        if is_team:
            open_score = teams[team_or_player_name]['count_first_scores']
        else:
            open_score = players[team_or_player_name]['count_first_scores'] if team_or_player_name in players else 0
        print(f"Score opens by {team_or_player_name} ---> {open_score}")

print(players)
