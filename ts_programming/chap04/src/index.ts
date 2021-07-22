import { allowedNodeEnvironmentFlags } from "process"
import { mapDefined } from "tslint/lib/utils"

console.log('Chapter 04: Function')

///// p. 56 // 4.1 함수
// function add(a: number, b:number){
//     return a + b
// }
// function add2(a: number, b:number): number{
//     return a + b
// }

// function greet(name: string) {              // 1. 이름을 붙인 함수
//     return 'hello ' + name
// }
// let greet2 = function (name: string) {      // 2. 함수 표현식
//     return 'hello ' + name
// }
// let greet3 = (name: string) => {            // 3. 화살표 함수 표현식
//     return 'hello ' + name
// }
// let greet4 = (name: string) =>              // 4. 단축형 화살표 함수 표현식
//     'hello ' + name
// let greet5 = new Function('name', 'return "hello" + name')  // 5. 함수 생성자

///// p. 58 // 4.1.1 선택적 매개변수와 기본 매개변수
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

///// p. 59 // 4.1.2 나머지 매개변수
// function sum(numbers:number[]): number {
//     return numbers.reduce((total, n) => total + n, 0)
// }
// console.log(sum([1, 2, 3]))

// function sumVariadic(): number {
//     return Array
//     .from(arguments)
//     .reduce((total, n) => total + n, 0)
// }
// sumVariadic(1, 2, 3, 4)

// function sumVariadic(...numbers: number[]): number {
//     console.log(numbers, arguments, typeof arguments)
//     return Array
//     .from(arguments)
//     .reduce((total, n) => total + n, 0)
// }
// console.log(sumVariadic(1, 2, 3, 4))

// function sumVariadic(...numbers: number[]): number {
//     console.log(numbers, arguments, typeof arguments, Array.from(arguments))
//     return numbers.reduce((total, n) => total + n, 0)
// }
// console.log(sumVariadic(1, 2, 3, 4))

// interface Console {
//     log(message?: any, ...optionalParams: any[]): void
// }

///// p. 61 // 4.1.3 call, apply, bind
// function add(a: number, b:number): number{
//     return a + b
// }
// console.log(add(10, 20))
// console.log(add.apply(null, [10, 20]))
// console.log(add.call(null, 10, 20))
// console.log(add.bind(null, 10, 20))

// let x = {
//     a() {
//         return this
//     }
// }
// console.log('x.a: ', x.a, ', x,a(): ', x.a(), ', x: ', x)
// let b = x.a
// console.log('b: ', b, ', b(): ', b())
// let y = {
//     c: x.a
// }
// console.log('y.c: ', y.c, ', y.c(): ', y.c(), ', y: ', y)

// function fancyDate() {
//     return ${ this.getDate() } /${this.getMonth()}/${ this.getFullYear() } // Expression Language 에러발생
// }

// function fancyDate(this: Date) {
//     return this.getDate().toString() + '/' + this.getMonth().toString() + '/' + this.getFullYear().toString()
//     //return ${ this.getDate() } /${this.getMonth()}/${ this.getFullYear() } // Expression Language 에러발생
// }
// console.log(fancyDate.call(new Date))
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
// console.log(
//     fibonacciGenerator.next(),
//     fibonacciGenerator.next(),
//     fibonacciGenerator.next(),
//     fibonacciGenerator.next(),
//     fibonacciGenerator.next(),
//     fibonacciGenerator.next(),
//     fibonacciGenerator.next()
// )

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
//     console.log(a)
// }
// let allNumbers = [...numbers]
// let [one, two, ...rest] = numbers
// let [one1, two2] = numbers
// console.log(allNumbers, one, two, one1, two2, rest)


///// p. 67 // 4.1.7 호출 시그니처
// function sum(a: number, b:number): number { return a + b }
// function sub(a: number, b:number): number { return a - b }
// function mul(a: number, b:number): number { return a * b }
// function div(a: number, b:number): number { return a / b }

// type Operations = (a: number, b: number) => number

