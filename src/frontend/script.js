document.addEventListener("DOMContentLoaded", function () {
  const menuToggle = document.getElementById("menuToggle");
  const sidebar = document.getElementById("sidebar");
  const textInput = document.getElementById("textInput");
  const sendButton = document.getElementById("sendButton");
  const audioPlayer = document.getElementById("audioPlayer");
  const audioSource = document.getElementById("audioSource");
  const menuDialog = document.getElementById("menuDialog");
  const closeBtn = document.querySelector(".close-btn");
  const darkModeToggle = document.getElementById("darkModeToggle");
  
  // ✅ Open Menu Dialog
  menuToggle.addEventListener("click", function () {
    menuDialog.style.display = "block";
});

// ✅ Close Menu Dialog
closeBtn.addEventListener("click", function () {
    menuDialog.style.display = "none";
});

// ✅ Close Dialog When Clicking Outside
window.addEventListener("click", function (event) {
    if (event.target === menuDialog) {
        menuDialog.style.display = "none";
    }
});

// ✅ Dark Mode Toggle (Saves State in Local Storage)
if (localStorage.getItem("darkMode") === "enabled") {
    document.body.classList.add("dark-mode");
    darkModeToggle.checked = true;
}

darkModeToggle.addEventListener("change", function () {
    document.body.classList.toggle("dark-mode");
    if (document.body.classList.contains("dark-mode")) {
        localStorage.setItem("darkMode", "enabled");
    } else {
        localStorage.setItem("darkMode", "disabled");
    }
});
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
