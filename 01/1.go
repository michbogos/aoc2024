package main

import (
	"fmt"
	"os"
	"regexp"
	"sort"
	"strconv"
)

func main() {
	s := 0
	data, _ := os.ReadFile("../inputs/01.txt")
	str := string(data)
	r := make([]int, 0)
	l := make([]int, 0)
	reg, _ := regexp.Compile("\\d+")
	for i, value := range reg.FindAllString(str, -1) {
		if i%2 == 0 {
			num, _ := strconv.Atoi(value)
			r = append(r, num)
		} else {
			num, _ := strconv.Atoi(value)
			l = append(l, num)
		}
	}
	sort.Ints(l)
	sort.Ints(r)
	for i := range l {
		val := (l[i] - r[i])
		if val < 0 {
			val = -val
		}
		s += val
	}
	fmt.Printf("%d\n", s)
}
