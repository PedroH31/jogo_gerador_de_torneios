def get_number_of_teams():
    while True:
        number_of_teams = int(input('Type the number of teams in the tournament: '))
        if number_of_teams >= 2:
            break

    return number_of_teams


def get_team_names(num_teams):
    team_names = []
    while len(team_names) < num_teams:
        team_name = input(f'Enter the name for team #{len(team_names) + 1}: ')

        if len(team_name) < 2:
            print('Team names must have at least 2 characters, try again.')

        elif team_name.count(' ') > 1:
            print('Team names may have at most 2 words, try again.')

        else:
            team_names.append(team_name)

    return team_names


def get_number_of_games_played(num_teams):
    while True:
        num_games = int(input('Enter the number of games played by each team: '))
        if num_games < num_teams - 1:
            print('Invalid number of games. Each team plays each other at least once in the regular season, try again.')

        else:
            break

    return num_games


def get_number_of_wins(team_names, games_played):
    number_of_wins = []
    for name in team_names:
        while True:
            team_wins = int(input(f'Enter the number of wins Team {name} had: '))

            if team_wins < 0:
                print('The minimum number of wins is 0, try again.')

            elif team_wins > games_played:
                print(f'The maximum number of wins is {games_played}')

            else:
                number_of_wins.append((name, team_wins))
                break

    return sorted(number_of_wins, key=lambda wins: wins[1])


num_teams = get_number_of_teams()
team_names = get_team_names(num_teams)
games_played = get_number_of_games_played(num_teams)
number_of_wins = get_number_of_wins(team_names, games_played)

print('Generating the games to be played in the first round of the tournament...')


home = 0
away = -1

for game in number_of_wins:
    home_team = number_of_wins[home][0]
    away_team = number_of_wins[away][0]

    print(f'Home: {home_team} VS Away: {away_team}')

    home += 1
    away -= 1

    if home == len(number_of_wins) // 2:
        break


