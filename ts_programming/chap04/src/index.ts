import { allowedNodeEnvironmentFlags } from "process"

console.log('Chapter 04: Function')

///// p. 56
// function add(a: number, b:number){
//     return a + b
// }
// function add2(a: number, b:number): number{
//     return a + b
// }
// function greet(name: string) {
//     return 'hello ' + name
// }
// let greet2 = function (name: string) {
//     return 'hello ' + name
// }
// let greet3 = (name: string) => {
//     return 'hello ' + name
// }
// let greet4 = (name: string) =>
//     'hello ' + name
// let greet5 = new Function('name', 'return "hello" + name')

///// p. 58
// function log(message: string, userId?: string) {
//     let time = new Date().toLocaleTimeString()
//     console.log(time, message, userId || 'Not signed in')
// }
// log('Page loaded')
// log('User signed in', 'da763be')

// function log(message: string, userId = 'Not signed in') {
//     let time = new Date().toLocaleTimeString()
//     console.log(time, message, userId)
// }
// log('User clicked on a button', 'da763be')
// log('User signed out')

// type Context = {
//     appId?: string
//     userId?: string
// }
// function log(message: string, context: Context = {}) {
//     let time = new Date().toLocaleTimeString()
//     console.log(time, message, context.userId)
// }
// log('User clicked on a button', { userId: 'da763be' })
// log('User signed out')

///// p. 59
// function sum(numbers:number[]): number {
//     return numbers.reduce((total, n) => total + n, 0)
// }
// console.log(sum([1, 2, 3, 4]))

// function sumVariadic(...numbers: number[]): number {
//     return Array.from(arguments).reduce((total, n) => total + n, 0)
// }
// sumVariadic(1, 2, 3, 4)

// interface Console {
//     log(message?: any, ...optionalParams: any[]): void
// }

///// p. 61
// function add(a: number, b:number): number{
//     return a + b
// }
// console.log(add(10, 20), add.apply(null, [10, 20]), add.call(null, 10, 20), add.bind(null, 10, 20)())

// let x = {
//     a() {
//         return this
//     }
// }
// let a = x.a
// console.log(a, x.a, x.a())

// function fancyDate(this: Date) {
//     return ${ this.getDate() } /${this.getMonth()}/${ this.getFullYear() }
// }
// fancyDate.call(new Date)
// fancyDate()

// function* createFibonacciGenerator() {
//     let a = 0
//     let b = 1
//     while (true) {
//         yield a;
//         [a, b] = [b, a + b]
//     }
// }
// let fibonacciGenerator = createFibonacciGenerator()
// console.log(fibonacciGenerator.next(), fibonacciGenerator.next(), fibonacciGenerator.next(), fibonacciGenerator.next(), fibonacciGenerator.next(), fibonacciGenerator.next())

// function* createNumbers(): IterableIterator<number> {
//     let n = 0
//     while (1) {
//         yield n++
//     }
// }
// let numbers = createNumbers()
// console.log(numbers.next(), numbers.next(), numbers.next(), numbers.next(), numbers.next())

///// p. 65 // 4.1.6 반복자
// let numbers = {
//     *[Symbol.iterator]() {
//         for ( let n = 1; n <= 10; n++) {
//             yield n
//         }
//     }
// }
// for (let a of numbers){
// }
// let allNumbers = [...numbers]
// let [one, two, ...rest] = numbers

///// p. 67 // 4.1.7 호출 시그니처
// function area(radius: number): number | null {
//     if (radius < 0) {
//         return null
//     }
//     return Math.PI * (radius ** 2)
// }
// let r: number = 3
// let a = area(r)
// if (a !== null) {
//     console.info('result:', a)
// }

// type Greet = (name: string) => string
// type Log = (message: string, userId?: string) => void
// let log: Log = (
//     message,
//     userId = 'Not signed in'
// ) => {
//     let time = new Date().toISOString()
//     console.log(time, message, userId)
// }
// log('Hello', 'jlim10')
// type SumVariadicSafe = (...numbers: number[]) => number

///// p. 70 // 4.1.8 문맥적 타입화
// function times(
//     f: (index: number) => void,
//     n: number
// ) {
//     for (let i = 0; i < n; i++) {
//         f(i)
//     }
// }
// times(n => console.log(n), 4)

///// p. 71 // 4.1.9 오버로드된 함수 타입
// type Log = (message: string, userId?: string) => void
// type Log2 = {
//     (message: string, userId?: string): void
// }

// type Reserve = {
//     (from: Date, to: Date, destination: string): Reservation
// }
// let reserve: Reserve = (from, to, destination) => {
//     //...
// }

// type Reserve = {
//     (from: Date, to: Date, destination: string): Reservation
//     (from: Date, destination: string): Reservation
// }
// let reserve: Reserve = (
//     from: Date,
//     toOrDestination: Date | string,
//     destination?: string
//     ) => {
//     if (toOrDestination instanceof Date && destination !== undefined) {
//         //편도 예약
//     }
//     else if ( typeof toOrDestination === 'string') {
//         // 왕복 예약
//     }
// }

// let reserve: Reserve = (
//     from: any,
//     toOrDestination: any,
//     destination?: any
//     ) => {
//     // ...
// }

// function getMonth(date: any): number | undefined {
//     if (date instanceof Date) {
//         return date.getMonth()
//     }
// }
// function getMonth2(date: Date): number {
//     return date.getMonth()
// }

// type CreateElement = {
//     (tag: 'a'): HTMLAnchorElement
//     (tag: 'canvas'): HTMLCanvasElement
//     (tag: 'table'): HTMLTableElement
//     (tag: 'string'): HTMLElement
// }
// let createElement: CreateElement = (tag: string): HTMLElement => {
//     // ...
// }
// function createElement(tag: 'a'): HTMLAnchorElement
// function createElement(tag: 'canvas'): HTMLCanvasElement
// function createElement(tag: 'table'): HTMLTableElement
// function createElement(tag: 'string'): HTMLElement {}

// function warnUser(warning) {
//     if(warnUser.wasCalled) {
//         return
//     }
//     warnUser.wasCalled = true
//     alert(warning)
// }
// warnUser.wasCalled = false

type WarnUser = {
    (warning: string): void
    wasCalled: boolean
}