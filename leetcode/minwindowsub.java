class minwindowsub {
    public static String minWindow(String s, String t) {
        // increase window until we find 1, then delete length of the elements looked thru so far until we found 1
        // then continue to increase window until find all 3, store as min, continue looking

        if(t.length() > s.length()){
            return "";
        }

        int left = 0;
        int right = 0;
        boolean [] visited = new boolean[t.length()];
        boolean done = false;
        boolean appended = false;

        StringBuilder ret = new StringBuilder("");
        StringBuilder old = new StringBuilder(s + "b");

        while(right < s.length()){
            boolean all = true;

            for(int i = 0; i < t.length(); i++){
                if(t.charAt(i) == s.charAt(right) && visited[i] != true){
                    visited[i] = true;
                    ret.append(t.charAt(i));
                    System.out.println("Appended: " + t.charAt(i));
                    System.out.println("appended: " + right);
                    System.out.println();
                    done = true;
                    appended = true;
                    break;
                }
                else{
                    appended = false;
                }
            }
            
            if(done && !appended){
                ret.append(s.charAt(right));
                System.out.println("Not Appended: " + s.charAt(right));
                System.out.println("Not appended: " + right);
                System.out.println();
            }

            right++;

            for(boolean b : visited){
                if(!b) all = false;
            }

            if(all){
                visited = new boolean[t.length()];
                done = false;
                old = ret.length() < old.length() ? ret : old;

                ret = new StringBuilder("");
                right = right - 1;
            }
        }

        return old.toString().equals(s + "b") ? "" : old.toString();
    }

    public static void main(String [] args){
        System.out.println(minWindow("a", "a"));
    }
}