class Solution {
    public String mergeAlternately(String word1, String word2) {
        // Much faster than string and "+="
        StringBuilder sb = new StringBuilder();

        int shorterWordLength = word1.length() < word2.length() ? word1.length() : word2.length();

        // Loop up until twice the shorter word
        for (int i = 0, j = 0, k = 0; i < shorterWordLength*2; i++) {
            if (i % 2 == 0) {
                sb.append(word1.charAt(j));
                j++;
            } else {
                sb.append(word2.charAt(k));
                k++;
            }
        }

        // append the rest of the longer string if needed
        if (word1.length() > word2.length()) {
            sb.append(word1.substring(word2.length()));
        } else {
            sb.append(word2.substring(word1.length()));
        }

        return sb.toString();
        
    }
}
