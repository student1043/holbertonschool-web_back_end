class AppController {
    static getHomepage(request, response) {
        return response.send(200),
        response.end('Hello Holberton School!');
    }
}
