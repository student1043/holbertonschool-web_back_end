export default function createIteratorObject(report) {
  const lists = [];
  for (const key in report.allEmployees) {
    for (const element in report.allEmployees[key]) {
      lists.push(report.allEmployees[key][element]);
    }
  }
  return lists;
}
