const chatWindow = document.getElementById("chatWindow");
const input = document.getElementById("messageInput");
const sendBtn = document.getElementById("sendBtn");

const progressBar = document.getElementById("progress-bar");
const progressText = document.getElementById("progress-text");

let questionCount = 1;
const TOTAL = 50;

function appendMessage(sender, text) {
    const div = document.createElement("div");
    div.className = sender === "user" ? "userMsg" : "botMsg";
    div.innerText = text;
    chatWindow.appendChild(div);
    chatWindow.scrollTop = chatWindow.scrollHeight;
}

function updateProgress() {
    let percent = (questionCount / TOTAL) * 100;
    progressBar.style.width = percent + "%";
    progressText.innerText = `Question ${questionCount} / ${TOTAL}`;
}

function sendMessage() {
    const msg = input.value.trim();
    if (!msg) return;

    appendMessage("user", msg);
    input.value = "";

    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: msg })
    })
    .then(res => res.json())
    .then(data => {
        appendMessage("bot", data.reply);
        questionCount++;
        if (questionCount <= TOTAL) updateProgress();
    });
}

sendBtn.onclick = sendMessage;
input.addEventListener("keypress", e => {
    if (e.key === "Enter") sendMessage();
});

// Initial greeting
appendMessage("bot", "Hello! Let's begin your diet assessment 😊");
updateProgress();
