document.addEventListener("DOMContentLoaded", () => {

    const audio = new Audio(document.body.getAttribute("data-bgm-src"));

    audio.loop = true;
    audio.volume = 0.4;

    // Restore previous playback position
    const savedTime = localStorage.getItem("aether_music_time");
    if (savedTime) {
        audio.currentTime = parseFloat(savedTime);
    }

    let musicOn = sessionStorage.getItem("aether_music_on") === "true";

    const btn = document.createElement("button");
    btn.id = "bgm-toggle";
    btn.textContent = musicOn ? "🔊 Music On" : "🔇 Music Off";

    btn.style.position = "fixed";
    btn.style.bottom = "16px";
    btn.style.right = "16px";
    btn.style.zIndex = "9999";
    btn.style.padding = "8px 14px";
    btn.style.borderRadius = "20px";
    btn.style.border = "none";
    btn.style.background = "#1e293b";
    btn.style.color = "white";
    btn.style.fontSize = "13px";
    btn.style.cursor = "pointer";
    btn.style.boxShadow = "0 0 10px rgba(0,0,0,0.4)";

    document.body.appendChild(btn);

    // Save playback position every second
    setInterval(() => {
        if (!audio.paused) {
            localStorage.setItem("aether_music_time", audio.currentTime);
        }
    }, 1000);

    if (musicOn) {
        audio.play().catch(() => {});
    }

    btn.addEventListener("click", (e) => {

        e.stopPropagation();

        musicOn = !musicOn;

        sessionStorage.setItem("aether_music_on", musicOn);

        if (musicOn) {
            audio.play();
            btn.textContent = "🔊 Music On";
        } else {
            audio.pause();
            btn.textContent = "🔇 Music Off";
        }

    });

});
