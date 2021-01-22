/* eslint-disable */
export default function updateStudentGradeByCity(input, city, newGrades) {
  return input.filter((localization) => localization.location === city).map(
    (student) => {
      let found = false;
      for (const mystudents of newGrades) {
        if (student.id === mystudents.studentId) {
          student.grade = mystudents.grade;
          found = true;
        }
      }
      if (found === false) {
        student.grade = 'N/A';
      }
      return student;
    },
  );
}
