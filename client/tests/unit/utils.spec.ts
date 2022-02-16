import { shallowMount } from "@vue/test-utils";
import { getWaveform } from "../../src/utils/utils"


test('get-wav APIにPOSTして、波形を受け取る', () => {
    const wav = getWaveform()
    expect(typeof (wav)).toMatch('object')
})