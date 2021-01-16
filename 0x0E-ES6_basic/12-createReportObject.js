export default function createReportObject(employeesList) {
  const employees = {
    AllEmployees: ...employeesList,
    getNumberOfDepartments: Object.keys(employees).length
  };

  return employees;
}
