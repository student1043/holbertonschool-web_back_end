export const weakMap = new WeakMap();
export function queryAPI(endpoint) {
  const number = weakMap.get(endpoint);
  if (number === 0) {
    weakMap.set(endpoint, 1);
  } else {
    weakMap.set(endpoint, weakMap.get(endpoint) + 1);
  }

  if (number >= 5) {
    throw Error('Endpoint load is high');
  }
}
