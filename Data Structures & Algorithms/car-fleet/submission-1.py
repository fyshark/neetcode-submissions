class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        curTime = 0
        pairs = sorted(zip(position, speed), reverse=True)

        for pos, spd in pairs:
            time = (target - pos)/spd
            if time > curTime:
                curTime = time
                fleets += 1
            
        return fleets