# Creating a stats table for the stats we are wanting to work with.

from sqlalchemy import create_engine, Column, Integer, Float, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
import uuid

Base = declarative_base()

# the user model specifies its fields (or columns) declaratively
class PlayerGeneralTraditionalStats(Base):
    # https://www.nba.com/stats/players/traditional/?sort=PTS&dir=-1

    __tablename__ = "player_general_traditional_totals"

    stat_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    season_id = Column(String, primary_key=True)
    player_id = Column(Integer, primary_key=True)
    player_name = Column(String)
    team_id = Column(Integer)
    team_abbreviation = Column(String)
    age = Column(Integer)
    gp = Column(Integer)
    w = Column(Integer)
    l = Column(Integer)
    w_pct = Column(Float)
    min = Column(Float)
    fgm = Column(Float)
    fga = Column(Float)
    fg_pct = Column(Float)
    fg3m = Column(Float)
    fg3a = Column(Float)
    fg3_pct = Column(Float)
    ftm = Column(Float)
    fta = Column(Float)
    ft_pct = Column(Float)
    oreb = Column(Float)
    dreb = Column(Float)
    reb = Column(Float)
    ast = Column(Float)
    tov = Column(Float)
    stl = Column(Float)
    blk = Column(Float)
    blka = Column(Float)
    pf = Column(Float)
    pfd = Column(Float)
    pts = Column(Float)
    plus_minus = Column(Float)
    nba_fantasy_points = Column(Float)
    dd2 = Column(Float)
    td3 = Column(Float)
    gp_rank = Column(Integer)
    w_rank = Column(Integer)
    l_rank = Column(Integer)
    w_pct_rank = Column(Integer)
    min_rank = Column(Integer)
    fgm_rank = Column(Integer)
    fga_rank = Column(Integer)
    fg_pct_rank = Column(Integer)
    fg3m_rank = Column(Integer)
    fg3a_rank = Column(Integer)
    fg3_pct_rank = Column(Integer)
    ftm_rank = Column(Integer)
    fta_rank = Column(Integer)
    ft_pct_rank = Column(Integer)
    oreb_rank = Column(Integer)
    dreb_rank = Column(Integer)
    reb_rank = Column(Integer)
    ast_rank = Column(Integer)
    tov_rank = Column(Integer)
    stl_rank = Column(Integer)
    blk_rank = Column(Integer)
    blka_rank = Column(Integer)
    pf_rank = Column(Integer)
    pfd_rank = Column(Integer)
    pts_rank = Column(Integer)
    plus_minus_rank = Column(Integer)
    nba_fantasy_points_rank = Column(Integer)
    dd2_rank = Column(Integer)
    td3_rank = Column(Integer)
    cfid = Column(Integer)
    cfparams = Column(String)


class PlayerGeneralAdvancedTotals(Base):
    # https://www.nba.com/stats/players/advanced/?sort=GP&dir=-1

    __tablename__ = "player_general_advanced_totals"

    stat_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    season_id = Column(String, primary_key=True)
    player_id = Column(Integer, primary_key=True)
    player_name = Column(String)
    team_id = Column(Integer)
    team_abbreviation = Column(String)
    age = Column(Integer)
    gp = Column(Integer)
    w = Column(Integer)
    l = Column(Integer)
    w_pct = Column(Float)
    min = Column(Float)
    off_rating = Column(Float)
    def_rating = Column(Float)
    net_rating = Column(Float)
    ast_pct = Column(Float)
    ast_to = Column(Float)
    ast_ratio = Column(Float)
    oreb_pct = Column(Float)
    dreb_pct = Column(Float)
    reb_pct = Column(Float)
    tm_tov_pct = Column(Float)
    efg_pct = Column(Float)
    ts_pct = Column(Float)
    usg_pct = Column(Float)
    pace = Column(Float)
    pie = Column(Float)
    fgm = Column(Float)
    fga = Column(Float)
    fgm_pg = Column(Float)
    fga_pg = Column(Float)
    fg_pct = Column(Float)
    gp_rank = Column(Integer)
    w_rank = Column(Integer)
    l_rank = Column(Integer)
    w_pct_rank = Column(Integer)
    min_rank = Column(Integer)
    off_rating_rank = Column(Integer)
    def_rating_rank = Column(Integer)
    net_rating_rank = Column(Integer)
    ast_pct_rank = Column(Integer)
    ast_to_rank = Column(Integer)
    ast_ratio_rank = Column(Integer)
    oreb_pct_rank = Column(Integer)
    dreb_pct_rank = Column(Integer)
    reb_pct_rank = Column(Integer)
    tm_tov_pct_rank = Column(Integer)
    efg_pct_rank = Column(Integer)
    ts_pct_rank = Column(Integer)
    usg_pct_rank = Column(Integer)
    pace_rank = Column(Integer)
    pie_rank = Column(Integer)
    fgm_rank = Column(Integer)
    fga_rank = Column(Integer)
    fgm_pg_rank = Column(Integer)
    fga_pg_rank = Column(Integer)
    fg_pct_rank = Column(Integer)
    cfid = Column(Integer)
    cfparams = Column(String)


