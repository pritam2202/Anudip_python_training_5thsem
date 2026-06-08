# ==========================================
# CRICKET TOURNAMENT ANALYTICS SYSTEM
# ==========================================

# 30 PLAYER RECORDS
players = {
    "Virat": {"runs": 645, "matches": 12, "wickets": 0},
    "Rohit": {"runs": 520, "matches": 10, "wickets": 1},
    "Dhoni": {"runs": 300, "matches": 15, "wickets": 0},
    "Bumrah": {"runs": 50, "matches": 20, "wickets": 25},
    "Shami": {"runs": 80, "matches": 18, "wickets": 30},
    "Hardik": {"runs": 400, "matches": 12, "wickets": 15},
    "Jadeja": {"runs": 350, "matches": 14, "wickets": 20},
    "Rahul": {"runs": 410, "matches": 11, "wickets": 2},
    "Gill": {"runs": 380, "matches": 9, "wickets": 0},
    "Pant": {"runs": 290, "matches": 8, "wickets": 0},
    "Iyer": {"runs": 310, "matches": 10, "wickets": 1},
    "Ashwin": {"runs": 120, "matches": 16, "wickets": 40},
    "Siraj": {"runs": 60, "matches": 17, "wickets": 22},
    "Kohli2": {"runs": 500, "matches": 13, "wickets": 0},
    "Player15": {"runs": 200, "matches": 10, "wickets": 3},
    "Player16": {"runs": 260, "matches": 11, "wickets": 6},
    "Player17": {"runs": 275, "matches": 9, "wickets": 8},
    "Player18": {"runs": 180, "matches": 7, "wickets": 10},
    "Player19": {"runs": 90, "matches": 5, "wickets": 12},
    "Player20": {"runs": 600, "matches": 12, "wickets": 0},
    "Player21": {"runs": 450, "matches": 13, "wickets": 2},
    "Player22": {"runs": 330, "matches": 11, "wickets": 5},
    "Player23": {"runs": 220, "matches": 8, "wickets": 7},
    "Player24": {"runs": 140, "matches": 6, "wickets": 9},
    "Player25": {"runs": 370, "matches": 10, "wickets": 11},
    "Player26": {"runs": 410, "matches": 12, "wickets": 13},
    "Player27": {"runs": 295, "matches": 9, "wickets": 14},
    "Player28": {"runs": 260, "matches": 8, "wickets": 16},
    "Player29": {"runs": 310, "matches": 10, "wickets": 18},
    "Player30": {"runs": 480, "matches": 14, "wickets": 20}
}

# ------------------------------------------
# 1. DISPLAY ALL PLAYERS
# ------------------------------------------
def display_players():
    print("\n--- PLAYER STATISTICS ---")
    for p in players:
        print(p, players[p])

# ------------------------------------------
# 2. HIGHEST RUN SCORER
# ------------------------------------------
def highest_runs():
    top = None
    for p in players:
        if top is None or players[p]["runs"] > players[top]["runs"]:
            top = p
    print("Highest Run Scorer:", top, players[top])

# ------------------------------------------
# 3. LOWEST RUN SCORER
# ------------------------------------------
def lowest_runs():
    low = None
    for p in players:
        if low is None or players[p]["runs"] < players[low]["runs"]:
            low = p
    print("Lowest Run Scorer:", low, players[low])

# ------------------------------------------
# 4. AVERAGE RUNS
# ------------------------------------------
def average_runs():
    total = 0
    for p in players:
        total += players[p]["runs"]
    avg = total / len(players)
    print("Average Runs:", avg)
    return avg

# ------------------------------------------
# 5. MAX WICKET PLAYER
# ------------------------------------------
def max_wickets():
    top = None
    for p in players:
        if top is None or players[p]["wickets"] > players[top]["wickets"]:
            top = p
    print("Max Wicket Taker:", top, players[top])

# ------------------------------------------
# 6. ALL ROUNDERS
# ------------------------------------------
def all_rounders():
    print("\nAll Rounders:")
    for p in players:
        if players[p]["runs"] > 300 and players[p]["wickets"] > 5:
            print(p, players[p])

# ------------------------------------------
# 7. ABOVE AVERAGE RUNS
# ------------------------------------------
def above_average():
    avg = average_runs()
    print("\nAbove Average Players:")
    for p in players:
        if players[p]["runs"] > avg:
            print(p, players[p])

# ------------------------------------------
# 8. PLAYER CATEGORIES
# ------------------------------------------
def categories():
    print("\n--- PLAYER CATEGORIES ---")

    for p in players:
        r = players[p]["runs"]

        if r >= 500:
            print(p, "Star Performer")
        elif r >= 350:
            print(p, "Good Performer")
        elif r >= 200:
            print(p, "Average Performer")
        else:
            print(p, "Poor Performer")

# ------------------------------------------
# 9. TEAM STATISTICS
# ------------------------------------------
def team_stats():
    total_runs = 0
    total_wickets = 0

    for p in players:
        total_runs += players[p]["runs"]
        total_wickets += players[p]["wickets"]

    print("Total Runs:", total_runs)
    print("Total Wickets:", total_wickets)

# ------------------------------------------
# 10. TOP 5 BATSMEN
# ------------------------------------------
def top5_batsmen():
    temp = players.copy()
    print("\nTop 5 Batsmen:")

    for _ in range(5):
        top = None
        for p in temp:
            if top is None or temp[p]["runs"] > temp[top]["runs"]:
                top = p
        print(top, temp[top])
        del temp[top]

# ------------------------------------------
# 11. TOP 5 BOWLERS
# ------------------------------------------
def top5_bowlers():
    temp = players.copy()
    print("\nTop 5 Bowlers:")

    for _ in range(5):
        top = None
        for p in temp:
            if top is None or temp[p]["wickets"] > temp[top]["wickets"]:
                top = p
        print(top, temp[top])
        del temp[top]

# ------------------------------------------
# 12. AWARD WINNERS
# ------------------------------------------
def award_winners():
    awards = {}

    for p in players:
        if players[p]["runs"] > 500 or players[p]["wickets"] > 25:
            awards[p] = players[p]

    print("\nAward Winners:")
    for p in awards:
        print(p, awards[p])

# ------------------------------------------
# MENU
# ------------------------------------------
while True:
    print("\n===== CRICKET MENU =====")
    print("1. Display Players")
    print("2. Highest Runs")
    print("3. Lowest Runs")
    print("4. Average Runs")
    print("5. Max Wickets")
    print("6. All Rounders")
    print("7. Above Average")
    print("8. Categories")
    print("9. Team Stats")
    print("10. Top 5 Batsmen")
    print("11. Top 5 Bowlers")
    print("12. Award Winners")
    print("13. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        display_players()
    elif ch == 2:
        highest_runs()
    elif ch == 3:
        lowest_runs()
    elif ch == 4:
        average_runs()
    elif ch == 5:
        max_wickets()
    elif ch == 6:
        all_rounders()
    elif ch == 7:
        above_average()
    elif ch == 8:
        categories()
    elif ch == 9:
        team_stats()
    elif ch == 10:
        top5_batsmen()
    elif ch == 11:
        top5_bowlers()
    elif ch == 12:
        award_winners()
    elif ch == 13:
        print("Tournament Ended")
        break
    else:
        print("Invalid Choice")
