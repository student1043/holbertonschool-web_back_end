export default function concatArrays(array1, array2, string) {
  console.log([].concat(...array1, ...array2, ...string));
}