// let sum2: Operations = (a, b) => {
//     return a + b
// }
// let sub2: Operations = (a, b) => {
//     return a - b
// }
// let mul2: Operations = (a, b) => {
//     return a * b
// }
// let div2: Operations = (a, b) => {
//     return a / b
// }
// console.log(sum2(1,2), sub2(19,13), mul2(7,8), div2(10, 5))

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

// function log1(message: string, userId?: string) {
//     let time = new Date().toLocaleTimeString()
//     console.log(time, message, userId || 'Not signed in')
// }

// function log2(message: string, userId = 'Not signed in') {
//     let time = new Date().toLocaleTimeString()
//     console.log(time, message, userId)
// }

// type Log = (message: string, userId?: string) => void

// let log11: Log = (
//     message,
//     userId?
// ) => {
//     let time = new Date().toISOString()
//     console.log(time, message, userId || 'Not signed in')
// }

// let log22: Log = (
//     message,
//     userId = 'Not signed in'
// ) => {
//     let time = new Date().toISOString()
//     console.log(time, message, userId)
// }

// type Greet = (name: string) => string
// let greet: Greet = (name) => {
//     return 'Hello' + name
// }

// type SumVariadicSafe = (...numbers: number[]) => number
// let sumVariadicSafe: SumVariadicSafe = (...numbers) => {
//     return numbers.reduce((total, n) => total+n, 0)
// }
// console.log(sumVariadicSafe(4,2,3,7))

///// p. 70 // 4.1.8 문맥적 타입화
// function times(
//     f: (index: number) => void,
//     n: number
// ) {
//     for (let i = 0; i < n; i++) {
//         f(i)
//     }
// }
// times(n =>console.log(n), 4)
// times(console.log, 4)

// function f(n: number) {
//     console.log(n)
// }
// times(f, 4)

///// p. 71 // 4.1.9 오버로드된 함수 타입
// type Log = (message: string, userId?: string) => void
// type Log2 = {
//     (message: string, userId?: string): void
// }

// type Reserve = {
//     (from: Date, to: Date, destination: string): Reservation
// }
// let reserve: Reserve = (from, to, destination) => {
//     // ...
// }

// type Reservation = void

// type Reserve = {
//     (from: Date, to: Date, destination: string): Reservation
//     (from: Date, destination: string): Reservation
// }
// let reserve: Reserve = (from, to) => {
//     // ...
// }

// let reserve: Reserve = (
//     from: Date,
//     toOrDestination: Date | string,
//     destination?: string) => {
//         // ...
// }

// type Reserve1 = {
//     (from: Date, to: Date, destination: string): Reservation
// }
// type Reserve2 = {
//     (from: Date, destination: string): Reservation
// }
// type ReserveUnion = Reserve1 | Reserve2

// let reserve2: ReserveUnion = (from, toOrDestination, desination) => {
//     // ...
// }

// type Reservation = [Date, Date | string, string?]

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
//         // ...
//     }
//     else if ( typeof toOrDestination === 'string') {
//         // ...
//     }
// }
// type Reservation = void

// let reserve2: Reserve = (
//     from: any,
//     toOrDestination: any,
//     destination?: any
//     ) => {
//     // ...
// }
// reserve2(new Date, new Date, 'Seoul')
// reserve2(new Date, 'Seoul')

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
//     (tag: string): HTMLElement
// }
// let createElement: CreateElement = (tag: string): HTMLElement => {
//     // ...
//     return new HTMLElement
// }
// function createElement2(tag: 'a'): HTMLAnchorElement
// function createElement3(tag: 'canvas'): HTMLCanvasElement
// function createElement4(tag: 'table'): HTMLTableElement
// function createElement5(tag: 'string'): HTMLElement {}

// function warnUser(warning: string) {
//     if(warnUser.wasCalled) {
//         return
//     }
//     warnUser.wasCalled = true
//     alert(warning)
// }
// warnUser.wasCalled = false

// type WarnUser = {
//     (warning: string): void
//     wasCalled: boolean
// }
// let warnUser2: WarnUser = (warning) => {
//     if(warnUser2.wasCalled) {
//         return
//     }
//     warnUser2.wasCalled = true
//     alert(warning)
// }
// warnUser2.wasCalled = false
// let warnUser2: WarnUser
// warnUser2 = (warning) => {warnUser2.wasCalled = true}
// warnUser2.wasCalled = false

