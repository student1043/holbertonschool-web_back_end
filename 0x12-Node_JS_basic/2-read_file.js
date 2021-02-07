const fs = require('fs');

function countStudents(file) {
  fs.readFileSync(file, (err, data) => {
    if (err) {
      throw new Error('Cannot load the database');
    }
    if (data) {
      let newLines = 0;
      const lines = data.split('\n');
      for (let i = 0; i < lines.length; i += 1) {
        if (lines[i].length > 0) newLines += 1;
      }
      console.log(`Number of students: ${newLines}`);
    }
  });
}
module.exports = countStudents;
