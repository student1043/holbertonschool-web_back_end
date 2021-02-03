export default class Airport {
  constructor(name, code) {
    if (typeof name !== 'string') {
      TypeError('Name is not a string');
    }
    if (typeof code !== 'string') {
      TypeError('Code is not a string');
    }
    this._name = name;
    this._code = code;
  }

  get name() {
    return this._name;
  }

  get code() {
    return this._code;
  }
}
Airport.prototype.toString = function t() {
  return '[object SFO]';
};
