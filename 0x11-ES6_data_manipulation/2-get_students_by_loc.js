export default function getStudentsByLocation(input, city) {
  const NewArray = input.filter((localization) => localization.location === city);
  return NewArray;
}
