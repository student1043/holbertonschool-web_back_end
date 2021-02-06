import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function asyncUploadUser() {
    let myobject
    try{(myobject = { photo: await uploadPhoto(),
        user: await signUpUser()}).catch(myobject = { photo: null,
        user: null})
        return myobject
    }
}
