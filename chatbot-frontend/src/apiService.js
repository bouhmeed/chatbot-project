// src/apiService.js
import axios from 'axios';

const API_URL = 'http://127.0.0.1:5000';

export const sendMessage = async (message) => {
  try {
    const response = await axios.post(`${API_URL}/message`, { message });
    return response.data;
  } catch (error) {
    console.error("Error sending message", error);
    throw error;
  }
};

export const fetchProducts = async () => {
  try {
    const response = await axios.get(`${API_URL}/products`);
    return response.data;
  } catch (error) {
    console.error("Error fetching products", error);
    throw error;
  }
};

export const fetchProductById = async (productId) => {
  try {
    const response = await axios.get(`${API_URL}/product/${productId}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching product", error);
    throw error;
  }
};
