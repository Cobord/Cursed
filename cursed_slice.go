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
    fmt.Println("0,1,2 example")
    slice := []int{0,1,2}
    fmt.Println("\tinside main before function",slice)
    appendAndChange(slice)
    fmt.Println("\tinside main after function",slice)
    fmt.Println("0,1,2,3 example")
    slice = append(slice,3)
	fmt.Println("\tinside main before function",slice)
    appendAndChange(slice)
    fmt.Println("\tinside main after function",slice)
}