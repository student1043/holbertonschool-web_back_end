export default function updateStudentGradeByCity(input, city, newGrades) {
    return input.filter((localization) => localization.location === city).map(
        newGrades.map(((person) => (person.studentId)))
    )
}
