export const weakMap = new WeakMap();
export function queryAPI(endpoint) {
  let number = weakMap.get(endpoint);
  if (number) {
    weakMap.set(endpoint, weakMap.get(endpoint) + 1);
    number += 1;
  } else {
    weakMap.set(endpoint, 1);
    number = 1;
  }
  if (number >= 5) {
    throw Error('Endpoint load is high');
  }
}
