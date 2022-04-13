int singleNumber(int* nums, int numsSize){
//     [2,2,1]
// *nums[0] == *(nums+0) 2
// *nums[1] == *(nums+1) 2
// *nums[2] == *(nums+2) 1
    
    for (int i=0; i<3;i++){
        printf("%d\n",nums[i]);
        int count = 0;
        for (int j=0; j< numsSize; j++){
            if (nums[j] == nums[i]){
                count++;
            }
        }
        if (count == 1) {
            return nums[i];
        }
    }
    return 0;
}