class PlayerBios(Base):
    # ?

    __tablename__ = "player_bios"

    stat_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    season_id = Column(String, primary_key=True)
    player_id = Column(Integer, primary_key=True)
    player_name = Column(String)
    team_id = Column(Integer)
    team_abbreviation = Column(String)
    age = Column(Integer)
    player_height = Column(String)
    player_height_inches = Column(Integer)
    player_weight = Column(String)
    college = Column(String)
    country = Column(String)
    draft_year = Column(String)
    draft_round = Column(String)
    draft_number = Column(String)
    gp = Column(Integer)
    pts = Column(Float)
    reb = Column(Float)
    ast = Column(Float)
    net_rating = Column(Float)
    oreb_pct = Column(Float)
    dreb_pct = Column(Float)
    usg_pct = Column(Float)
    ts_pct = Column(Float)
    ast_pct = Column(Float)


class PlayerGameLogs(Base):
    # https://www.nba.com/stats/players/boxscores/

    __tablename__ = "player_game_logs"

    stat_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    season_id = Column(String, primary_key=True)
    player_id = Column(Integer, primary_key=True)
    player_name = Column(String)
    team_id = Column(Integer)
    team_abbreviation = Column(String)
    team_name = Column(String)
    game_id = Column(String)
    game_date = Column(String)
    matchup = Column(String)
    wl = Column(String)
    min = Column(Float)
    fgm = Column(Float)
    fga = Column(Float)
    fg_pct = Column(Float)
    fg3m = Column(Float)
    fg3a = Column(Float)
    fg3_pct = Column(Float)
    ftm = Column(Float)
    fta = Column(Float)
    ft_pct = Column(Float)
    oreb = Column(Float)
    dreb = Column(Float)
    reb = Column(Float)
    ast = Column(Float)
    stl = Column(Float)
    blk = Column(Float)
    tov = Column(Float)
    pf = Column(Float)
    pts = Column(Float)
    plus_minus = Column(Float)
    video_available = Column(Integer)


class TeamGameLogs(Base):
    # https://www.nba.com/stats/teams/boxscores/

    __tablename__ = "team_game_logs"

    stat_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    season_id = Column(String, primary_key=True)
    team_id = Column(Integer)
    team_abbreviation = Column(String)
    team_name = Column(String)
    game_id = Column(String)
    game_date = Column(String)
    matchup = Column(String)
    wl = Column(String)
    min = Column(Float)
    fgm = Column(Float)
    fga = Column(Float)
    fg_pct = Column(Float)
    fg3m = Column(Float)
    fg3a = Column(Float)
    fg3_pct = Column(Float)
    ftm = Column(Float)
    fta = Column(Float)
    ft_pct = Column(Float)
    oreb = Column(Float)
    dreb = Column(Float)
    reb = Column(Float)
    ast = Column(Float)
    stl = Column(Float)
    blk = Column(Float)
    tov = Column(Float)
    pf = Column(Float)
    pts = Column(Float)
    plus_minus = Column(Float)
    video_available = Column(Integer)


