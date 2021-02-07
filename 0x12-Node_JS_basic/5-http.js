const http = require('http');
const countStudents = require('./3-read_file_async');

const requestListener = function fix(req, res) {
  if (req.url === '/') {
    res.end('Hello Holberton School!');
  }
  if (req.url === '/students') {
    countStudents(process.argv[2]);
  }
  res.writeHead(200);
  res.end('Hello Holberton School!');
};
const server = http.createServer(requestListener);
server.listen(1245);
module.exports = server;
