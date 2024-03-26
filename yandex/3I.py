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

players = collections.defaultdict(list)
teams = collections.defaultdict(lambda: collections.defaultdict(int))


def add_data_to_players(name: str, time, match_id):
    score = {'match_id': match_id, 'time': time}
    players[name].append(score)


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

        for i in range(score1 + score2):
            command = commands.pop()
            match = goal_pattern.match(command)
            if match:
                player_name = match.group(1)
                time = match.group(2)
                add_data_to_players(name=player_name, time=time, match_id=match_id)
                print(f"Done: {player_name} {time}")

    # match = total_goals_for_pattern.match(command)
    # if match:
    #     player_name = match.group(1)
    #     print(f"Total goals for '{player_name}'")

    # match = mean_goals_per_game_for_pattern.match(command)
    # if match:
    #     print(f"Mean goals per game for {match.group(1)}")
    #
    match = total_goals_by_pattern.match(command)
    if match:
        player_name = match.group(1)
        scores = players[player_name]
        s = set()
        for score in scores:
            s.add(score['match_id'])
        match_count = len(s)
        score_count = len(scores)
        total_goals = score_count / match_count
        print(f"Done: Total goals by {player_name} ---> {total_goals}")
    #
    # match = mean_goals_per_game_by_pattern.match(command)
    # if match:
    #     print(f"Mean goals per game by {match.group(1)}")
    #
    # match = goals_on_minute_pattern.match(command)
    # if match:
    #     print(f"Goals on minute {match.group(1)} by {match.group(2)}")
    #
    # match = goals_on_first_t_minutes_pattern.match(command)
    # if match:
    #     print(f"Goals on first {match.group(1)} minutes by {match.group(2)}")
    #
    # match = goals_on_last_t_minutes_pattern.match(command)
    # if match:
    #     print(f"Goals on last {match.group(1)} minutes by {match.group(2)}")
    #
    # match = score_opens_by_team_pattern.match(command)
    # if match:
    #     print(f"Score opens by {match.group(1)}")
    #
    # match = score_opens_by_player_pattern.match(command)
    # if match:
    #     print(f"Score opens by {match.group(1)}")

print(players)