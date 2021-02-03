export default function createReportObject(employeesList) {
  const employees = {
    allEmployees: { ...employeesList },
    getNumberOfDepartments: (employees) => Object.keys(employees).length,
  };

  return employees;
}
