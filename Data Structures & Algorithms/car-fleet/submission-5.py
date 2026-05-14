class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        fleets = 0
        currTime = 0
        for pos, spd in pairs:
            time = (target - pos)/spd

            if time > currTime:
                currTime = time
                fleets += 1
        
        return fleets