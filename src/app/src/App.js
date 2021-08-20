import axios from "./axios";
import React, { useState, useEffect } from "react";
import "./App.css";
import FetchTodos from "./FetchTodos";

export function App() {
  const [input, setInput] = useState("");

  const addTodo = (event) => {
    event.preventDefault();
    axios
      .post("http://localhost:8000/todos/", {
        title: input,
      })
      .catch((err) => console.log(err));

    setInput("");
  };
  // console.log(todos);
  return (
    <div className="App">
      <div>
        <h1>Add a ToDo</h1>
        <form>
          <div>
            <label htmlFor="todo">ToDo: </label>
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
            />
          </div>
          <div>
            <button disabled={!input} type="submit" onClick={addTodo}>
              Add a ToDo
            </button>
          </div>
        </form>
      </div>
      <FetchTodos />
    </div>
  );
}

export default App;
