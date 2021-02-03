export default function getStudentIdsSum(input) {
  return input.reduce((total, numberofstudents) => total + numberofstudents.id, 0);
}
