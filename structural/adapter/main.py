from peg import RoundHole, RoundPeg, SquarePeg, SquarePegAdapter

if __name__ == "__main__":
    round_hole = RoundHole(radius=5)
    round_peg = RoundPeg(radius=4)
    square_peg = SquarePeg(width=8)
    square_peg_adapter = SquarePegAdapter(square_peg=square_peg)

    print(round_hole.fits(peg=round_peg))
    print(round_hole.fits(peg=square_peg_adapter))
