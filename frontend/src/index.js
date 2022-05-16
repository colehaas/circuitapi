import React from "react";
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";


import Study from "./components/study"
import App from "./components/App"
//import Trial from "./components/trial"

const rootElement = document.getElementById("root");
const root = createRoot(rootElement);

root.render(
    <StrictMode>
      <Layout />
    </StrictMode>
  );

function Layout() {
    return(   
        <App/>
    )
}