///// p. 78 4.2 다형성

// function filter(array, f) {
//     let result = []
//     for (let i = 0; i < array.length; i++){
//         let item = array[i]
//         if (f(item)) {
//             result.push(item)
//         }
//     }
//     return result
// }
// filter([1, 2, 3, 4], _ => _ < 3)    // [1, 2]

// type Filter = {
//     (array: number[], f: (item: number) => boolean): number[]
//     (array: string[], f: (item: string) => boolean): string[]
//     (array: object[], f: (item: object) => boolean): object[]
// }

// let filter: Filter = (array, f) => {
//     let result = []
//     for (let i = 0; i < array.length; i++){
//         if (f(array[i])) {
//             result.push(array[i])
//         }
//     }
//     return result
// }

// let names = [
//     { firstName: 'beth' },
//     { firstName: 'caitlyn' },
//     { firstName: 'xin' }
// ]

// let result = filter(
//     names,
//     _ => _.firstName.startsWith('b')
// )
// result[0].firstName

///// p.81 제네릭 타입 매개변수
// type Filter = {
//     <T>(array: T[], f: (item: T) => boolean): T[]
// }

// let filter: Filter = (array, f) => {
//     let result = []
//     for (let i = 0; i < array.length; i++){
//         if (f(array[i])) {
//             result.push(array[i])
//         }
//     }
//     return result
// }

// console.log(filter([1,2,3], _ => _ > 2))

// console.log(filter(['a', 'b'], _ => _ !== 'b'))

// let names = [
//     { firstName: 'beth' },
//     { firstName: 'caitlyn' },
//     { firstName: 'xin' }
// ]
// console.log(filter(names, _ => _.firstName.startsWith('b')))

///// p.83 // 4.2.1 언제 제네릭 타입이 한정되는가?
// type Filter = {
//     <T>(array: T[], f: (item: T) => boolean): T[]
// }
// let filter: Filter = (array, f) => //...

// type Filter<T> = {
//     (array: T[], f: (item: T) => boolean): T[]
// }

// let filter: Filter = (array, f) => {
//     let result = []
//     for (let i = 0; i < array.length; i++){
//         if (f(array[i])) {
//             result.push(array[i])
//         }
//     }
//     return result
// }

// type OtherFilter = Filter

// type StringFilter = Filter<string>
// let stringFilter: StringFilter = (array, f) => // ...

///// p.84 // 4.2.2 제네릭을 어디에 선언할 수 있을까?
// type Filter = {
//     <T>(array: T[], f: (item: T) => boolean): T[]
// }
// let filter: Filter = (array, f) => //...

// type Filter<T> = {
//     (array: T[], f: (item: T) => boolean): T[]
// }
// let filter: Filter<number> = (array, f) => //...

// type Filter = <T>(array: T[], f: (item: T) => boolean) => T[]
// let filter: Filter = (array, f) => //...

// type Filter<T> = (array: T[], f: (item: T) => boolean) => T[]
// let filter: Filter<string> = (array, f) => //...

// function filter<T>(array: T[], f: (item: T) => boolean): T[] {
//     return []
// }

// function map(array: unknown[], f: (item: unknown) => unknown): unknown[] {
//     let result = []
//     for (let i = 0; i < array.length; i++) {
//         result[i] = f(array[i])
//     }
//     return result
// }

// function map<T, U>(array: T[], f: (item: T) => U): U[] {
//     let result = []
//     for (let i = 0; i < array.length; i++) {
//         result[i] = f(array[i])
//     }
//     return result
// }

// interface Array<T> {
//     filter(
//         callbackfn: (value: T, index: number, array: T[]) => any,
//         thisArg?: any
//     ): T[]
//     map<U>(
//         callbackfn: (value: T, index: number, array: T[]) => U,
//         thisArg?: any
//     ): U[]
// }
// let a = new Array
// a.map()

