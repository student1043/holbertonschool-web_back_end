export default function cleanSet(set, startString) {
  if (typeof startString !== 'string') {
    return '';
  }
  if (startString === '') {
    return '';
  }
  const allvalues = [];
  set.forEach((value) => {
    if (value.startsWith(startString)) {
      allvalues.push(value.slice(startString.length, value.length));
    }
  });
  return allvalues.join('-');
}
