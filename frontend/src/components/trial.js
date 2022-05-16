import React from "react";
import axios from "axios"

const baseurl = "/trials"


export default function Trial () {
    const [trial, setTrial] = React.useState(null);

    React.useEffect(() => {
        axios.get(baseurl).then((response) => {
            setTrial(response.data);
        });
    }, []);

    if (!trial) return null;


    return (
        <div>
            <h1> {trial[0].BriefTitle} </h1>
        </div>
    )
}