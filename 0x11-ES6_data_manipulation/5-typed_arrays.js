export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  const dv1 = new DataView(buffer);
  if (position > length) {
    throw Error('Position outside range');
  }
  dv1.setInt8(position, value);
  return dv1;
}
