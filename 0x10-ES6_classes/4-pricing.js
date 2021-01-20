import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    if (typeof amount !== 'number') {
      TypeError('Amount is not a number');
    }
    if (!(currency instanceof Currency)) {
      TypeError('Currency is not a currency');
    }
    this._amount = amount;
    this._currency = currency;
  }

  set amount(amount) {
    if (typeof amount !== 'number') {
      TypeError('Amount is not a number');
    }
    this._amount = amount;
  }

  get amount() {
    return this._amount;
  }

  set currency(currency) {
    if (!(currency instanceof Currency)) {
      TypeError('Currency is not a currency');
    }
    this._currency = currency;
  }

  get currency() {
    return this._currency;
  }

  displayFullPrice() {
    return (`${this._amount} ${this._currency.name} (${this._currency.code})`);
  }

  static convertPrice(amount, conversionRate) {
    if (typeof amount !== 'number') {
      TypeError('Amount is not a number');
    }
    if (typeof conversionRate !== 'number') {
      TypeError('Amount is not a number');
    }
    return amount * conversionRate;
  }
}
