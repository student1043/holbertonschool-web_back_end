export default class HolbertonCourse {
    constructor(name = String, length = Number, students = Array) {
        this._name = name;
        this._length = length;
        this._students = students;
    }
    get name() {
    }
    set name(name) {
        this._name = name;
    }
    get length() {
    }
    set length(length) {
        this._length = length;
    }
    get students() {

    }
    set students(students) {
        this._students = students;
    }
}
