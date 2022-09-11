#!/usr/bin/node

const list = require('./100-data').list;
const mapped = list.map((value, index) => value * index);
console.log(list);
console.log(mapped);
