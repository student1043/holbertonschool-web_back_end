export default function createIteratorObject(report) {
  for (const key in report.allEmployees) {
    const lists = report.allEmployees[key];
    return lists;
  }
}
