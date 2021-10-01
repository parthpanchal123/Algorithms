class Solution {
    List<List<Integer>> res = new ArrayList<List<Integer>>();
        
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        if(nums.length == 0) return res;
        Arrays.sort(nums);
        bt(0,new ArrayList<Integer>(),nums);
        return res;
    }
    
    public void bt(int start,ArrayList<Integer> curr,int[] nums){
        res.add(new ArrayList<Integer>(curr));
        for(int i=start;i<nums.length;i++){
            if(i>start && nums[i-1] == nums[i]){
                continue;
            }
            curr.add(nums[i]);
            bt(i+1,curr,nums);
            curr.remove(curr.size()-1);
        }
    }
}
