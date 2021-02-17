nba_stats_columns = [
    "PLAYER_ID",
    "PLAYER_NAME",  # "Player": "player_name"
    "TEAM_ID",
    "TEAM_ABBREVIATION", # "Tm": "team_abbreviation"
    "AGE",  # "Age": "age"
    "GP",  # "G": "gp"
    "W",
    "L",
    "W_PCT",
    "MIN",  # "MP": "min"
    "FGM",  # "FG": "fgm"
    "FGA",  # "FGA": "fga"
    "FG_PCT",  # "FG%": "fg_pct"
    "FG3M",  # "3P": "fg3m"
    "FG3A",  # "3PA": "fg3a"
    "FG3_PCT",  # "3P%": "fg3_pct"
    "FTM",  # "FT": "ftm"
    "FTA",  # "FTA": "fta"
    "FT_PCT",  # "FT%": "ft_pct"
    "OREB",  # "ORB": "oreb"
    "DREB",  # "DRB": "dreb"
    "REB",  # "TRB": "reb"
    "AST",  # "AST": "ast"
    "TOV",  # "TOV": "tov"
    "STL",  # "STL": "stl"
    "BLK",  # "BLK": "blk"
    "BLKA",
    "PF",  # "PF": "pf"
    "PFD",
    "PTS",  # "PTS": "pts"
    "PLUS_MINUS",
    "NBA_FANTASY_PTS",
    "DD2",
    "TD3",
    "GP_RANK",
    "W_RANK",
    "L_RANK",
    "W_PCT_RANK",
    "MIN_RANK",
    "FGM_RANK",
    "FGA_RANK",
    "FG_PCT_RANK",
    "FG3M_RANK",
    "FG3A_RANK",
    "FG3_PCT_RANK",
    "FTM_RANK",
    "FTA_RANK",
    "FT_PCT_RANK",
    "OREB_RANK",
    "DREB_RANK",
    "REB_RANK",
    "AST_RANK",
    "TOV_RANK",
    "STL_RANK",
    "BLK_RANK",
    "BLKA_RANK",
    "PF_RANK",
    "PFD_RANK",
    "PTS_RANK",
    "PLUS_MINUS_RANK",
    "NBA_FANTASY_PTS_RANK",
    "DD2_RANK",
    "TD3_RANK",
    "CFID",
    "CFPARAMS",
]

basketball_reference_columns = [
    "Player",
    "Pos",
    "Age",
    "Tm",
    "G",
    "GS",
    "MP",
    "FG",
    "FGA",
    "FG%",
    "3P",
    "3PA",
    "3P%",
    "2P",
    "2PA",
    "2P%",
    "eFG%",
    "FT",
    "FTA",
    "FT%",
    "ORB",
    "DRB",
    "TRB",
    "AST",
    "STL",
    "BLK",
    "TOV",
    "PF",
    "PTS",
]

rename_these_columns = {
    "Player": "player_name",
    "Tm": "team_abbreviation",
    "Age": "age",
    "G": "gp",
    "MP": "min",
    "FG": "fgm",
    "FGA": "fga",
    "FG%": "fg_pct",
    "3P": "fg3m",
    "3PA": "fg3a",
    "3P%": "fg3_pct",
    "FT": "ftm",
    "FTA": "fta",
    "FT%": "ft_pct",
    "ORB": "oreb",
    "DRB": "dreb",
    "TRB": "reb",
    "AST": "ast",
    "TOV": "tov",
    "STL": "stl",
    "BLK": "blk",
    "PF": "pf",
    "PTS": "pts",
}


drop_these_columns = [
    "Player",
    "Tm",
    "Age",
    "G",
    "MP",
    "FG",
    "FGA",
    "FG%",
    "3P",
    "3PA",
    "3P%",
    "FT",
    "FTA",
    "FT%",
    "ORB",
    "DRB",
    "TRB",
    "AST",
    "TOV",
    "STL",
    "BLK",
    "PF",
    "PTS",
]

drop_these_columns_refactored = [
    "player_name",
    "team_abbreviation",
    "age",
    "gp",
    "min",
    "fgm",
    "fga",
    "fg_pct",
    "fg3m",
    "fg3a",
    "fg3_pct",
    "ftm",
    "fta",
    "ft_pct",
    "oreb",
    "dreb",
    "reb",
    "ast",
    "tov",
    "stl",
    "blk",
    "pf",
    "pts",
]

# Converts a basketball reference season to a season recognized by stats.nba.com (2019 -> 2018-19)
def convert_bbref_season_to_nba_season(season):
    year = int(season)
    last_year = year - 1
    last_two = season[-2:]
    return "{0}-{1}".format(last_year, last_two)
