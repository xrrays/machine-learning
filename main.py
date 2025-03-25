import json
import pandas as pd

# load config
with open("config.json") as f:
    config = json.load(f)

# load datasets
steam_path = config["steam_reviews_path"]
games_path = config["all_games_path"]

steam_df = pd.read_csv(steam_path, nrows=5)
games_df = pd.read_csv(games_path, nrows=5)

print("steam reviews sample:\n", steam_df.head())
print("all games sample:\n", games_df.head())