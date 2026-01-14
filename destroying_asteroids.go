// on collision either planet gains mass of asteriod or is destoryed
// if a planet is destroyed -> mass = 0?


// can our planet gain enough mass to destroy largest asterioid?
// At each asteroid i, check if plant + astroid[0:i] > asteroid

// sort asteroids -> simulate this process of collisions

// loop from currLargest asteroid to currPlanetMass 
// if any i in that range ^ in set of asteroids -> add to planetMass, reset loop
// if we reach 

import "sort"
func asteroidsDestroyed(mass int, asteroids []int) bool {
    sort.Ints(asteroids)
    n := len(asteroids)

    for i:=0;i<n;i++{
        if asteroids[i] > mass{
            return false
        }
        mass += asteroids[i]
    }

    return true
}