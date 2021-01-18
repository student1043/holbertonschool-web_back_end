export default function createIteratorObject(report) {
  const lists = []
  for (const key in report.allEmployees) {
    lists.push(report.allEmployees[key]);
  }
  return lists;
}
