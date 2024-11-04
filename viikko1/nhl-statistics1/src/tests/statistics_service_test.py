import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

#Only minimum tests to achieve 100% branch coverage
class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())
    
    def test_search_finds_player(self):
        self.assertEqual(self.stats.search("Semenko"), self.stats._players[0])
    
    def test_search_for_nonexistent_player(self):
        self.assertEqual(self.stats.search("nonexistentplayer"), None)
    
    def test_team_search_works(self):
        team = self.stats.team("EDM")

        self.assertEqual(team[0], self.stats._players[0])
        self.assertEqual(team[1], self.stats._players[2])
        self.assertEqual(team[2], self.stats._players[4])
    
    def test_top_three_points(self):
        top_three = self.stats.top(3)

        self.assertEqual(top_three[0], self.stats._players[4])
        self.assertEqual(top_three[1], self.stats._players[1])
        self.assertEqual(top_three[2], self.stats._players[3])
    
    def test_top_three_by_goals(self):
        top_three = self.stats.top(3, SortBy.GOALS)

        self.assertEqual(top_three[0], self.stats._players[1])
        self.assertEqual(top_three[1], self.stats._players[3])
        self.assertEqual(top_three[2], self.stats._players[2])
    
    def test_top_three_by_assists(self):
        top_three = self.stats.top(3, SortBy.ASSISTS)

        self.assertEqual(top_three[0], self.stats._players[4])
        self.assertEqual(top_three[1], self.stats._players[3])
        self.assertEqual(top_three[2], self.stats._players[1])
    
    def test_top_three_by_else(self):
        top_three = self.stats.top(3, "improper value")

        self.assertEqual(top_three[0], self.stats._players[4])
        self.assertEqual(top_three[1], self.stats._players[1])
        self.assertEqual(top_three[2], self.stats._players[3])

        