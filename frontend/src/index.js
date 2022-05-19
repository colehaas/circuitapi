import React from "react";
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import {
    BrowserRouter as Router,
    Routes,
    Route,
    Link
  } from "react-router-dom";

import SearchCTAPI from "./components/searchctapi"
import ShowStudy from "./components/showstudy"


const rootElement = document.getElementById("root");
const root = createRoot(rootElement);

root.render(
    <StrictMode>
        <Layout />
    </StrictMode>
);

function Layout() {
    return (
        <Router>
          <div>
            <Nav/>
            <Routes>
              <Route path="/" element = {<Search/>}>
              </Route>
              <Route path="/manage" element = {<Manage/>} >
              </Route>
            </Routes>
          </div>
        </Router>
      );
    }

function Search() {
    return(
        <div>
            <h2>Search</h2>
            <p>Search clinical trials from the ClinicalTrials.gov API and add them to the database</p>
            <SearchCTAPI />
        </div>
    );
}


function Manage() {
    return(
        <div>
            <h2>Manage</h2>
            <p>View, Update, or Delete clinical trials that are in the database</p>
            <ShowStudy/>
        </div>
    );
}

function Nav(){
    return (
        <div>
            <ul>
                <li>
                    <Link to="/">Search</Link>
                </li>
                <li>
                    <Link to="/manage">Manage</Link>
                </li>
            </ul>
            <hr />
        </div>  
    );
}
