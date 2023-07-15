func lengthOfLongestSubstring(s string) int {
    charMap := make(map[byte]int)
	maxLength := float64(0)
	left := float64(0)

	for i := 0; i < len(s); i++ {
		c := s[i]
		if val, ok := charMap[c]; ok {
			left = math.Max(left, float64(val)+1)
		}
		charMap[c] = i
		maxLength = math.Max(maxLength, float64(i)-left+1)
	}

	return int(maxLength)
}