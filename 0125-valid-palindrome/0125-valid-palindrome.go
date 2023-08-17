func isPalindrome(s string) bool {
	s = strings.ToLower(s)
	left, right := 0, len(s)-1

	for left < right {
        sl, sr := rune(s[left]), rune(s[right])
		if !isAlphanumeric(sl) {
			left++
			continue
		}

		if !isAlphanumeric(sr) {
			right--
			continue
		}

		if sl != sr {
			return false
		}
        
		left++
		right--
	}

	return true
}

func isAlphanumeric(c rune) bool {
    return unicode.IsLetter(c) || unicode.IsNumber(c)
}