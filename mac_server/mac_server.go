package main

import (
	"net/http"
	"fmt"
	"strings"
	"os/exec"
)

func crossdomain_handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "<?xml version=\"1.0\" ?>\n<cross-domain-policy>\n<allow-access-from domain=\"*\" />\n</cross-domain-policy>")
}

func find_mac(w http.ResponseWriter, r *http.Request) {

	remote_addr := strings.Split(r.RemoteAddr, ":")

	cmd := exec.Command("arp", "-a")
	output, _ := cmd.CombinedOutput()

	mac_addr := "Unknown"

	for _, element := range strings.Split(string(output), "\n") {
		if strings.Contains(element, remote_addr[0]) {
			elems := strings.Split(element, " ")
			mac_addr = elems[3]
		}
	}

	fmt.Fprintf(w, mac_addr)
}

func main() {
	http.HandleFunc("/crossdomain.xml", crossdomain_handler)
	http.HandleFunc("/mac", find_mac)

	http.ListenAndServe(":8080", nil)
}