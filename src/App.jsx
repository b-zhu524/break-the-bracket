import { useState } from "react";
import FileUploader from "./components/FileUploader";

function App() {
    return (
        <div>
            <h1>Break the Bracket</h1>
            <FileUploader />
            <FileUploader />
        </div>
    );
}

export default App;
