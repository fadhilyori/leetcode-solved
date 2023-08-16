func isPalindrome(s string) bool {
    nonAlphanumericRegex := regexp.MustCompile("[^a-zA-Z0-9]+")
    s = strings.ToLower(nonAlphanumericRegex.ReplaceAllString(s, ""))
    l, r := 0, len(s) - 1
    
    for l < r {
        if s[l] != s[r] {
            return false
        }
        
        l++
        r--
    }
    
    return true
}
