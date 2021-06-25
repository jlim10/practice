console.log('Hello JS')

// 3 + []      // 문자열 "3"

// let obj = {}
// obj.foo     // undefined

// function a(b) {
//     return b/2
// }
// a("z")      // NaN

function func (a, b){
    return a+b
}

console.log(func(1,2), func('a', 'b'), func('a', 2), func(3, 'b'), func(1,[2]))