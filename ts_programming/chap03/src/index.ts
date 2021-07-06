import { setupMaster } from "cluster"
import { allowedNodeEnvironmentFlags } from "process"
import { arraysAreEqual } from "tslint/lib/utils"

console.log('Chapter 03')

///// p. 20 
// function squareOf(n: number) {
//     return n * n
// }
// squareOf(2)
// squareOf('z')

// function squareOf(n: any) {
//     return n * n
// }
// console.log(squareOf(2),squareOf('z'))

///// p. 22
// let a: any = 666
// let b: any = ['danger']
// let c = a + b
// console.log(c)

///// p. 23 // 확인
// let a: unknown = 30
// let b = a === 123
// //let c = a + 10
// if (typeof a === 'number') {
//     let d = a + 10
// }

// let a: unknown = 123
// let b = a === 123
// //let c = a + 10
// if (typeof a === 'number') {
//     let d = a + 'adf'
//     console.log('true!', d)
// }
// if (typeof a === 'string') {
//     let d = a + 'add'
//     console.log(d)
// }
// console.log(a, b)

///// p. 24
// let a = true
// var b = false
// const c = true
// let d: boolean = true
// let e: true = true
// let f: true = false

// let a = true
// var b = false
// const c = true
// let d: boolean = true
// let e: true = true
// //let f: true = false
// let f: true = c
// let g = a && b
// d = e
// console.log(d, g)

//// p. 25~26
// let a = 1234
// var b = Infinity * 0.10
// const c = 5678
// let d = a < b
// let e: number = 100
// let f: 26.218 = 26.218
// let g: 26.218 = 10

// let a = 1234
// var b = Infinity * 0.10
// const c = 5678
// let d = a < b
// let e: number = 100
// let f: 26.218 = 26.218
// //let g: 26.218 = 10
// let oneMil = 1_000_000
// let twoMil : 2_000_000 = 2000000
// console.log(a, b, c, d, e, f, oneMil, twoMil)

// let a = 1234n // type casting 확인
// const b = 5678n
// var c = a+b
// let d = a < 1235
// //let e = 88.5n
// let f: bigint = 100n
// let g: 100n = 100n
// //let h: bigint = 100
// console.log(a, b, c, d, f, g)

///// p. 27
// let a = 'hello'
// var b = 'billy'
// const c = '!'
// let d = a + ' ' + b + c
// let e: string = 'zoom'
// let f: 'john' = 'john'
// //let g: 'john' = 'zoe'

///// p. 28
// let a = Symbol('a')
// let b: symbol = Symbol('b')
// var c = a === b
// //let d = a + 'x'
// const e = Symbol('e')
// const f: unique symbol = Symbol('f')
// //let g: unique symbol = Symbol('f')
// let h = e === e
// //let i = e === f

// let a = Symbol('a')
// let b: symbol = Symbol('b')
// const d : unique symbol = Symbol('d')
// const e : unique symbol = Symbol('e')
// var c: typeof d = d
// let f: typeof a
// let h: number
// let g: typeof h
// console.log(a, b, c, e, e.valueOf(), e.toString(), d, c.valueOf())

///// p. 29
// let a: object = {
//     b: 'x'
// }
// a.b

// let a = {
//     b: 'x',
//     c: 5
// }
// a.b
// let b = {
//     c: {
//         d: 'f'
//     }
// }
// b.c.d


// let a: { b: number } = {
//     b: 12 
// }
// console.log(a, a.b)
// a.b = 100
// console.log(a, a.b)

///// p. 31
// let c: {
//     firstName: string
//     lastName: string
// } = {
//     firstName: 'john',
//     lastName: 'barrowman',
//     //middleName: 'lim'
// }
// class Person {
//     constructor(
//         public firstName: string,
//         public lastName: string
//     ) {}
// }
// console.log(c)
// c = new Person('matt', 'smith')
// console.log(c)

// let a: { b: number }
// a = {}
// a = { b: 1 }
// a = { b: 1, c: 2 }

// let a: {
//     b: number
//     c?: string
//     [key: number]: boolean
// }
// a = { b: 1 }
// a = { b: 1, c: undefined }
// a = { b: 1, c: 'd' }
// a = { b: 1, 10: true, 20: false, c: 'hello'}
// console.log(a, a[10], a[20], a[1])

// let gu: {
//     [a: number]: number
// }
// gu = { 1: 10, 10: 100}
// gu = { 10: 99, 100: 2 }
// console.log(gu, gu[1], gu[10], gu[100])

// let a3: {
//     [key3: string]: number
// }
// a3 = {
//     'backNum': 1,
//     'Temp': 2
// }
// console.log(a3['backNum'], a3['Temp'], a3['Hello'])

// let name: {
//     readonly lName: string
//     fName: string
// } = {
//     lName: 'Lim',
//     fName: 'JH'
// }
// name.lName = 'Kim'
// name.fName = 'SY'

// a4 = {
//     lName: 'Lee',
//     fName: 'SY',
//     10: 100
// }
// console.log(a4)
// a4.fName = 'B'
// a4[10]=1000
// console.log(a4)

// let danger: {}
// danger = {}
// danger = {x:1}
// danger = []
// danger = 2
// console.log(danger)

// let a = {
//     toString() { return 1},
//     add(aa: number, ba: number) { return aa+ba}
// }
// console.log(a)
// let b: {} = {
//     toString() { return 2},
//     add(aa: number, ba: number) { return aa+ba}
// }
// console.log(b)
// let c: object = {
//     toString() { return 3}
// }
// let d: Object = {
//     toString() { return 'a'}
// }
// console.log(a.toString(), b.toString(), c.toString(), a.add(1,2))

