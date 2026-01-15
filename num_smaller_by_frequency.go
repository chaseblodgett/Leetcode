// Return an array where arr[i] is how many words where f(word) > f(queries[i])
// arr.length == queries[i]

// create an array frequencyArr -> each element contains frequency of queries[i]
// create wordsFrequency arr -> each element of words containts frequency of words[i]

// for each elem of frequency, count number of greater frequencies in wordsFrequency
import "fmt"
func numSmallerByFrequency(queries []string, words []string) []int {
    
    queriesFrequency := make([]int, len(queries))
    wordsFrequency := make([]int, len(words))

    // For each word -> count all frequecies, find smallest key in map keys, add frequency to frequencyArr

    for i, val := range queries{
        mp := make(map[byte]int)
        for j := 0; j < len(val); j++{
            mp[val[j]]++
        }

        smallestCharFreq := 0
        smallestChar := val[0]
        for key,val := range mp{
            if key <= smallestChar{
                smallestChar = key
                smallestCharFreq = val
            }
        }

        queriesFrequency[i] = smallestCharFreq
    }


    for i, val := range words{
        mp := make(map[byte]int)
        for j := 0; j < len(val); j++{
            mp[val[j]]++
        }

        smallestCharFreq := 0
        smallestChar := val[0]
        for key,val := range mp{
            if key <= smallestChar{
                smallestChar = key
                smallestCharFreq = val
            }
        }

        wordsFrequency[i] = smallestCharFreq
    }
    ret := make([]int, len(queries))
    for i := 0; i< len(queriesFrequency); i++{
        count := 0
        for j := 0; j < len(wordsFrequency); j++{
            if wordsFrequency[j] > queriesFrequency[i]{
                count++
            }
        }
        ret[i] = count
    }

    return ret
}