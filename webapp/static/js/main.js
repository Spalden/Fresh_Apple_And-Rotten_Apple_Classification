const form = document.getElementById("upload-form");

if (form) {
  const input = document.getElementById("file-input");
  const btn = document.getElementById("submit-btn");
  const status = document.getElementById("status");
  const result = document.getElementById("result");
  const list = document.getElementById("detections");
  const canvas = document.getElementById("canvas");
  const ctx = canvas.getContext("2d");

  const COLORS = { fresh_apple: "#2f7d32", rotten_apple: "#c62828" };

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const file = input.files[0];
    if (!file) return;

    btn.disabled = true;
    status.textContent = "Analyzing...";
    result.classList.add("hidden");

    const body = new FormData();
    body.append("file", file);

    try {
      const res = await fetch("/api/predict", { method: "POST", body });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || "Request failed");

      await draw(file, data);
      render(data);
      status.textContent = "";
      result.classList.remove("hidden");
    } catch (err) {
      status.textContent = err.message;
    } finally {
      btn.disabled = false;
    }
  });

  function draw(file, data) {
    return new Promise((resolve) => {
      const img = new Image();
      img.onload = () => {
        canvas.width = img.width;
        canvas.height = img.height;
        ctx.drawImage(img, 0, 0);
        ctx.lineWidth = Math.max(2, img.width / 200);
        ctx.font = `${Math.max(14, img.width / 40)}px sans-serif`;

        data.detections.forEach((d) => {
          const [x1, y1, x2, y2] = d.bbox;
          const color = COLORS[d.label] || "#1565c0";
          ctx.strokeStyle = color;
          ctx.fillStyle = color;
          ctx.strokeRect(x1, y1, x2 - x1, y2 - y1);
          ctx.fillText(`${d.label} ${(d.confidence * 100).toFixed(0)}%`, x1 + 4, Math.max(16, y1 - 6));
        });
        resolve();
      };
      img.src = URL.createObjectURL(file);
    });
  }

  function render(data) {
    list.innerHTML = "";
    if (data.count === 0) {
      list.innerHTML = "<li>No apples detected.</li>";
      return;
    }
    data.detections.forEach((d) => {
      const li = document.createElement("li");
      li.textContent = `${d.label} - ${(d.confidence * 100).toFixed(1)}%`;
      list.appendChild(li);
    });
  }
}
