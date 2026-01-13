import ( 
  "strconv"
  "fmt"
)
// a map of sorts
// customerId -> { tripObject }
// tripObject : startStation, endStation, checkInTime, checkoutTime

// new data structure to map [station1-station2] {totalTrips, totalTime}
type UndergroundSystem struct {
    CustomerTrips map[int]map[string]string
    TripTimes map[string]map[string]float64
}

// empty map where each customerId maps to customer trip details
func Constructor() UndergroundSystem {
    return UndergroundSystem{
      CustomerTrips: make(map[int]map[string]string),
      TripTimes: make(map[string]map[string]float64),
    }
}

// add entry to our map 
func (this *UndergroundSystem) CheckIn(id int, stationName string, t int)  {
    this.CustomerTrips[id] = make(map[string]string)
    this.CustomerTrips[id]["startStation"] = stationName
    this.CustomerTrips[id]["checkIn"] = strconv.Itoa(t)
}

func (this *UndergroundSystem) CheckOut(id int, stationName string, t int)  {
    startStation := this.CustomerTrips[id]["startStation"]
    checkIn,_ := strconv.Atoi(this.CustomerTrips[id]["checkIn"])
    
    // not yet in tripTimes mapping
    if _,ok := this.TripTimes[startStation+"-"+stationName]; !ok{
      this.TripTimes[startStation+"-"+stationName] = make(map[string]float64)
    }

    this.TripTimes[startStation+"-"+stationName]["totalTrips"] += 1
    this.TripTimes[startStation+"-"+stationName]["totalTime"] += float64(t - checkIn)

}

// Do we need this to be 0(1)?
// if not can utilize some loop through customer lists
// can access each customers start and end times by loop through

// keep track of numTrips with those stations and totalTime taken for all trips
// return totalTime / numTrips
func (this *UndergroundSystem) GetAverageTime(startStation string, endStation string) float64 {
    return this.TripTimes[startStation+"-"+endStation]["totalTime"] / this.TripTimes[startStation+"-"+endStation]["totalTrips"]
}


/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * obj := Constructor();
 * obj.CheckIn(id,stationName,t);
 * obj.CheckOut(id,stationName,t);
 * param_3 := obj.GetAverageTime(startStation,endStation);
 */