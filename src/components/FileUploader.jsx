import { useState } from "react";
import axios from "axios";

export default function FileUploader() {
    const [file, setFile] = useState(null);
    const [progress, setProgress] = useState({ started: false, pc: 0 });
    const [msg, setMsg] = useState(null);

    function handleUpload() {
        if (!file) {
            setMsg("No file selected");
            return;
        }

        const formData = new FormData();
        formData.append("file", file);

        setMsg("uploading...");
        fetch("http://httpbin.org/post", {
            method: "POST",
            body: formData,
            headers: {
                "Custom-Header": "Value",
            },
        })
            .then((res) => {
                if (!res.ok) {
                    throw new Error("Bad response");
                }
                setMsg("Upload successful");
                return res.json();
            })
            .then((data) => console.log(data))
            .catch((err) => {
                setMsg("Upload failed");
                console.error(err);
            });
    }
    return (
        <div>
            <input onChange={(e) => setFile(e.target.files[0])} type="file" />
            <button onClick={handleUpload}>Upload</button>

            {/* {progress.started && (
                <progress max="100" value={progress.pc}></progress>
            )} */}
            {msg && <span>{msg}</span>}
        </div>
    );
}