class TeamGeneralTraditionalStats(Base):
    # https://www.nba.com/stats/teams/traditional/?sort=W_PCT&dir=-1

    __tablename__ = "team_general_traditional_stats"

    stat_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    season_id = Column(String, primary_key=True)
    team_id = Column(Integer)
    team_name = Column(String)
    gp = Column(Integer)
    w = Column(Integer)
    l = Column(Integer)
    w_pct = Column(Float)
    min = Column(Float)
    fgm = Column(Float)
    fga = Column(Float)
    fg_pct = Column(Float)
    fg3m = Column(Float)
    fg3a = Column(Float)
    fg3_pct = Column(Float)
    ftm = Column(Float)
    fta = Column(Float)
    ft_pct = Column(Float)
    oreb = Column(Float)
    dreb = Column(Float)
    reb = Column(Float)
    ast = Column(Float)
    tov = Column(Float)
    stl = Column(Float)
    blk = Column(Float)
    blka = Column(Float)
    pf = Column(Float)
    pfd = Column(Float)
    pts = Column(Float)
    plus_minus = Column(Float)
    gp_rank = Column(Integer)
    w_rank = Column(Integer)
    l_rank = Column(Integer)
    w_pct_rank = Column(Integer)
    min_rank = Column(Integer)
    fgm_rank = Column(Integer)
    fga_rank = Column(Integer)
    fg_pct_rank = Column(Integer)
    fg3m_rank = Column(Integer)
    fg3a_rank = Column(Integer)
    fg3_pct_rank = Column(Integer)
    ftm_rank = Column(Integer)
    fta_rank = Column(Integer)
    ft_pct_rank = Column(Integer)
    oreb_rank = Column(Integer)
    dreb_rank = Column(Integer)
    reb_rank = Column(Integer)
    ast_rank = Column(Integer)
    tov_rank = Column(Integer)
    stl_rank = Column(Integer)
    blk_rank = Column(Integer)
    blka_rank = Column(Integer)
    pf_rank = Column(Integer)
    pfd_rank = Column(Integer)
    pts_rank = Column(Integer)
    plus_minus_rank = Column(Integer)
    cfid = Column(Integer)
    cfparams = Column(String)


class TeamGeneralAdvancedStats(Base):
    # https://www.nba.com/stats/teams/advanced/?sort=W&dir=-1

    __tablename__ = "team_general_advanced_stats"

    stat_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    team_id = Column(Integer)
    team_name = Column(String)
    gp = Column(Integer)
    w = Column(Integer)
    l = Column(Integer)
    w_pct = Column(Float)
    min = Column(Float)
    e_off_rating = Column(Float)
    off_rating = Column(Float)
    e_def_rating = Column(Float)
    def_rating = Column(Float)
    e_net_rating = Column(Float)
    net_rating = Column(Float)
    ast_pct = Column(Float)
    ast_to = Column(Float)
    ast_ratio = Column(Float)
    oreb_pct = Column(Float)
    dreb_pct = Column(Float)
    reb_pct = Column(Float)
    tm_tov_pct = Column(Float)
    efg_pct = Column(Float)
    ts_pct = Column(Float)
    e_pace = Column(Float)
    pace = Column(Float)
    pace_per40 = Column(Float)
    poss = Column(Float)
    pie = Column(Float)
    gp_rank = Column(Integer)
    w_rank = Column(Integer)
    l_rank = Column(Integer)
    w_pct_rank = Column(Integer)
    min_rank = Column(Integer)
    off_rating_rank = Column(Integer)
    def_rating_rank = Column(Integer)
    net_rating_rank = Column(Integer)
    ast_pct_rank = Column(Integer)
    ast_to_rank = Column(Integer)
    ast_ratio_rank = Column(Integer)
    oreb_pct_rank = Column(Integer)
    dreb_pct_rank = Column(Integer)
    reb_pct_rank = Column(Integer)
    tm_tov_pct_rank = Column(Integer)
    efg_pct_rank = Column(Integer)
    ts_pct_rank = Column(Integer)
    pace_rank = Column(Integer)
    pie_rank = Column(Integer)
    cfid = Column(Integer)
    cfparams = Column(String)


