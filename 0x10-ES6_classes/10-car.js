export default class Car {
    constructor(brand, motor, color) {
        if (typeof brand !== 'string') {
            TypeError('Brand must be a string')
        }
        if (typeof motor !== 'string') {
            TypeError('Motor must be a string')
        }
        if (typeof color !== 'string') {
            TypeError('Color must be a string')
        }
        this._brand = brand;
        this._motor = motor;
        this._color = color;
    }

    cloneCar() {
        Car[Symbol.match] = true;
        return new Car();
    }
}
