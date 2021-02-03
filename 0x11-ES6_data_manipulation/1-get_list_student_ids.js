export default function getListStudentIds(input) {
  if (!(input instanceof Array)) {
    return [];
  }
  return input.map((person) => (person.id));
}
