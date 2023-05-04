import { useState } from "react";
import "./App.css";

const App = () => {
  const [isChecked, setIsChecked] = useState(false); // Estado para almacenar si el botón está chequeado

  const handleSwitchChange = () => {
    if ( !isChecked ) {
      fetch('http://127.0.0.1:5000');
    }
    setIsChecked(!isChecked); // Actualizar el estado al cambiar el valor del interruptor
  };

  return (
    <main>
      <div className="robot">
        <h1>Jarvis TEC</h1>
        <input
          type="checkbox"
          checked={isChecked}
          onChange={handleSwitchChange}
          id="switch-button"
        />
        <label htmlFor="switch-button">
          <div className="switch">
            <p>{isChecked ? "ON" : "OFF"}</p>
          </div>
        </label>
        <div className="face"></div>
        <div className="head"></div>
        <div className="body"></div>
        <div className="left-hand"></div>
        <div className="right-hand"></div>
        <div className="eye1"></div>
        <div className="eye2"></div>
        <p className="bubble-bottom">
          Hola, soy Jarvis TEC su asistente personal. ¿Qué modelo quiere usar?
        </p>
      </div>
    </main>
  );
};

export default App;
