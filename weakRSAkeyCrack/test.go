package main

import (
    "bytes"
    "log"
    "net"
    "strings"
)

func getThreeBlocks(input string) [128]byte {
    conn, err := net.Dial("tcp", "chc.cs.cornell.edu:1352") //39
    defer conn.Close()
    if err != nil {
        log.Fatal(err)
    }
    _, err = conn.Write([]byte(input))
    if err != nil {
        log.Fatal(err)
    }
    conn.(*net.TCPConn).CloseWrite()

    var buf [128]byte
    conn.Read(buf[:])
    return buf
}

const printable string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
const flagLen int = 32//32

func main() {
    known := bytes.NewBufferString("CHC{") // Technically you can write "CHC{" here

outer:
    for known.Len() != flagLen { // while known.Len() != flagLen:
        preambleLen := flagLen - known.Len() + 15
        preamble := strings.Repeat("A", preambleLen)

        goal := getThreeBlocks(preamble)

        for _, char := range printable { // for char in printable:
            try := getThreeBlocks(preamble + known.String() + string(char))
            if try == goal {
                known.WriteRune(char)
                log.Println(known.String())
                continue outer
            }
        }
        log.Fatalln("cannot continue")
    }
}
