// Toggle sections
const textToSpeechBtn = document.getElementById("textToSpeechBtn");
const voiceCloningBtn = document.getElementById("voiceCloningBtn");
const textToSpeechSection = document.getElementById("textToSpeechSection");
const voiceCloningSection = document.getElementById("voiceCloningSection");

textToSpeechBtn.addEventListener("click", () => {
  textToSpeechSection.classList.remove("hidden");
  voiceCloningSection.classList.add("hidden");
});

voiceCloningBtn.addEventListener("click", () => {
  voiceCloningSection.classList.remove("hidden");
  textToSpeechSection.classList.add("hidden");
});

// Handle voice input selection
const voiceInput = document.getElementById("voiceInput");
const uploadVoiceSample = document.getElementById("uploadVoiceSample");
const pretrainedVoice = document.getElementById("pretrainedVoice");

voiceInput.addEventListener("change", (e) => {
  if (e.target.value === "upload") {
    uploadVoiceSample.classList.remove("hidden");
    pretrainedVoice.classList.add("hidden");
  } else {
    pretrainedVoice.classList.remove("hidden");
    uploadVoiceSample.classList.add("hidden");
  }
});

// Handle voice cloning option
const voiceCloneOption = document.getElementById("voiceCloneOption");
const uploadAudioFile = document.getElementById("uploadAudioFile");
const recordMicrophone = document.getElementById("recordMicrophone");

voiceCloneOption.addEventListener("change", (e) => {
  if (e.target.value === "upload") {
    uploadAudioFile.classList.remove("hidden");
    recordMicrophone.classList.add("hidden");
  } else {
    recordMicrophone.classList.remove("hidden");
    uploadAudioFile.classList.add("hidden");
  }
});

// Dark mode toggle
const darkModeToggle = document.getElementById("darkModeToggle");
darkModeToggle.addEventListener("click", () => {
  document.body.classList.toggle("dark-mode");
});

// Placeholder for recording and cloning functionality
const startRecordingBtn = document.getElementById("startRecordingBtn");
const stopRecordingBtn = document.getElementById("stopRecordingBtn");

startRecordingBtn.addEventListener("click", () => {
  startRecordingBtn.classList.add("hidden");
  stopRecordingBtn.classList.remove("hidden");
  // Add recording logic here
});

stopRecordingBtn.addEventListener("click", () => {
  stopRecordingBtn.classList.add("hidden");
  startRecordingBtn.classList.remove("hidden");
  // Add stop recording logic here
});
