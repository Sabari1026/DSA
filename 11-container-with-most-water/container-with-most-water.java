class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int max_area = 0;
        while (left < right){
            int width = right - left;
            int curr_area = width * Math.min(height[right], height[left]);
            max_area = Math.max(max_area,curr_area);

            if (height[left] < height[right]){
                left++;
            }
            else{
                right--;
            }
        }
    return max_area;
    }
}