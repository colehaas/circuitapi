import React, { useEffect, useState } from "react";
import axios from "axios";

const baseurl = "/addstudy/";

export default function ShowStudy(props) {

    const [trial, setTrial] = useState(null);

    useEffect(() => {
        axios.get("/trials/").then((response) => {
            setTrial(response.data);
        });
    }, []);

    function deleteStudy(e) {
        axios.post(baseurl, {
            method: "DELETE",
            NCTId: e.target.getAttribute("id")
        });
    }

    function updateStudy(e) {
        axios.post(baseurl, {
            method: "UPDATE",
            NCTId: e.target.getAttribute("id")
        });
    }

    if (trial) {
        return (
            <ul>
            {trial.map((study) => 
                <li key={study.NCTId}>
                    <div> {study.BriefTitle} </div>
                    <div> {study.NCTId} </div>
                    <button type="submit" id = {study.NCTId} onClick = {deleteStudy}> Delete </button>
                    <button type="submit" id = {study.NCTId} onClick = {updateStudy}> Update </button>
                    
                    <br/><br/>
                </li>
            )}
            </ul>
        );
    }

}