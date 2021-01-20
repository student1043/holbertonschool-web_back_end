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
    for (const s of students) {
      if (typeof s !== 'string' && students !== null) {
        throw TypeError('Students must be an Array');
      } else {
        this._students = students;
      }
    }
  }

  get name() {
    return this._name;
  }

  set name(name) {
    if (typeof name !== 'string' && name !== null) {
      throw TypeError('Name must be a string');
    } else {
      this._name = name;
    }
  }

  get length() {
    return this._length;
  }

  set length(length) {
    if (typeof length !== 'number' && length !== null) {
      throw TypeError('Length must be a number');
    } else {
      this._length = length;
    }
  }

  get students() {
    return this._students;
  }

  set students(students) {
    for (const s of students) {
      if (typeof s !== 'string' && s !== null) {
        throw TypeError('Students must be an Array');
      } else {
        this._students = students;
      }
    }
  }
}
