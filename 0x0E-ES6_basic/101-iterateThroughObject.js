export default function iterateThroughObject(reportWithIterator) {
  const mylist = reportWithIterator.toString().replaceAll(',', ' | ');
  return mylist;
}
