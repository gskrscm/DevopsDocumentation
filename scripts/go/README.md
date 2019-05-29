# GO Language 

## Basics
- All go projects will be in place .i.e, GOPATH
- `go env GOPATH` 
- Projects folder `GOPATH/src/<project>`

### Sample code
```
package main

import (
  "fmt"
)

func main(){

  fmt.println("Hello World")
  
  // variables 
  var x int 
  x = 10 
  var y int = 10 
  var sum int = x + y
  
  // variables shorthand
  z := 20 
  m := 30 
  add := z + m 
  
  fmt.println(sum, add)
  
  // if condition 
  x := 7  
  
  if x > 6 {
    fmt.println("More than 6")
  } else if x > 2 {
     fmt.println("More than 2")
  } else {
  }
  
}
```
- To execute `go run <filename>`
- To create executeble file `go build`
- To create executeble file and keep file in GOBIN path `go install` 
