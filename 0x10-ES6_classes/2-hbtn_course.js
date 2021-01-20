export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string' && name !== null) {
      throw TypeError('Name must be a string');
    } else {
      this._name = name;
    }
    if (typeof length !== 'number' && length !== null) {
      throw TypeError('Length must be a number');
    } else {
      this._length = length;
    }
    for (let i = 0; i < students.length; i += 1) {
      if (typeof students[i] !== 'string') {
        throw TypeError('Students must be an Array');
      } else {
        this._students = students;
      }
    }
  }

  get name() {
    return this._name;
  }

  get length() {
    return this._length;
  }

  get students() {
    return this._students;
  }

  set name(name) {
    if (typeof name !== 'string' && name !== null) {
      throw TypeError('Name must be a string');
    } else {
      this._name = name;
    }
  }

  set length(length) {
    if (typeof length !== 'number' && length !== null) {
      throw TypeError('Length must be a number');
    } else {
      this._length = length;
    }
  }

  set students(students) {
    for (let i = 0; i < students.length; i += 1) {
      if (typeof students[i] !== 'string') {
        throw TypeError('Students must be an Array');
      } else {
        this._students = students;
      }
    }
  }
}
