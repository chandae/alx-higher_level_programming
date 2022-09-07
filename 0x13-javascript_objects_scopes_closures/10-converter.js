#!/usr/bin/node

exports.converter = function (base) {
  // set base when initialising function
  function convert (number) {
    return number.toString(base);
  }
  return convert;
};
