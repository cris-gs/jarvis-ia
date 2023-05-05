import { useState } from "react";
import "./App.css";

const App = () => {
  const [isChecked, setIsChecked] = useState(false); // Estado para almacenar si el botón está chequeado
  const [jarvisResponse, setJarvisResponse] = useState(null);
  const [jarvisActive, setJarvisActive] = useState(false);
  const [facialRecognitionActive, setFacialRecognitionActive] = useState(false);

  const jarvisSay = (message) => {
    return new Promise((resolve, reject) => {
      const synth = window.speechSynthesis;
      const msg = new SpeechSynthesisUtterance(message);
      msg.lang = 'es-ES';
      // msg.pitch = 1.5;
      // msg.rate = 0.8;
      setJarvisResponse(message);
      msg.onend = () => {
        resolve();
      };
      synth.speak(msg);
    });
  };
  
  const handleSwitchChange = async () => {
    const synth = window.speechSynthesis;
    setIsChecked(!isChecked);
    if (!isChecked) {
      setJarvisActive(true);
      await jarvisSay("Hola, soy Jarvis TEC su asistente personal. ¿Qué modelo quiere usar?");
      await jarvisSay("Opciones disponibles");
      await jarvisSay("1 si quiere predecir el precio del bitcoin.");
      await jarvisSay("2 si quiere predecir el precio de un automóvil.");
      await jarvisSay("3 si quiere que le recomiende películas.");
      await jarvisSay("4 si quiere clasificar la calidad de un vino.");
      await jarvisSay("5 si quiere predecir la cantidad de inventario de una compañía.");
      await jarvisSay("6 si quiere predecir la tarifa de los viajes de taxi.");
      await jarvisSay("7 si quiere clasificar si un cliente se va a pasar de compañía celular.");
      await jarvisSay("8 si quiere predecir el delay de los viajes de avión.");
      await jarvisSay("9 si quiere predecir la masa corporal de un paciente.");
      await jarvisSay("10 si quiere predecir el precio de un aguacate.");
      await jarvisSay("Por favor, indique la opción que desea seleccionar diciendo la palabra 'opción' seguida del número correspondiente.");
      // await jarvisSay("La dejo con mi colega, ten paciencia porque es media tontita.")
      await jarvisSay("Tomando indicaciones...");
      fetch('http://127.0.0.1:5000/voice')
        .then(response => response.json())
        .then(data => {
          console.log(data);
          setJarvisResponse(data.message);
          setJarvisActive(false);
        })
        .catch(error => console.error(error));
    } else {
      synth.cancel();
      setJarvisActive(false);
    }
  };

  const handleFacialRecognition = () => {
    setFacialRecognitionActive(true);
    setIsChecked(true);
    setJarvisResponse("Escaneando rostro...");
    fetch('http://127.0.0.1:5000/face')
      .then(response => response.json())
      .then(data => {
        console.log(data);
        setJarvisResponse(data);
        setFacialRecognitionActive(false);
      })
      .catch(error => console.error(error));
  }

  return (
    <main>
      <div className="robot">
        <h1>Jarvis TEC</h1>
        <input
          type="checkbox"
          checked={isChecked}
          onChange={handleSwitchChange}
          id="switch-button"
          disabled={jarvisActive && facialRecognitionActive ? true : false}
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
          {jarvisResponse && jarvisResponse }
        </p>
      </div>
      <button className="button" onClick={handleFacialRecognition} disabled={jarvisActive || facialRecognitionActive ? true : false}>
        <img src="/src/assets/reconocimiento-facial.png" alt="Texto alternativo" />
      </button>
    </main>
  );
};

export default App;
