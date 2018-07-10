import unittest
from lifegame import LifeGame


class LifeGameTest(unittest.TestCase):
    def test_lifeGame(self):
        # 初期状態生成
        lg = LifeGame(4, 4)
        for p in [[0, 1], [0, 3], [1, 2], [2, 0], [2, 1], [3, 2], [3, 3]]:
            lg.set_alive(p[0], p[1])
        assert lg.board == [
            [0, 1, 0, 1],
            [0, 0, 1, 0],
            [1, 1, 0, 0],
            [0, 0, 1, 1]
        ], "初期生成エラー"
        # １世代進めて結果をテスト
        lg.next_generation()
        assert lg.board == [
            [1, 1, 0, 1],
            [0, 0, 1, 1],
            [1, 1, 0, 0],
            [0, 0, 0, 1]
        ], "世代1エラー"
        # もう１世代進めて結果をテスト
        lg.next_generation()
        assert lg.board == [
            [0, 1, 0, 0],
            [0, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 0, 1]
        ], "世代2エラー"


if __name__ == "__main__":
    unittest.main()
