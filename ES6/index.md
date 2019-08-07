#es6

## let 和 const

## 模板字符串

## 箭头函数

## Symbol

## Set 和 Map

-   Set 结构类似于数组，但成员是不重复的值；如数组去重[...new Set(list)]

```bash
# 数组去重
[...new Set(array)]
```

-   Map 结构是键值对集合(Hash 结构)；Api 包括 new Map().get(xxx), new Map().has(xxx)

```bash
# 条件语句优化
# bad
let text;
switch(type) {
    case 1:
        text = 'a'
    break;
    case 2:
        text = 'b'
    break;
    case 3:
        text = 'c'
    break;
}

# good
let getText = new Map().set(1, 'a').set(2, 'b').set(3, 'c');
let text = getText.get(type)

```

## Promise

## Async/await
