from datetime import date, datetime
from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator

_NULL_STRINGS = {"-.--", ".---", "-.---", ""}


def _coerce_null(v: object) -> object:
    if isinstance(v, float) and v != v:  # pandas NaN
        return None
    if isinstance(v, str) and v.strip() in _NULL_STRINGS:
        return None
    return v


class _BasePlayerRow(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: int
    first_name: str
    last_name: str
    active: bool
    current_team: str
    position: str
    nickname: Optional[str] = None
    last_played: Optional[date] = None
    mlb_debut: Optional[date] = None
    bat_side: str
    pitch_hand: str
    type: Literal["season"]
    season: int
    age: Optional[float] = None
    gamesPlayed: Optional[int] = None
    time: datetime

    @field_validator("nickname", "last_played", "mlb_debut", mode="before")
    @classmethod
    def _nullify_optional_strs(cls, v: object) -> object:
        return _coerce_null(v)

    @field_validator("age", "gamesPlayed", mode="before")
    @classmethod
    def _nullify_shared_numerics(cls, v: object) -> object:
        return _coerce_null(v)


class DailyHittingRow(_BasePlayerRow):
    group: Literal["hitting"]

    groundOuts: Optional[int] = None
    airOuts: Optional[int] = None
    runs: Optional[int] = None
    doubles: Optional[int] = None
    triples: Optional[int] = None
    homeRuns: Optional[int] = None
    strikeOuts: Optional[int] = None
    baseOnBalls: Optional[int] = None
    intentionalWalks: Optional[int] = None
    hits: Optional[int] = None
    hitByPitch: Optional[int] = None
    avg: Optional[float] = None
    atBats: Optional[int] = None
    obp: Optional[float] = None
    slg: Optional[float] = None
    ops: Optional[float] = None
    caughtStealing: Optional[int] = None
    stolenBases: Optional[int] = None
    stolenBasePercentage: Optional[float] = None
    caughtStealingPercentage: Optional[float] = None
    groundIntoDoublePlay: Optional[int] = None
    numberOfPitches: Optional[int] = None
    plateAppearances: Optional[int] = None
    totalBases: Optional[int] = None
    rbi: Optional[int] = None
    leftOnBase: Optional[int] = None
    sacBunts: Optional[int] = None
    sacFlies: Optional[int] = None
    babip: Optional[float] = None
    groundOutsToAirouts: Optional[float] = None
    catchersInterference: Optional[int] = None
    atBatsPerHomeRun: Optional[float] = None

    @field_validator(
        "groundOuts", "airOuts", "runs", "doubles", "triples", "homeRuns",
        "strikeOuts", "baseOnBalls", "intentionalWalks", "hits", "hitByPitch",
        "atBats", "caughtStealing", "stolenBases", "groundIntoDoublePlay",
        "numberOfPitches", "plateAppearances", "totalBases", "rbi",
        "leftOnBase", "sacBunts", "sacFlies", "catchersInterference",
        mode="before",
    )
    @classmethod
    def _nullify_hitting_ints(cls, v: object) -> object:
        return _coerce_null(v)

    @field_validator(
        "avg", "obp", "slg", "ops", "babip",
        "stolenBasePercentage", "caughtStealingPercentage",
        "groundOutsToAirouts", "atBatsPerHomeRun",
        mode="before",
    )
    @classmethod
    def _nullify_hitting_floats(cls, v: object) -> object:
        return _coerce_null(v)


class DailyPitchingRow(_BasePlayerRow):
    group: Literal["pitching"]

    # opponent batting stats (what batters did against this pitcher)
    groundOuts: Optional[int] = None
    airOuts: Optional[int] = None
    runs: Optional[int] = None
    doubles: Optional[int] = None
    triples: Optional[int] = None
    homeRuns: Optional[int] = None
    strikeOuts: Optional[int] = None
    baseOnBalls: Optional[int] = None
    intentionalWalks: Optional[int] = None
    hits: Optional[int] = None
    hitByPitch: Optional[int] = None
    avg: Optional[float] = None
    atBats: Optional[int] = None
    obp: Optional[float] = None
    slg: Optional[float] = None
    ops: Optional[float] = None
    caughtStealing: Optional[int] = None
    stolenBases: Optional[int] = None
    stolenBasePercentage: Optional[float] = None
    caughtStealingPercentage: Optional[float] = None
    groundIntoDoublePlay: Optional[int] = None
    numberOfPitches: Optional[int] = None
    plateAppearances: Optional[int] = None
    totalBases: Optional[int] = None
    rbi: Optional[int] = None
    leftOnBase: Optional[int] = None
    sacBunts: Optional[int] = None
    sacFlies: Optional[int] = None
    babip: Optional[float] = None
    groundOutsToAirouts: Optional[float] = None
    catchersInterference: Optional[int] = None
    atBatsPerHomeRun: Optional[float] = None

    # pitching stats
    gamesStarted: Optional[int] = None
    era: Optional[float] = None
    # baseball thirds notation: "34.2" means 34⅔ innings, not 34.2 decimal innings
    inningsPitched: Optional[str] = None
    wins: Optional[int] = None
    losses: Optional[int] = None
    saves: Optional[int] = None
    saveOpportunities: Optional[int] = None
    holds: Optional[int] = None
    blownSaves: Optional[int] = None
    earnedRuns: Optional[int] = None
    whip: Optional[float] = None
    battersFaced: Optional[int] = None
    outs: Optional[int] = None
    gamesPitched: Optional[int] = None
    completeGames: Optional[int] = None
    shutouts: Optional[int] = None
    strikes: Optional[int] = None
    strikePercentage: Optional[float] = None
    hitBatsmen: Optional[int] = None
    balks: Optional[int] = None
    wildPitches: Optional[int] = None
    pickoffs: Optional[int] = None
    winPercentage: Optional[float] = None
    pitchesPerInning: Optional[float] = None
    gamesFinished: Optional[int] = None
    strikeoutWalkRatio: Optional[float] = None
    strikeoutsPer9Inn: Optional[float] = None
    walksPer9Inn: Optional[float] = None
    hitsPer9Inn: Optional[float] = None
    runsScoredPer9: Optional[float] = None
    homeRunsPer9: Optional[float] = None
    inheritedRunners: Optional[int] = None
    inheritedRunnersScored: Optional[int] = None

    @field_validator(
        "groundOuts", "airOuts", "runs", "doubles", "triples", "homeRuns",
        "strikeOuts", "baseOnBalls", "intentionalWalks", "hits", "hitByPitch",
        "atBats", "caughtStealing", "stolenBases", "groundIntoDoublePlay",
        "numberOfPitches", "plateAppearances", "totalBases", "rbi",
        "leftOnBase", "sacBunts", "sacFlies", "catchersInterference",
        "gamesStarted", "wins", "losses", "saves", "saveOpportunities",
        "holds", "blownSaves", "earnedRuns", "battersFaced", "outs",
        "gamesPitched", "completeGames", "shutouts", "strikes",
        "hitBatsmen", "balks", "wildPitches", "pickoffs",
        "gamesFinished", "inheritedRunners", "inheritedRunnersScored",
        mode="before",
    )
    @classmethod
    def _nullify_pitching_ints(cls, v: object) -> object:
        return _coerce_null(v)

    @field_validator(
        "avg", "obp", "slg", "ops", "babip",
        "stolenBasePercentage", "caughtStealingPercentage",
        "groundOutsToAirouts", "atBatsPerHomeRun",
        "era", "whip", "strikePercentage", "winPercentage",
        "pitchesPerInning", "strikeoutWalkRatio",
        "strikeoutsPer9Inn", "walksPer9Inn", "hitsPer9Inn",
        "runsScoredPer9", "homeRunsPer9",
        mode="before",
    )
    @classmethod
    def _nullify_pitching_floats(cls, v: object) -> object:
        return _coerce_null(v)

    @field_validator("inningsPitched", mode="before")
    @classmethod
    def _nullify_innings_pitched(cls, v: object) -> object:
        return _coerce_null(v)


class DailyStandingsRow(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str
    div_rank: int
    w: int
    l: int
    gb: Optional[float] = None          # "-" = first place
    wc_rank: Optional[int] = None       # "-" = not in wild card race
    wc_gb: Optional[str] = None         # "+2.5" format; "-" = N/A
    wc_elim_num: Optional[int] = None   # "-" = clinched or N/A
    elim_num: Optional[int] = None      # "-" = clinched or N/A
    team_id: int
    league_rank: int
    sport_rank: int
    division: str
    time: datetime

    @field_validator("gb", "wc_rank", "wc_elim_num", "elim_num", mode="before")
    @classmethod
    def _nullify_standings_numerics(cls, v: object) -> object:
        if isinstance(v, str) and v.strip() in {"-", ""}:
            return None
        return _coerce_null(v)

    @field_validator("wc_gb", mode="before")
    @classmethod
    def _nullify_wc_gb(cls, v: object) -> object:
        if isinstance(v, str) and v.strip() in {"-", ""}:
            return None
        return _coerce_null(v)


class DailyFieldingRow(_BasePlayerRow):
    group: Literal["fielding"]

    gamesStarted: Optional[int] = None
    assists: Optional[int] = None
    putOuts: Optional[int] = None
    errors: Optional[int] = None
    chances: Optional[int] = None
    fielding_pct: Optional[str] = Field(None, alias="fielding")
    position_code: Optional[int] = Field(None, alias="position.code")
    position_name: Optional[str] = Field(None, alias="position.name")
    position_type: Optional[str] = Field(None, alias="position.type")
    position_abbreviation: Optional[str] = Field(None, alias="position.abbreviation")
    rangeFactorPerGame: Optional[float] = None
    rangeFactorPer9Inn: Optional[float] = None
    # baseball thirds notation: "293.0" = 293 IP, "299.1" = 299⅓ IP
    innings: Optional[str] = None
    games: Optional[int] = None
    doublePlays: Optional[int] = None
    triplePlays: Optional[int] = None
    throwingErrors: Optional[int] = None

    @field_validator(
        "fielding_pct", "position_name", "position_type", "position_abbreviation",
        mode="before",
    )
    @classmethod
    def _nullify_fielding_strs(cls, v: object) -> object:
        return _coerce_null(v)

    @field_validator(
        "gamesStarted", "assists", "putOuts", "errors", "chances",
        "position_code", "games", "doublePlays", "triplePlays", "throwingErrors",
        mode="before",
    )
    @classmethod
    def _nullify_fielding_ints(cls, v: object) -> object:
        return _coerce_null(v)

    @field_validator(
        "rangeFactorPerGame", "rangeFactorPer9Inn",
        mode="before",
    )
    @classmethod
    def _nullify_fielding_floats(cls, v: object) -> object:
        return _coerce_null(v)

    @field_validator("innings", mode="before")
    @classmethod
    def _nullify_innings(cls, v: object) -> object:
        return _coerce_null(v)
