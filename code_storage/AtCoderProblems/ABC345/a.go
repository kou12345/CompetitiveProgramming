package main

import "fmt"

func main() {
	var s string
	fmt.Scan(&s)

	if s[0] != 60 {
		fmt.Println("No")
		return
	}
	if s[len(s)-1] != 62 {
		fmt.Println("No")
		return
	}

	for i := 1; i < len(s)-1; i++ {
		if s[i] != 61 {
			fmt.Println("No")
			return
		}
	}

	fmt.Println("Yes")

}

// < 60
// = 61
// > 62

// 良い書き方 chはcharacterの略
// package main

// import "fmt"

// func main() {
//     var s string
//     fmt.Scan(&s)

//     if len(s) < 3 || s[0] != '<' || s[len(s)-1] != '>' {
//         fmt.Println("No")
//         return
//     }

//     for _, ch := range s[1 : len(s)-1] {
//         if ch != '=' {
//             fmt.Println("No")
//             return
//         }
//     }

//     fmt.Println("Yes")
// }
