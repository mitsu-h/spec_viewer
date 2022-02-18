import { shallowMount } from "@vue/test-utils";
import { getWaveform } from "../../src/utils/utils";

test("get-wav APIにPOSTして、波形を受け取る", () => {
  const formData = new FormData();
  const wav = getWaveform(formData);
  expect(typeof wav).toMatch("object");
});
