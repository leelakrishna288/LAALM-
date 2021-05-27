
#Apply the createOscillator method to osc variable
let osc;
osc = audioContext.createOscillator();

#Assign the type of waveform as "sine"
osc.type = "sine";

#Apply the frequency value to 440
osc.frequency.value = 440;

#connect osc to the destination
osc.connect(audioContext.destination);

#output sound
osc.start(audioContext.currentTime);
