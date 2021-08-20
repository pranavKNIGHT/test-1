import React, { useState, useEffect } from "react";
import axios from "./axios";

function FetchTodos() {
  const [todos, setTodos] = useState([]);

  useEffect(() => {
    const fetchTodos = async () => {
      const response = await axios
        .get("/todos/")
        .catch((err) => alert("api or db is down", err));
      setTodos(response.data);
    };
    fetchTodos();
  }, [todos]);
  return (
    <div>
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

export default FetchTodos;
