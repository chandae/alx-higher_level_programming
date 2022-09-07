#!/usr/bin/node

exports.esrever = function (list) {
  const array = [];
  const iter = list.length;
  for (let i = iter - 1; i >= 0; i--) {
    array.push(list[i]);
  }
  return array;
};
