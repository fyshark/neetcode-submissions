class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int num: nums) {
            map.putIfAbsent(num, 0);
            map.put(num, map.get(num)+1);
        }
        List<Map.Entry<Integer, Integer>> list = 
            new ArrayList<>(map.entrySet());
        list.sort((a, b) -> Integer.compare(b.getValue(), a.getValue()));

        int[] res = new int[k];
        for (int i=0; i<k; i++) {
            res[i] = list.get(i).getKey();
        }
        return res;
    }
}
