import { useState } from "react";

export const Modal = ({ isOpen, onClose }) => {
    const [inputValue, setInputValue] = useState('');

    const handleInputChange = (e) => {
        setInputValue(e.target.value);
    };

    const handleSubmit = () => {
        // Aquí puedes realizar alguna acción con el valor del campo de texto
        console.log('Valor del campo de texto:', inputValue);
        localStorage.setItem('videoUrl', inputValue);
        setInputValue('');
        // Cerrar el modal
        onClose();
    };

    if (!isOpen) {
        return null;
    }

    return (
        <div className="modal">
        <div className="modal-content">
            <h2>Url del video</h2>
            <input
            type="text"
            value={inputValue}
            onChange={handleInputChange}
            placeholder="Ingresa la url del video"
            />
            <div className="modal-buttons">
                <button className="save-button" onClick={handleSubmit}>Escanear</button>
                <button className="close-button" onClick={onClose}>Cerrar</button>
            </div>
        </div>
        </div>
    )
}
