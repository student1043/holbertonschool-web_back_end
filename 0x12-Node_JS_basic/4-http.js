const http = require('http');

const requestListener = function fix(req, res) {
  res.writeHead(200);
  res.end('Hello Holberton School!');
};
const server = http.createServer(requestListener);
server.listen(1245);
module.exports = server;
