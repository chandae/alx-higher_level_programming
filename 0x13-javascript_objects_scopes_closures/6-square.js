#!/usr/bin/node

const Square1 = require('./5-square');

module.expoers = class Square extends Square1 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    this.print(c);
  }
};
