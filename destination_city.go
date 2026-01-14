func destCity(paths [][]string) string {
    
    // paths[i][1] is either intermediary city or destination
    // It is final destination if we don't leave from that city
    // I.e. paths[i][1] does exist in paths[i][0] for all i

    // Make set to store all departure cities
    // Loop through arrival cities, if city is not in departures -> final destination

    set := make(map[string]struct{})

    for _,path := range paths{
        set[path[0]] = struct{}{}
    }

    finalDestination := ""
    for _,path := range paths{
        if _,ok := set[path[1]]; !ok{
            finalDestination = path[1]
        }
    }

    return finalDestination
}