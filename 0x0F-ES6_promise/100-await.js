import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  let myobject;
  try {
    myobject = {
      photo: await uploadPhoto(),
      user: await createUser(),
    };
  } catch (err) {
    myobject = {
      photo: null,
      user: null,
    };
  }
  return myobject;
}
