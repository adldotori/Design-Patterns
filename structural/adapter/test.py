from peg import RoundHole, RoundPeg, SquarePeg, SquarePegAdapter


class Test(object):
    def test_small(self):
        round_hole = RoundHole(radius=5)
        round_peg = RoundPeg(radius=4)
        square_peg = SquarePeg(width=4)
        square_peg_adapter = SquarePegAdapter(square_peg=square_peg)

        assert round_hole.fits(peg=round_peg) == True
        assert round_hole.fits(peg=square_peg_adapter) == True

    def test_large(self):
        round_hole = RoundHole(radius=5)
        round_peg = RoundPeg(radius=4)
        square_peg = SquarePeg(width=8)
        square_peg_adapter = SquarePegAdapter(square_peg=square_peg)

        assert round_hole.fits(peg=round_peg) == True
        assert round_hole.fits(peg=square_peg_adapter) == False
