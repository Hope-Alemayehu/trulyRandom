//this part is totally not necessary but i already wrote it
//so yeah till i find a reason to integrate it
//it shall stay

package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"sync"
)

const apiURL = "http://localhost:8000/random_number"

type Response struct {
	RandomNumber int `json:"random_number"`
}

func fetchRandomNumber(wg *sync.WaitGroup) {
	defer wg.Done()

	resp, err := http.Get(apiURL)
	if err != nil {
		log.Println("error fetching random number:", err)
		return
	}

	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Println("error reading response body:", err)
		return
	}

	var response Response
	err = json.Unmarshal(body, &response)
	if err != nil {
		log.Println("error unmarshlling JSON:", err)
		return
	}
	fmt.Println("Random number:", response.RandomNumber)

}

func main() {
	var wg sync.WaitGroup

	for i := 0; i < 10; i++ {
		wg.Add(1)
		go fetchRandomNumber(&wg)
	}

	wg.Wait()
}
