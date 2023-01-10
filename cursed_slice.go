// seen on r/rust making fun of Go

package main

import (
	"fmt"
)

func appendAndChange(numbers []int) {
    newNumbers := append(numbers,24)
    newNumbers[0] =576
    fmt.Println("\tinside function",newNumbers)
}

func main() {
    // for the 0,1,2 example it goes from 0,1,2 as input
    //      then 576,1,2,24 after but within appendAndChange as expected from appending 24 and changing first to 576
    //      then after comes back it is 0,1,2
    fmt.Println("0,1,2 example")
    slice := []int{0,1,2}
    fmt.Println("\tinside main before function",slice)
    appendAndChange(slice)
    fmt.Println("\tinside main after function",slice)
    // but when you append 3 it has different behavior from if you had entered []int{0,1,2,3}
    //      576,1,2,3,24 after but within appendAndChange as expected
    //      but gives 576,1,2,3 upon returning back to main
    //          which is neither the 0,1,2,3 you would expect if the appendAndChange only worked with a copy that has subsequently disappeared
    //          nor the 576,1,2,3,24 if it was the same as inside appendAndChange
    //      instead it mangles the effects of appendAndChange and the keeping the same length
    fmt.Println("0,1,2,3 example")
    slice = append(slice,3)
	fmt.Println("\tinside main before function",slice)
    appendAndChange(slice)
    fmt.Println("\tinside main after function",slice)
}