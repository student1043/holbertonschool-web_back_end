export default class HolbertonClass {
  constructor(size, location) {
    if (typeof size !== 'number') {
      TypeError('size is not a number');
    }
    if (typeof location !== 'string') {
      TypeError('location is not a string');
    }
    this._size = size;
    this._location = location;
  }

  [Symbol.toPrimitive](output) {
    if (output === 'number') {
      return this._size;
    }
    return this._location;
  }
}
