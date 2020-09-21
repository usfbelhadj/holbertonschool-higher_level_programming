#!/usr/bin/node
/*
class Square
*/
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
      if (size > 0)
      {
          super(size, size);
      }
  }
}

module.exports = Square;
