// some mapping of carType -> spaces available
// either mapping of 1 -> "small"
// 3 -> small spaces, 2 -> medium spaces, 1 -> big spaces

type ParkingSystem struct {
    SpacesAvailable map[int]int
}


func Constructor(big int, medium int, small int) ParkingSystem {
    mp := make(map[int]int)
    mp[1] = big
    mp[2] = medium
    mp[3] = small
    return ParkingSystem{
        SpacesAvailable: mp,
    }
}


func (this *ParkingSystem) AddCar(carType int) bool {
    if this.SpacesAvailable[carType] > 0{
        this.SpacesAvailable[carType] -= 1
        return true
    }

    return false
}


/**
 * Your ParkingSystem object will be instantiated and called as such:
 * obj := Constructor(big, medium, small);
 * param_1 := obj.AddCar(carType);
 */