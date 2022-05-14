package main

import (
	"fmt"
	"net/http"
)

const (
	sourceHost = "http://localhost:8080"
)

func main() {
	for i := 1; i < 100000; i++ {
		_, _ = http.Get(fmt.Sprintf("%s/broadcast?message=%d", sourceHost, i))
	}
}
