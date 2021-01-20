export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') {
      throw TypeError('Name must be a string');
    }
    if (typeof length !== 'number') {
      throw TypeError('Length must be a number');
    }
    if (!Array.isArray(students)) {
      throw TypeError('students must be an array');
    }
    for (let i = 0; i < students.length; i += 1) {
      if (typeof students[i] !== 'string') {
        throw TypeError('Students must be all strings');
      }
    }
    this._name = name;
    this._length = length;
    this._students = students;
  }

  set name(name) {
    if (typeof name !== 'string') {
      throw TypeError('Name must be a string');
    } else {
      this._name = name;
    }
  }

  get name() {
    return this._name;
  }

  set length(length) {
    if (typeof length !== 'number') {
      throw TypeError('Length must be a number');
    } else {
      this._length = length;
    }
  }

  get length() {
    return this._length;
  }

  set students(students) {
    if (!Array.isArray(students)) {
      throw TypeError('students must be an Array');
    }
    for (let i = 0; i < students.length; i += 1) {
      if (typeof students[i] !== 'string') {
        throw TypeError('Students must be an Array');
      } else {
        this._students = students;
      }
    }
  }

  get students() {
    return this._students;
  }
}
