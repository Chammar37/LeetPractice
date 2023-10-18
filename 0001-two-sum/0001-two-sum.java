class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        int[] ans = new int[2];
        HashMap <Integer, Integer> hp = new HashMap<>();
        
        //First make dictionary, put all elements in dictionary as key 
        for (int i = 0; i < nums.length; i++){
            hp.put(nums[i], i);
            // System.out.println(hp.get(nums[i]));
        }

        
        for (int i = 0; i < nums.length; i++) {
            int currentNegation = target - nums[i];
            //Check indices not values
            if (hp.containsKey(currentNegation) && i != hp.get(currentNegation)) {
                ans[0] = (i);
                ans[1] = ( hp.get(currentNegation));

                System.out.println(ans[0]+ ", " + ans[1]);
            }
        }
        
        return ans;
    } 
}