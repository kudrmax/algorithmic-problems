# # with open('input.txt', 'r') as file:
# #     lines = file.readlines()
# # commands = []
# # for line in lines:
# #     commands.append(line.strip())
# #
# # for command in commands:
# #     print(command)
# 
#
# import re
#
# # Создаем паттерны для каждой команды
# total_goals_for_pattern = re.compile(r'Total goals for "(.*?)"')
# mean_goals_per_game_for_pattern = re.compile(r'Mean goals per game for "(.*?)"')
# total_goals_by_pattern = re.compile(r'Total goals by (.*?)')
# mean_goals_per_game_by_pattern = re.compile(r'Mean goals per game by (.*?)')
# goals_on_minute_pattern = re.compile(r'Goals on minute (\d+) by (.*?)')
# goals_on_first_t_minutes_pattern = re.compile(r'Goals on first (\d+) minutes by (.*?)')
# goals_on_last_t_minutes_pattern = re.compile(r'Goals on last (\d+) minutes by (.*?)')
# score_opens_by_team_pattern = re.compile(r'Score opens by "(.*?)"')
# score_opens_by_player_pattern = re.compile(r'Score opens by (.*?)')
#
# with open('input.txt', 'r') as file:
#     lines = file.readlines()
#
# for line in lines[1:]:
#     # Проверяем каждую строку на соответствие шаблонам с помощью регулярных выражений
#     match = total_goals_for_pattern.match(line)
#     if match:
#         print(f"Total goals for {match.group(1)}")
#
#     match = mean_goals_per_game_for_pattern.match(line)
#     if match:
#         print(f"Mean goals per game for {match.group(1)}")
#
#     match = total_goals_by_pattern.match(line)
#     if match:
#         print(f"Total goals by {match.group(1)}")
#
#     match = mean_goals_per_game_by_pattern.match(line)
#     if match:
#         print(f"Mean goals per game by {match.group(1)}")
#
#     match = goals_on_minute_pattern.match(line)
#     if match:
#         print(f"Goals on minute {match.group(1)} by {match.group(2)}")
#
#     match = goals_on_first_t_minutes_pattern.match(line)
#     if match:
#         print(f"Goals on first {match.group(1)} minutes by {match.group(2)}")
#
#     match = goals_on_last_t_minutes_pattern.match(line)
#     if match:
#         print(f"Goals on last {match.group(1)} minutes by {match.group(2)}")
#
#     match = score_opens_by_team_pattern.match(line)
#     if match:
#         print(f"Score opens by {match.group(1)}")
#
#     match = score_opens_by_player_pattern.match(line)
#     if match:
#         print(f"Score opens by {match.group(1)}")
