export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  const firstdata = new DataView(buffer);
  if (position > length) {
    throw Error('Position outside range');
  }
  firstdata.setInt8(position, value);
  return firstdata;
}
