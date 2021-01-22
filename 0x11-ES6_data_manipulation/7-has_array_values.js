export default function hasValuesFromArray(set, array) {
  for (const idx in array) {
    if (!(set.has(array[idx]))) {
      return false;
    }
  }
  return true;
}
