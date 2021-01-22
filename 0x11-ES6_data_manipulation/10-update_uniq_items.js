export default function updateUniqueItems(mymap) {
  if (!(mymap instanceof Map)) {
    throw Error('Cannot process');
  }

  for (const [key, value] of mymap) {
    if (value === 1) {
      mymap.set(key, 100);
    }
  }
  return mymap;
}
