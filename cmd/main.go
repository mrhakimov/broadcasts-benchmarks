package main

import (
	"flag"
	"fmt"
	"net/http"
)

const (
	sourceHost = "http://localhost:8080"
)

func main() {
	mbytes := flag.Int("mbytes", 1, "the number of bytes of sending messages")
	broadcast := flag.String("broadcast", "brb", "choose one of the supported broadcasts: brb or cebrb")
	flag.Parse()

	msg := ""
	for i := 0; i < *mbytes; i++ {
		msg += "0"
	}

	for i := 1; i < 1000000; i++ {
		_, _ = http.Get(fmt.Sprintf("%s/%s/broadcast?message=%s", sourceHost, *broadcast, msg))
	}
}
