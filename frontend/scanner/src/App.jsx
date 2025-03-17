import React, { useState } from "react";
import axios from "axios";
import './App.css'

function App() {
  const [formData, setFormData] = useState({
    location: "",
    gps_coordinates: "",
    item_name: "",
    description: "",
  });

  const [qrCodeUrl, setQrCodeUrl] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  // Handle input changes
  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };
  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");

    try {
      const response = await axios.post("http://127.0.0.1:8000/generate_qr/", formData);
      setQrCodeUrl(response.data.qr_code_url);
    } catch (err) {
      setError("Failed to generate QR code. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
  <div >
    <div className="container">
      <h2>QR Code Generator</h2>
      <form onSubmit={handleSubmit}>
        <input type="text" name="location" placeholder="Location" value={formData.location} onChange={handleChange} required />
        <input type="text" name="gps_coordinates" placeholder="GPS Coordinates" value={formData.gps_coordinates} onChange={handleChange} />
        <input type="text" name="item_name" placeholder="Item Name" value={formData.item_name} onChange={handleChange} required />
        <textarea name="description" placeholder="Description" value={formData.description} onChange={handleChange} required />
        <button type="submit" disabled={loading}>{loading ? "Generating..." : "Generate QR Code"}</button>
      </form>

      {error && <p className="error">{error}</p>}

      {qrCodeUrl && (
        <div className="qr-container">
          <h3>Generated QR Code:</h3>
          <img src={qrCodeUrl} alt="QR Code" />
        </div>
      )}
    </div>
  </div>
  )
}

export default App
