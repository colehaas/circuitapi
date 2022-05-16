import React from "react";
import axios from "axios"

const baseURL = "/trials/"


export default function Study () {

    
    //const [trial, setTrial] = React.useState(null);

/*
    React.useEffect(() => {
        axios.get(`${baseURL}`).then((response) => {
            setTrial(response.data);
        });
    }, []);


    function studyPost() {
        axios.post(baseURL, {
            Search: "True",
            Expr: "heart+attack",
        })

        .then((response) => {
            setTrial(response.data);

    }

*/
    function studyPost() {
        axios.post(baseURL, {
            "BriefTitle": "TiReTiTle",
        })

    //if (!trial) return null;
    }
    return (
        <div>
            <button onClick={studyPost}> Create Post </button>
        </div>
    )
}