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

class Data():
    def __init__(self):
        self.team1 = ''
        self.team2 = ''
        self.score1 = 0
        self.score2 = 0
        self.scores1 = []
        self.scores2 = []

        self.score1_remain = 0
        self.score2_remain = 0

    def clear(self):
        self.team1 = ''
        self.team2 = ''
        self.score1 = 0
        self.score2 = 0
        self.scores1.clear()
        self.scores2.clear()

data = Data()

for command in commands:

    match = match_score_pattern.match(command)
    if match:
        data.team1 = match.group(1)
        data.team2 = match.group(2)
        data.score1 = int(match.group(3))
        data.score2 = int(match.group(4))
        data.score1_remain = data.score1
        data.score2_remain = data.score2
        print(f"{data.team1} - {data.team2} {data.score1}:{data.score2}")

    match = goal_pattern.match(command)
    if match:
        if data.score1_remain > 0:
            data.scores1.append({
                'name': match.group(1),
                'score': int(match.group(2))
            })
            data.score1_remain -= 1
        else:
            pass
        print(f"{match.group(1)} {match.group(2)}")

    match = total_goals_for_pattern.match(command)
    if match:
        print(f"Total goals for '{match.group(1)}'")

    match = mean_goals_per_game_for_pattern.match(command)
    if match:
        print(f"Mean goals per game for {match.group(1)}")

    match = total_goals_by_pattern.match(command)
    if match:
        print(f"Total goals by {match.group(1)}")

    match = mean_goals_per_game_by_pattern.match(command)
    if match:
        print(f"Mean goals per game by {match.group(1)}")

    match = goals_on_minute_pattern.match(command)
    if match:
        print(f"Goals on minute {match.group(1)} by {match.group(2)}")

    match = goals_on_first_t_minutes_pattern.match(command)
    if match:
        print(f"Goals on first {match.group(1)} minutes by {match.group(2)}")

    match = goals_on_last_t_minutes_pattern.match(command)
    if match:
        print(f"Goals on last {match.group(1)} minutes by {match.group(2)}")

    match = score_opens_by_team_pattern.match(command)
    if match:
        print(f"Score opens by {match.group(1)}")

    match = score_opens_by_player_pattern.match(command)
    if match:
        print(f"Score opens by {match.group(1)}")
