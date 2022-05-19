import React, {useState, useEffect} from "react";
import axios from "axios"


const baseURL = "/preview/"


export default function SearchCTAPI () {

    const [searchInput, setSearchInput] = useState('');
    const [trial, setTrial] = React.useState(null);


    function handleSearch(e) {
        e.preventDefault();
        const url = baseURL + searchInput;
        axios.get(url).then((response) => {
            setTrial(response.data);
        });
    }     

    return (
        <div>
            <form onSubmit = {handleSearch}>
                <input placeholder='Search...' value = {searchInput} onChange={(e) => setSearchInput(e.target.value)}/>
                <button type="submit">Add</button>
            </form>
            <Previews prev={trial}/>
        </div>
    )
}

    
function Previews(props) {
    const prev = props.prev;
    if (prev) {
        return(
            <div>
                <br/><br/>
                <Preview study = {prev.FullStudies}/>
            </div>
        )
    }
}

function Preview(props) {

    function createStudy(e) {
        e.preventDefault();
        axios.post("/addstudy/", {
            method: "POST",
            NCTId: e.target.getAttribute("id")
        });
    }     
    
    return (
        <ul>
        {props.study.map((study) => 
            <li key={study.Study.ProtocolSection.IdentificationModule.NCTId}>
                <div> {study.Study.ProtocolSection.IdentificationModule.BriefTitle} </div>
                <div> {study.Study.ProtocolSection.IdentificationModule.NCTId} </div>
                <button 
                    type="submit" 
                    id = {study.Study.ProtocolSection.IdentificationModule.NCTId} 
                    onClick = {createStudy}> 
                Add </button>
                <br/><br/>
            </li>
        )}
        </ul>
    )

}

