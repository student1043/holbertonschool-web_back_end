export default function appendToEachArrayValue(array, appendString) {
  const newarray = [];
  for (const idx of array) {
    const value = array[idx];
    newarray[idx] = appendString + value;
  }

  return Object.values(newarray);
}