///// p.87 // 4.2.3 제네릭 타입 추론
// function map<T, U>(array: T[], f: (item: T) => U): U[] {
//     // ...
// }
// map(
//     ['a', 'b', 'c'],
//     _ => _ === 'a'
// )
// map<string, boolean>(
//     ['a', 'b', 'c'],
//     _ => _ === 'a'
// )
// map<string>(
//     ['a', 'b', 'c'],
//     _ => _ === 'a'
// )
// map<string, boolean | string>(
//     ['a', 'b', 'c'],
//     _ => _ === 'a'
// )
// map<string, number>(
//     ['a', 'b', 'c'],
//     _ => _ === 'a'
// )

// let promise = new Promise(resolve =>
//     resolve(45)
// )
// promise.then(result =>
//     result * 4
// )

// let promise = new Promise<number>(resolve =>
//     resolve(45)
// )
// promise.then(result =>
//     result * 4
// )

///// p.89 // 4.2.4 제네릭 타입 별칭
// type MyEvent<T> = {
//     target: T
//     type: string
// }
// type ButtonEvent = MyEvent<HTMLButtonElement>
// let myEvent: MyEvent<HTMLButtonElement | null> = {
//     target: document.querySelector('#myButton'),
//     type: 'click'
// }
// type TimedEvent<T> = {
//     event: MyEvent<T>
//     from: Date
//     to: Date
// }

// function triggerEvent<T>(event: MyEvent<T>): void {
//     // ...
// }

// triggerEvent({
//     target: document.querySelector('#myButton'),
//     type: 'mouseover'
// })

///// p.91 // 4.2.5 한정된 다형성
// type TreeNode = {
//     value: string
// }
// type LeafNode = TreeNode & {
//     isLeaf: true
// }
// type InnerNode = TreeNode & {
//     children: [TreeNode] | [TreeNode, TreeNode]
// }

// let a: TreeNode = {value: 'a'}
// let b: LeafNode = {value: 'b', isLeaf: true}
// let c: InnerNode = {value: 'c', children: [b]}

// let a1 = mapNode(a, _ => _.toUpperCase())
// let b1 = mapNode(b, _ => _.toUpperCase())
// let c1 = mapNode(c, _ => _.toUpperCase())

// function mapNode<T extends TreeNode>(
//     node: T,
//     f: (value: string) => string
// ): T {
//     return {
//         ...node,
//         value: f(node.value)
//     }
// }
// console.log(a1, b1, c1)

// type HasSides = { numberOfSides: number }
// type SidesHaveLength = { sideLength: number }

// function logPerimeter<Shape extends HasSides & SidesHaveLength>(s: Shape): Shape {
//     console.log(s.numberOfSides * s.sideLength)
//     return s
// }

// type Squre = HasSides & SidesHaveLength
// let square: Squre = { numberOfSides: 4, sideLength: 3 }
// logPerimeter(square)

// function call(
//     f: (...args: unknown[]) => unknown,
//     ...args: unknown[]
// ): unknown {
//     return f(...args)
// }

// function fill(length: number, value: string): string[] {
//     return Array.from({ length }, () => value)
// }

// console.log(call(fill, 10, 'a'))

// function call2<T,U>(
//     f: (...args: T[]) => U,
//     ...args: T[]
// ):U {
//     return f(...args)
// }
// console.log(call2(fill, 10, 'a'))


// function call<T extends unknown[], R>(
//     f: (...args: T) => R,
//     ...args: T
// ): R {
//     return f(...args)
// }
// let a = call(fill, 10, 'a')
// let b = call(fill, 10)
// let c = call(fill, 10, 'a', 'z')

///// p.96 // 4.2.6 제네릭 타입 기본값
// type MyEvent<T> = {
//     target: T
//     type: string
// }

// let buttonEvent: MyEvent<HTMLButtonElement>

// type MyEvent<T = HTMLElement> = {
//     target: T
//     type: string
// }

// type MyEvent<T extends HTMLElement = HTMLElement> = {
//     target: T
//     type: string
// }

// let myEvent: MyEvent = {
//     target: myElement,
//     type: string
// }

// type MyEvent2<Type extends string, Target extends HTMLElement = HTMLElement> = {
//     target: Target
//     type: Type
// }

// type MyEvent3<Target extends HTMLElement = HTMLElement, Type extends string> = {
//     target: Target
//     type: Type
// }