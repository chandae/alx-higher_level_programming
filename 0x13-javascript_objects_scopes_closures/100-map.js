#!/usr/bin/node

const list = require('./100-data');

const newList = [];
for (let i = 0; i < list.list.length; i++) {
  newList.push(list.list[i] * i);
}
console.log(list.list);
console.log(newList);
