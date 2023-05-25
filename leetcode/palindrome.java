// leetcode problem #9!

import java.util.*;
class palindrome {
    public boolean isPalindrome(int x) {
        int c = 0;
        String s = Integer.toString(x);

        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == s.charAt(s.length() - i - 1)){
                c++;
            }
        }
        if(c == s.length()){
            return true; 
        }
        else{
            return false; 
        }
    }
}