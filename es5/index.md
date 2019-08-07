# es5

## Object.defineProperty(obj, prop, descriptor)

-   obj 要在其上定义属性的对象。
-   prop 要定义或修改的属性的名称。
-   descriptor 将被定义或修改的属性描述符。

*   configurable：是否可修改 descriptor 属性, 是否可 delete
*   enumerable：是否可枚举，false 的话枚举显示 undefined
*   value：属性对应的值
*   writable：当且仅当该属性的 writable 为 true 时，value 才能被赋值运算符改变
*   get：近似 value
*   set：近似 writable
*   ps：1. 属性默认为 false 或 undefined

2. 在 descriptor 中不能同时设置访问器 (get 和 set) 和 wriable 或 value，否则会报错

# Object.getOwnPropertyDescriptor(obj, prop)

-   obj 需要查找的目标对象
-   prop 目标对象内属性名称

# js 十进制和二进制的互相转换(四进制、八进制、十六进制)

-   二 => 十: parseInt(Num, 2)
-   十 => 二：Num.toString(2)

# js 除法取整、取余

-   parseInt()、%

# 检查原型链

-   param instanceof type

# 参数长度

-   实参的长度：arguments.length
-   形参的长度：fn.length

# ~，<<， >>， &...

-   ~ 在 JS 中作为位运算符表示取反，即把执行该操作的数值的二进制码的每一位（共 8 位）中 0 和 1 互换。
-   类似的还有：
    << 左移，<<\a 将 a 第一位丢弃，后七位尾部加 0
    >> 右移，>>a 将 a 末位丢弃，前七位开头加 0
    >> & 或，a & b 将 a 和 b 中所有为 1 的位组成新值
    >> | 与 ，a | b 将 a 和 b 中 ab 同时为 1 的位组成新值
    >> ^ 异，a ^ b 将 a 和 b 中 ab 不同的位组（即其中一个为 0 且另一个为 1，则为 1，两个都为 0 或都为 1，则为 0）成新值

# 一个简化 if 判断的方法(非三元表达式)

-   表达式 && 需要执行的代码块

# Object.keys(), Object.values(), Object.assgin()

# 需要将形如[{}, {}]中对应的键值取出
```bash
let list = [{a: 11}, {b: 22}, {c: 33}]
let myMap = new Map()
list.forEach(item => {
myMap.set(Object.keys(item)[0], Object.values(item)[0])
})
```