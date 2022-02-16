import axios from 'axios';

export const getWaveform = async (file: FormData) => {
    const response = await axios.post('http://localhost:8080/spec-api/get-wav', file)
    return response.data.wav
}