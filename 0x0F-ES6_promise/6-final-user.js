import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return new Promise((resolve) => [resolve(signUpUser(firstName, lastName)),
    resolve(uploadPhoto(fileName))]).catch((error) => (error));
}
