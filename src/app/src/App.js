import axios from "./axios";
import React, { useState, useEffect } from "react";
import "./App.css";

export function App() {
  const [input, setInput] = useState("");
  const [todos, setTodos] = useState([]);

  useEffect(() => {
    const fetchTodos = async () => {
      const response = await axios.get("/todos/");
      setTodos(response.data);
    };
    fetchTodos();
  }, []);

  const addTodo = (event) => {
    event.preventDefault();
    axios
      .post("http://localhost:8000/todos/", {
        title: input,
      })
      .catch((err) => console.log(err));

    todos.push({
      title: input,
    });

    setInput("");
  };
  console.log(todos);
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
            <button type="submit" onClick={addTodo}>
              Add a ToDo
            </button>
          </div>
        </form>
      </div>
      <div>
        <h1>List of TODOs</h1>
      </div>
      {todos.map((todo, index) => {
        return (
          <p className="app__todoList" key={index}>
            {todo.title}
          </p>
        );
      })}
    </div>
  );
}

export default App;
