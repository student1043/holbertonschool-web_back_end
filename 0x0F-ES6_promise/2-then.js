export default function handleResponseFromAPI(promise) {
  Promise.all(console.log('Got a response from the API'));
  return promise.then(() => ({
    status: 200,
    body: 'status',

  }
  )).catch(new Error(''));
}
