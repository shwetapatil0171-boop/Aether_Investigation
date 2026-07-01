const AetherBGM = (() => {
    let ctx;
    let masterGain;
    let nodes = [];
    let running = false;

    const chordNotes = [
        [110.00, 130.81, 164.81],
        [98.00, 123.47, 146.83],
        [110.00, 130.81, 164.81],
        [87.31, 110.00, 130.81],
    ];
    let chordIndex = 0;
    let chordTimer = null;

    function getCtx() {
        if (!ctx) ctx = new (window.AudioContext || window.webkitAudioContext)();
        return ctx;
    }

    function playChord(freqs) {
        const audioCtx = getCtx();
        const now = audioCtx.currentTime;
        const chordGain = audioCtx.createGain();
        chordGain.gain.value = 0;
        chordGain.connect(masterGain);

        freqs.forEach((freq) => {
            const osc = audioCtx.createOscillator();
            osc.type = "sine";
            osc.frequency.value = freq;

            const lfo = audioCtx.createOscillator();
            lfo.frequency.value = 0.1 + Math.random() * 0.1;
            const lfoGain = audioCtx.createGain();
            lfoGain.gain.value = 2;
            lfo.connect(lfoGain);
            lfoGain.connect(osc.frequency);
            lfo.start(now);

            osc.connect(chordGain);
            osc.start(now);

            nodes.push(osc, lfo);
        });

        chordGain.gain.linearRampToValueAtTime(0.15, now + 2);
        chordGain.gain.linearRampToValueAtTime(0.15, now + 6);
        chordGain.gain.linearRampToValueAtTime(0, now + 8);

        nodes.push(chordGain);
    }

    function loop() {
        if (!running) return;
        playChord(chordNotes[chordIndex]);
        chordIndex = (chordIndex + 1) % chordNotes.length;
        chordTimer = setTimeout(loop, 6000);
    }

    function start() {
        const audioCtx = getCtx();
        if (audioCtx.state === "suspended") {
            audioCtx.resume();
        }
        if (running) return;
        if (!masterGain) {
            masterGain = audioCtx.createGain();
            masterGain.gain.value = 1;
            masterGain.connect(audioCtx.destination);
        }
        running = true;
        loop();
    }

    function stop() {
        running = false;
        if (chordTimer) clearTimeout(chordTimer);
        nodes.forEach(n => {
            try { n.stop && n.stop(); } catch (e) {}
            try { n.disconnect(); } catch (e) {}
        });
        nodes = [];
    }

    function setMuted(muted) {
        if (!masterGain) return;
        masterGain.gain.value = muted ? 0 : 1;
    }

    return { start, stop, setMuted };
})();

document.addEventListener("DOMContentLoaded", () => {
    const isMuted = sessionStorage.getItem("aether_bgm_muted") === "true";

    const btn = document.createElement("button");
    btn.id = "bgm-toggle";
    btn.textContent = isMuted ? "🔇 Music Off" : "🔊 Music On";
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

    let started = false;
    function tryStart() {
        if (started) return;
        started = true;
        AetherBGM.start();
        AetherBGM.setMuted(isMuted);
        document.removeEventListener("click", tryStart);
    }
    document.addEventListener("click", tryStart);

    btn.addEventListener("click", (e) => {
        e.stopPropagation();
        if (!started) tryStart();
        const currentlyMuted = sessionStorage.getItem("aether_bgm_muted") === "true";
        const newMuted = !currentlyMuted;
        sessionStorage.setItem("aether_bgm_muted", newMuted);
        AetherBGM.setMuted(newMuted);
        btn.textContent = newMuted ? "🔇 Music Off" : "🔊 Music On";
    });
});
