import axios from "axios";

export const getWaveform = async (file: FormData) => {
  console.log("get waveform!");
  const response = await axios.post(
    "http://localhost:8080/spec-api/get-wav",
    file
  );
  return response.data.wav;
};
