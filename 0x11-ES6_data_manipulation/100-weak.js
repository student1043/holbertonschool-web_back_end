export const weakMap = new WeakMap();
export function queryAPI(endpoint) {
    let number = weakMap.get(endpoint)
    if (number === 0) {
        weakMap.set(endpoint, 1);
    }
    number = weakMap.get(endpoint)
    if (number >= 5) {
        throw Error('Endpoint load is high')
    }
}
