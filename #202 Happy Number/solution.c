// n = 19
// 1 => 1*1 + 9*9 = 82
// 2 => 8*8 + 2*2 = 68
// 3 => 6*6 + 8*8 = 100
// 4 => 1*1 + 0*0 +0*0 = 1 
int check_happy(int target)
{    
    int sum = (target % 10)*(target % 10);    
    /* Chech digit */
    while ((target / 10) > 0) {              
        target /= 10;
        sum += (target % 10)*(target % 10);
    }
    
    return sum;
}

bool isHappy(int n)
{
    int fast = n, slow = n;
    do {  
        /* slow calculate once per round*/
        slow = check_happy(slow);
        /* fast calculate two times per round*/
        fast = check_happy(fast);
        fast = check_happy(fast);
        if (slow == 1 || fast == 1)        
            return true;        
    } while (slow != fast);  

    return  false;
}
