import "sort"

func sortVowels(s string) string {
    
    // put all vowels into array, sort it
    // loop from 0 to length of s, creating t as we go
        // if s[i] is a vowel -> insert from vowel arr
        // otherwise insert s[i]
    vowels := "aeiouAEIOU"
	isVowel := func(ch byte) bool {
		return strings.ContainsRune(vowels, rune(ch))
	}

    vowelArr := []byte{}

    for i:=0;i<len(s);i++{
        if isVowel(s[i]) {
			vowelArr = append(vowelArr, s[i])
		}
    }

    sort.Slice(vowelArr, func(i, j int) bool {
		return vowelArr[i] < vowelArr[j] 
	})


    t := ""
    vowelIdx := 0

    for i:=0;i<len(s);i++{
        if isVowel(s[i]) {
			t = t + string(vowelArr[vowelIdx])
            vowelIdx += 1
		} else{
            t = t + string(s[i])
        }
    }

    return t

}