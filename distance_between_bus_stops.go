// distance[i] is distance between stop i and the next clockwise stop

// two options : clockwise or counterclockwise
// Find distance for options, return the minimum

// Clockwise:
    // add all distances distance[i]s until we reach destination
// Counterclockwise add all distance[i-1 + n % n] until we reach destination

func distanceBetweenBusStops(distance []int, start int, destination int) int {
    
    n := len(distance)
    left := start
    leftSum := 0

    for left != destination{
        leftSum += distance[(left - 1 + n) % n]
        left = (left - 1 + n) % n
    }

    rightSum := 0
    right := start

    for right != destination{
        rightSum += distance[right]
        right = (right + 1) % n
    }

    return min(rightSum, leftSum)
}