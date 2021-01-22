import Car from './10-car';

export default class EVCar extends Car {
  constructor(brand, motor, color, range) {
    if (typeof brand !== 'string') {
      TypeError('Brand must be a string');
    }
    if (typeof motor !== 'string') {
      TypeError('Motor must be a string');
    }
    if (typeof color !== 'string') {
      TypeError('Color must be a string');
    }
    if (typeof range !== 'string') {
      TypeError('Range must be a string');
    }
    super(brand, motor, color);
    this._brand = brand;
    this._motor = motor;
    this._color = color;
    this._range = range;
  }

  cloneCar() {
    return new Car();
  }
}
