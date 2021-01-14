export default function createReportObject(employeesList) {
  const employees = {
    AllEmployees: employeesList,
    getNumberOfDepartments: (employeesList) => `${employeesList}`
  };

  return employees;
}
