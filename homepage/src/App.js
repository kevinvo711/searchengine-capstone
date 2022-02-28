import { useState } from "react";
import './App.css';

function App() {

  const [setQuery] = useState("");

  return (
    <div>
      <h1>Search Engine</h1>
      <label>Search</label>
      <input type = "text" onChange = {e => setQuery(e.target.value)} />
    </div>
  );
}

export default App;
