document.addEventListener("DOMContentLoaded", function () {
  const menuToggle = document.getElementById("menuToggle");
  const sidebar = document.getElementById("sidebar");
  const textInput = document.getElementById("textInput");
  const sendButton = document.getElementById("sendButton");
  const audioPlayer = document.getElementById("audioPlayer");
  const audioSource = document.getElementById("audioSource");

  // ✅ Toggle Sidebar (Menu Button Working Now)
  menuToggle.addEventListener("click", function () {
      sidebar.classList.toggle("active");
  });

  // ✅ Close sidebar when clicking outside of it
  document.addEventListener("click", function (event) {
      if (!sidebar.contains(event.target) && event.target !== menuToggle) {
          sidebar.classList.remove("active");
      }
  });

  // ✅ Text to Speech Button Click Event
  sendButton.addEventListener("click", function () {
      const text = textInput.value.trim();
      if (text === "") {
          alert("Please enter some text.");
          return;
      }

      fetch("http://127.0.0.1:5000/generate_audio", {
          method: "POST",
          headers: {
              "Content-Type": "application/json",
          },
          body: JSON.stringify({ text: text }),
      })
      .then(response => response.json())
      .then(data => {
          if (data.audio_url) {
              audioSource.src = data.audio_url;
              audioPlayer.load();
              audioPlayer.classList.remove("hidden");
          } else {
              alert("Error generating audio.");
          }
      })
      .catch(error => console.error("Error:", error));
  });
});
