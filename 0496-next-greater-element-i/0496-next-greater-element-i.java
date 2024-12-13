class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
    int l1 = nums1.length;
    int l2 = nums2.length;
    int indexInNums2;
    int nextGreaterElement;
    int[] ans = new int[l1];
    
    for(int i = 0; i < l1; i++){
        indexInNums2 = -1;
        nextGreaterElement = -1;
        for(int j = 0; j < l2; j++){
            if(nums1[i] == nums2[j]){
                indexInNums2 = j;
            }
            if(indexInNums2 != -1 && nums2[j] > nums1[i] && nextGreaterElement == -1){
                nextGreaterElement = nums2[j];
            }
        }
        ans[i] = nextGreaterElement;
    }
    return ans;
    }
}