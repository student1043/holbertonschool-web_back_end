export default function appendToEachArrayValue(array, appendString) {
  const newarray = [];
  for (const idx of array) {
    const value = array[array.indexOf(idx)];
    newarray.push(appendString + value);
  }

  return Object.values(newarray);
}
