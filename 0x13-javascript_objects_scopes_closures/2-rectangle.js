#!/usr/bin/node
/*
class Rectangle
*/
'use strict';

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      Rectangle.width = w;
      Rectangle.height = h;
    }
  }
}
module.exports = Rectangle;
