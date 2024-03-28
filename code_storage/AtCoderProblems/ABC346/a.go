package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	n, _ := strconv.Atoi(scanner.Text())

	scanner.Scan()
	aStr := strings.Split(scanner.Text(), " ")
	a := make([]int, n)
	for i := 0; i < n; i++ {
		a[i], _ = strconv.Atoi(aStr[i])
	}

	ans := make([]int, n-1)
	for i := 0; i < n-1; i++ {
		ans[i] = a[i] * a[i+1]
	}

	ansAny := make([]any, len(ans))
	for i, v := range ans {
		ansAny[i] = v
	}

	fmt.Println(strings.Join(strings.Fields(fmt.Sprint(ansAny...)), " "))
}

// 綺麗に書いたversion
// package main

// import (
//     "fmt"
//     "strings"
// )

// func main() {
//     var n int
//     fmt.Scan(&n)

//     a := make([]int, n)
//     for i := 0; i < n; i++ {
//         fmt.Scan(&a[i])
//     }

//     ans := make([]int, n-1)
//     for i := 0; i < n-1; i++ {
//         ans[i] = a[i] * a[i+1]
//     }

//     fmt.Println(strings.Trim(fmt.Sprint(ans), "[]"))
// }
