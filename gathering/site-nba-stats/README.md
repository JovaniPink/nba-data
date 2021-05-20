Table of Contents

1.  The Game Plan
2.  Data Acquisition
3.  Data Exploration & Processing
4.  Choosing the Right Model
5.  Testing and Results
6.  Public API

Data Sources Matter:
https://www.nba.com/stats/help/glossary/
https://www.basketball-reference.com/about/glossary.html

https://sportsdata.io/developers/data-dictionary/nba
http://popcornmachine.net/

https://www.scrapehero.com/how-to-rotate-proxies-and-ip-addresses-using-python-3/
https://www.scrapehero.com/how-to-fake-and-rotate-user-agents-using-python-3/

## Glossary

Standard:
GP Games Played
W Wins
L Losses
MIN Minutes Played
FGM Field Goals Made
FGA Field Goals Attempted
FG% Field Goal Percentage
3PM 3 Point Field Goals Made
3PA 3 Point Field Goals Attempted
3P% 3 Point Field Goals Percentage
FTM Free Throws Made
FTA Free Throws Attempted
FT% Free Throw Percentage
OREB Offensive Rebounds
DREB Defensive Rebounds
REB Rebounds
AST Assists
TOV Turnovers
STL Steals
BLK Blocks
PF Personal Fouls
FP Fantasy Points
DD2 Double doubles
TD3 Triple doubles
PTS Points
+/- Plus Minus

Advance:
GP Games Played
W Wins
L Losses
MIN Minutes Played
OffRtg Offensive Rating
DefRtg Defensive Rating
NetRtg Net Rating
AST% Assist Percentage
AST/TO Assist to Turnover Ratio
AST Ratio Assist Ratio
OREB% Offensive Rebound Percentage
DREB% Defensive Rebound Percentage
REB% Rebound Percentage
TO Ratio Turnover Ratio
eFG% Effective Field Goal Percentage
TS% True Shooting Percentage
USG% Usage Percentage
PACE Pace
PIE Player Impact Estimate

Features:
Player — Player name
Pos — Position
Age — Age of Player at the start of February 1st of that season.
Tm — Team name
G— Games Played
GS — Games Started
MP — Minutes Played over the entire season
MPG — Minutes averaged per game
FG — Field Goals Per 36 Minutes
FGA — Field Goal Attempts Per 36 Minutes
FG% — Field Goal Percentage
3P — 3-Point Field Goals Per 36 Minutes
3PA — 3-Point Field Goal Attempts Per 36 Minutes
3P% — FG% on 3-Pt FGAs.
2P — 2-Point Field Goals Per 36 Minutes
2PA — 2-Point Field Goal Attempts Per 36 Minutes
2P% — FG% on 2-Pt FGAs.
FT — Free Throws Per 36 Minutes
FTA — Free Throw Attempts Per 36 Minutes
FT% — Free Throw Percentage
ORB — Offensive Rebounds Per 36 Minutes
DRB — Defensive Rebounds Per 36 Minutes
TRB — Total Rebounds Per 36 Minutes
AST — Assists Per 36 Minutes
STL — Steals Per 36 Minutes
BLK — Blocks Per 36 Minutes
TOV — Turnovers Per 36 Minutes
A2TO — Assists to turnover ration
PF — Personal Fouls Per 36 Minutes
PTS — Points Per 36 Minutes
PER — Player Efficiency Rating- A measure of per-minute production standardized such that the league average is 15.
TS% — True Shooting Percentage- A measure of shooting efficiency that takes into account 2-point field goals, 3-point field goals, and free throws.
3PAr — 3-Point Attempt Rate- Percentage of FG Attempts from 3-Point Range
FTr — Free Throw Attempt Rate- Number of FT Attempts Per FG Attempt
ORB% — Offensive Rebound Percentage- An estimate of the percentage of available offensive rebounds a player grabbed while he was on the floor.
DRB% — Defensive Rebound Percentage- An estimate of the percentage of available defensive rebounds a player grabbed while he was on the floor.
TRB% — Total Rebound Percentage- An estimate of the percentage of available rebounds a player grabbed while he was on the floor.
AST% — Assist Percentage- An estimate of the percentage of teammate field goals a player assisted while he was on the floor.
STL% — Steal Percentage- An estimate of the percentage of opponent possessions that end with a steal by the player while he was on the floor.
BLK% — Block Percentage- An estimate of the percentage of opponent two-point field goal attempts blocked by the player while he was on the floor.
TOV% — Turnover Percentage- An estimate of turnovers committed per 100 plays.
USG% — Usage Percentage- An estimate of the percentage of team plays used by a player while he was on the floor.
OWS — Offensive Win Shares- An estimate of the number of wins contributed by a player due to his offense.
DWS — Defensive Win Shares- An estimate of the number of wins contributed by a player due to his defense.
WS — Win Shares- An estimate of the number of wins contributed by a player.
WS/48 — Win Shares Per 48 Minutes- An estimate of the number of wins contributed by a player per 48 minutes (league average is approximately .100)
OBPM — Offensive Box Plus/Minus- A box score estimate of the offensive points per 100 possessions a player contributed above a league-average player, translated to an average team.
DBPM — Defensive Box Plus/Minus- A box score estimate of the defensive points per 100 possessions a player contributed above a league-average player, translated to an average team.
BPM — Box Plus/Minus- A box score estimate of the points per 100 possessions a player contributed above a league-average player, translated to an average team.
VORP — Value over Replacement Player- A box score estimate of the points per 100 TEAM possessions that a player contributed above a replacement-level (-2.0) player, translated to an average team and prorated to an 82-game season.
Fast Break PTS — Fast break points per game
Points in Paint — Points score in the paint per game
Points off TO — Points scored after the opposing team turned over the ball
2nd chance points — Any points scored during a possession after an offensive player has already attempted one shot and missed
Points scored per shot — Calculated by dividing the total points (2P made and 3P made) by the total field goals attempt
