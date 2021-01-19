export default function handleResponseFromAPI(promise) {
  return promise.then(() => ({
    status: 200,
    body: 'status',
  })).catch(new Error(''))
    .finally('Got a response from the API');
}
