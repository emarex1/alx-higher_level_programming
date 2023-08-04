#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || typeof w !== 'number' || typeof h !== 'number') {
      // If w or h is equal to 0 or not a positive integer, create an empty object
      return {};
    }
    this.width = w;
    this.height = h;
  }

  print () {
    if (this.width && this.height) {
      // If both width and height are valid, print the rectangle
      for (let i = 0; i < this.height; i++) {
        let row = '';
        for (let j = 0; j < this.width; j++) {
          row += 'X';
        }
        console.log(row);
      }
    }
  }
};
