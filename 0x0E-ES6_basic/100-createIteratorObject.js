export default function createIteratorObject(report) {
  const lists = [];
  for (const key in report.allEmployees) {
    if (key !== 0) {
      for (const element in report.allEmployees[key]) {
        if (element !== 0) {
          lists.push(report.allEmployees[key][element]);
        }
      }
    }
  }
  return lists;
}