// let aa: {
//     com1: number
//     com2: string
//     com3: number
//     add: Function
//     sum: Function
// } = {
//     com1: 1,
//     com2: 'a',
//     com3: 99,
//     add(a: number, b: number) { return a+b},
//     sum() { return this.com1+this.com3}
// }
// console.log(aa.add(2,5), aa.sum())

// let a: object = {
//     b: 10,
//     c: 'aa'
// }
// a = {
//     b:20
// }

// console.log(a)

// let d = {
//     e: 10,
//     f: 'aa'
// }
// d = {
//     e: 20,
//     f: 'ag'
// }

// let g: {} = {
//     h: 10,
//     i: 'aa'

// }
// g = {
// }

///// o, 36
// type Age = number
// type Person = {
//     name: string
//     age: Age
// }
// let Me: Person = {
//     name: 'J',
//     age: 33
// }

// type Color = 'red'
// let x = Math.random() < .5
// if (x) {
//     type Color = 'blue'
//     let b: Color = 'blue'
//     console.log(b)
// }
// else{
//     let c: Color = 'red'
//     console.log(c)
// }

// type Cat = { name: string, purrs: boolean }
// type Dog = { name: string, barks: boolean, wags: boolean }
// type CatOrDogOrBoth = Cat | Dog
// type CatAndDog = Cat & Dog

// let a: CatOrDogOrBoth = {
//     name: 'AA',
//     purrs: true,
//     barks: true
// }
// let b: CatAndDog = {
//     name: 'BB',
//     purrs: true,
//     barks: true,
//     wags: false
// }

// function trueOrNull(isTrue: boolean) {
//     if (isTrue) {
//         return 'true'
//     }
//     return null
// }
// type Returns = string | null
// let ret: Returns = trueOrNull(true)

// function strORNum(a: string, b: number) {
//     return a || b
// }
// type Returns = string | number
// let ret: Returns = strORNum('a', 1)

// let c: number[] | string | boolean[] | null = [1, 2]
// let d: (number | string)[] = [1, 'aa']
// type Returns = string | null
// function A(a: string, b: number) {
//     return a || b
// }
// console.log(A('a', 1))

///// p. 40
// let a = [1, 2, 3]
// var b = ['a', 'b']
// let c: string[] = ['a']
// let d = [1, 'a']
// const e = [2, 'b']

// let f = ['red']
// f.push('blue')
// //f.push(true)
// console.log(f)

// let g = []
// g.push(1)
// g
// g.push('red')
// g
// g.push(true)
// console.log(g)

// let h: number[] = []
// h.push(1)
// //h.push('red')

// let i = d.map(_ => {
//     if (typeof _ === 'number') {
//         return _ * 3
//     }
//     return _.toUpperCase()
// })
// console.log(d, i)

// function buildArray() {
//     let a = []
//     a.push(1)
//     a.push('x')
//     return a
// }
// let myArray = buildArray()
// //myArray.push(true)

///// p. 42
// let a: [number] = [1]
// let b: [string, string, number] = ['malcomn', 'gladwell', 1963]
// let trainFares: [number, number?][] = [
//     [3.75],
//     [8.25, 7.70],
//     [10.50]
// ]
// let trainFares2: ([number] | [number, number])[] = [
//     [3.75],
//     [8.25, 7.70],
//     [10.50]
// ]

// let friends: [string, ...string[]] = ['a', 'b', 'c']
// let list: [number, ...string[], boolean] = [1, 'a', 'b', true]

// let as: readonly number[] = [1, 2, 3]
// let bs: readonly number[] = as.concat(4)
// let three = bs[2]
// console.log(as, bs, three)

// type A = readonly string[]
// type B = ReadonlyArray<string>
// type C = Readonly<string[]>

// type D = readonly [number, string]
// type E = Readonly<[number, string]>

// function a(x: number) {
//     if (x < 10) {
//         return x
//     }
//     return null
// }
// function b() {
//     return undefined
// }
// function c() {
//     let a = 2 + 2
//     let b = a * a
// }
// function d() {
//     throw TypeError('I always error')
// }
// function e() {
//     while (true) {
//         a(1)
//     }
// }
// console.log(a(2), b(), c())

// /// p. 47
// enum Language {
//     English = 100,
//     Spanish = 200+300,
//     Russian
// }
// let myFirstLanguage = Language.Russian
// let mySecondLanguage = Language['English']
// console.log(myFirstLanguage, mySecondLanguage)

// enum Color {
//     Red = '#c10000',
//     Blue = '#007ac1',
//     Pink = 0xc10050,
//     White = 255
// }
// let red = Color.Red
// let pink = Color.Pink
// let a = Color[6]
// console.log(red, pink, Color[255], Color[0xc10050], Color[6], a)

// const enum Flippable {
//     Burger,
//     Chair,
//     Cup,
//     Skateboard,
//     Table
// }

// function flip ( f: Flippable ) {
//     return 'flipped it'
// }
// console.log(flip(Flippable.Chair), flip(Flippable.Cup), flip(12))

// const enum Flippable {
//     Burger = 'Burger',
//     Chair = 'Chair',
//     Cup = 'Cup',
//     Skateboard = 'Skateboard',
//     Table = 'Table'
// }

// function flip ( f: Flippable ) {
//     return 'flipped it'
// }
// console.log(flip(Flippable.Chair), flip(Flippable.Cup), flip(12))

///// p. 52
// let a = 1042
// let b = 'apples and orages'
// const c = 'pineapples'
// let d = [true, true, false]
// let e = {type: 'ficus'}
// e = {type: 'gg'}
// let f = [1, false]
// const g = [3]
// let h = null

// let i: 3 = 3
// i = 4

// let j = [1, 2, 3]
// j.push(4)
// j.push('5')

// let k: never = 4

// let l: unknown = 4
// let m = l * 2