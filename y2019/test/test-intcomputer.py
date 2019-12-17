# type: ignore
import y2019.IntComputer as IC

class TestIntComputer:
    def test_day2(self):
        cp = IC.IntComputer([1,0,0,0,99])
        cp.run()
        assert cp.program == [2,0,0,0,99]

        cp = IC.IntComputer([2,3,0,3,99])
        cp.run()
        assert cp.program == [2,3,0,6,99]

        cp = IC.IntComputer([2,4,4,5,99,0])
        cp.run()
        assert cp.program == [2,4,4,5,99,9801]

        cp = IC.IntComputer([1,1,1,4,99,5,6,0,99])
        cp.run()
        assert cp.program == [30,1,1,4,2,5,6,0,99]
