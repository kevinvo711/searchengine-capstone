import { useState } from "react";
import TextField from "@mui/material/TextField";
import ResultList from "./Components/ResultList";
import "./App.css";

function App() {
  const [query, setQuery] = useState("");
  const [showQuery, setShowQuery] = useState(false);
  const onSubmit = () => setShowQuery(true);
  //make responsive to enter key
  const handleKeypress = (e) => {
    if (e.key === "Enter") {
      setShowQuery(true);
    }
  };
  return (
    <div classname="main">
      <h1>Search Engine</h1>
      <div className="search">
        <TextField
          onChange={(e) =>
            setQuery(e.target.value.toLowerCase(), setShowQuery(false))
          }
          label="Search"
          onKeyPress={handleKeypress}
        />
        <button onClick={onSubmit}>Search</button>
      </div>
      <div>{showQuery ? <ResultList input={query} /> : null}</div>
    </div>
  );
}

export default App;
