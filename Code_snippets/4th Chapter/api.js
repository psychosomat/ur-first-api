const API_BASE_URL = 'http://127.0.0.1:8080';

async function apiRequest(endpoint, options = {}) {
    const url = `${API_BASE_URL}${endpoint}`;

    try {
        const response = await fetch(url, options);

        const contentType = response.headers.get('content-type');
        if (!contentType || !contentType.includes('application/json')) {
            if (response.status === 204) return null;

            throw new TypeError(`Received non-JSON response from server: ${response.statusText}`);
        }

        const data = await response.json();

        if (!response.ok) {
            const errorMessage = data.detail || `HTTP error! Status: ${response.status}`;
            throw new Error(errorMessage);
        }

        return data;

    } catch (error) {
        console.error(`API request error to ${endpoint}:`, error);
        throw error;
    }
}
