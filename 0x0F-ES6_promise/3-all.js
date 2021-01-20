import uploadPhoto from "./utils";
import createUser from "./utils";

export default function handleProfileSignup() {
    Promise.all([uploadPhoto, createUser]).then((elements) => {
        console.log(elements[0]);
    })
}
