import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  await new Promise((resolve) => [resolve(signUpUser(firstName, lastName)),
    resolve(uploadPhoto(fileName))]).catch((error) => (error));
}
