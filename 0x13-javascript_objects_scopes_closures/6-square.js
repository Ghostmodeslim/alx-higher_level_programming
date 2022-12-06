#!/usr/bin/node

const subSquare = require('./5-square');

class Square extends subSquare {
  charPrint (c) {
    if (c === undefined) {
	    c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
	    console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
