package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func main() {
	data, _ := ioutil.ReadFile("input.txt")
	input := strings.Split(string(data), "\n")
	final := 2020
	for i, price := range input {
		if price == "" {
			continue
		}

		intPrice, _ := strconv.Atoi(price)

		for ii, cmp_price := range input[i+1:] {
			if cmp_price == "" {
				continue
			}

			intCmpPrice, _ := strconv.Atoi(cmp_price)

			for _, cmp_cmp_price := range input[ii+1:] {
				if cmp_cmp_price == "" {
					continue
				}

				intCmpCmpPrice, _ := strconv.Atoi(cmp_cmp_price)

				if (intPrice + intCmpPrice + intCmpCmpPrice) == final {
					fmt.Printf("found!! %d", intCmpPrice*intPrice*intCmpCmpPrice)
				}
			}
		}
	}
}