class PlayersByTeam(Base):
    # ?

    __tablename__ = "players_by_team"

    stat_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    group_set = Column(String)
    team_id = Column(Integer)
    team_name = Column(String)
    group_value = Column(String)
    gp = Column(Integer)
    w = Column(Integer)
    l = Column(Integer)
    w_pct = Column(Float)
    min = Column(Float)
    fgm = Column(Float)
    fga = Column(Float)
    fg_pct = Column(Float)
    fg3m = Column(Float)
    fg3a = Column(Float)
    fg3_pct = Column(Float)
    ftm = Column(Float)
    fta = Column(Float)
    ft_pct = Column(Float)
    oreb = Column(Float)
    dreb = Column(Float)
    reb = Column(Float)
    ast = Column(Float)
    stl = Column(Float)
    blk = Column(Float)
    blka = Column(Float)
    pf = Column(Float)
    pfd = Column(Float)
    pts = Column(Float)
    plus_minus = Column(Float)
    gp_rank = Column(Integer)
    w_rank = Column(Integer)
    l_rank = Column(Integer)
    w_pct_rank = Column(Integer)
    min_rank = Column(Integer)
    fgm_rank = Column(Integer)
    fga_rank = Column(Integer)
    fg_pct_rank = Column(Integer)
    fg3m_rank = Column(Integer)
    fg3a_rank = Column(Integer)
    fg3_pct_rank = Column(Integer)
    ftm_rank = Column(Integer)
    fta_rank = Column(Integer)
    ft_pct_rank = Column(Integer)
    oreb_rank = Column(Integer)
    dreb_rank = Column(Integer)
    reb_rank = Column(Integer)
    ast_rank = Column(Integer)
    tov_rank = Column(Integer)
    stl_rank = Column(Integer)
    blk_rank = Column(Integer)
    blka_rank = Column(Integer)
    pf_rank = Column(Integer)
    pfd_rank = Column(Integer)
    pts_rank = Column(Integer)
    plus_minus_rank = Column(Integer)

class PlayerAbbr(Base):
    # ?

    __tablename__ = "player_abbr"

    stat_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    team_id = Column(Integer)
    season_year = Column(String)
    team_city = Column(String)
    team_name = Column(String)
    team_abbreviation = Column(String)
    team_conference = Column(String)
    team_division = Column(String)
    team_code = Column(String)
    team_slug = Column(String)
    w = Column(Integer)
    l = Column(Integer)
    pct = Column(Float)
    conf_rank = Column(Integer)
    div_rank = Column(Integer)
    min_year = Column(String)
    max_year = Column(String)


    
class TeamAbbr(Base):
    # ?

    __tablename__ = "team_abbr"

    stat_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    team_id = Column(Integer)
    season_year = Column(String)
    team_city = Column(String)
    team_name = Column(String)
    team_abbreviation = Column(String)
    team_conference = Column(String)
    team_division = Column(String)
    team_code = Column(String)
    team_slug = Column(String)
    w = Column(Integer)
    l = Column(Integer)
    pct = Column(Float)
    conf_rank = Column(Integer)
    div_rank = Column(Integer)
    min_year = Column(String)
    max_year = Column(String)

class Shots(Base):
    # ?

    __tablename__ = "shots"

    stat_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    player_id = Column(Integer, primary_key=True)
    display_name  = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    roster_status = Column(Integer)
    from_year = Column(Integer)
    to_year = Column(Integer)
    player_code = Column(String)
    team_id = Column(Integer)
    team_city  = Column(String)
    team_name  = Column(String)
    team_abbreviation  = Column(String)
    team_code  = Column(String)
    games_played_flag  = Column(String)
    other_league_experience_ch  = Column(String)
    