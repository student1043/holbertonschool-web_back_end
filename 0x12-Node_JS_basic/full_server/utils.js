const fs = require('fs');

async function readDatabase(file) {
    await fs.readFileSync(file, (err, data) => {
        if (err) {
          throw new Error('Cannot load the database');
        }
    });
}
module.exports = readDatabase;
