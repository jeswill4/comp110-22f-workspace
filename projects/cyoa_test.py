"""Testing rock paper scissors."""

from projects.cyoa import achievement_tracked, winner_award, player

def test_achievements() -> None:
    winner_award() == True
    assert achievement_tracked() == print(f"\nACHIEVEMENT - {player} DOMINATION\n Win +5 times or more in a row")