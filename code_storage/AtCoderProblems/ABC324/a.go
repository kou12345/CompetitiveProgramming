package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	var n int
	fmt.Scanf("%d", &n)
	fmt.Println(n)

	var a []int

	sc := bufio.NewScanner(os.Stdin)
	sc.Scan()
	inputs := strings.Split(sc.Text(), "")

	for _, input := range inputs {
		i, _ := strconv.Atoi(input)
		a = append(a, i)
	}

	fmt.Println(a)

}
