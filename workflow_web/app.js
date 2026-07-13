const state = {
  jobId: null,
  pollTimer: null,
  previewKind: "tex",
  latestJob: null,
};

const els = {
  jobDescription: document.querySelector("#jobDescription"),
  feedback: document.querySelector("#feedback"),
  compilePdf: document.querySelector("#compilePdf"),
  revisionAttempts: document.querySelector("#revisionAttempts"),
  generateBtn: document.querySelector("#generateBtn"),
  feedbackBtn: document.querySelector("#feedbackBtn"),
  refreshBtn: document.querySelector("#refreshBtn"),
  copyLatexBtn: document.querySelector("#copyLatexBtn"),
  globalStatus: document.querySelector("#globalStatus"),
  jobIdLabel: document.querySelector("#jobIdLabel"),
  runMessage: document.querySelector("#runMessage"),
  stepList: document.querySelector("#stepList"),
  outputLinks: document.querySelector("#outputLinks"),
  preview: document.querySelector("#preview"),
  tabs: document.querySelectorAll(".tab"),
  nodes: document.querySelectorAll(".node"),
};

function setBusy(isBusy) {
  els.generateBtn.disabled = isBusy;
  els.feedbackBtn.disabled = isBusy || !state.jobId || !state.latestJob?.output_dir;
  els.refreshBtn.disabled = !state.jobId;
  els.copyLatexBtn.disabled = isBusy || !state.latestJob?.files?.tex;
}

async function api(path, options = {}) {
  const response = await fetch(path, {
    headers: { "Content-Type": "application/json" },
    ...options,
  });
  const payload = await response.json();
  if (!response.ok) {
    throw new Error(payload.error || "Request failed");
  }
  return payload;
}

function fileUrl(path) {
  return `/api/file?path=${encodeURIComponent(path)}`;
}

function setStage(stage, status) {
  els.nodes.forEach((node) => {
    const nodeStage = node.dataset.stage;
    node.classList.toggle("active", nodeStage === stage && status === "running");
    node.classList.toggle("error", nodeStage === "error" && status === "error");
    node.classList.toggle("done", status === "done" && nodeStage !== "error");
  });
}

function renderSteps(steps = []) {
  els.stepList.innerHTML = "";
  steps.forEach((step) => {
    const li = document.createElement("li");
    li.textContent = step;
    els.stepList.appendChild(li);
  });
}

function renderOutputs(files = {}) {
  const entries = [
    ["pdf", "PDF", "Open compiled resume"],
    ["tex", "LaTeX", "Open LaTeX source"],
    ["rules", "Rule Check", "Inspect validation"],
    ["content", "Resume JSON", "Inspect structured content"],
    ["evidence", "Evidence Rationale", "Inspect selected evidence"],
    ["feedback", "Latest Feedback", "Review submitted notes"],
    ["compile_log", "Compile Log", "Inspect PDF compilation"],
  ].filter(([key]) => files[key]);

  if (!entries.length) {
    els.outputLinks.innerHTML = "<p>No files yet. Run the workflow to generate outputs.</p>";
    return;
  }

  els.outputLinks.innerHTML = "";
  entries.forEach(([key, label, hint]) => {
    const link = document.createElement("a");
    link.href = fileUrl(files[key]);
    link.target = "_blank";
    link.rel = "noreferrer";
    link.innerHTML = `<strong>${label}</strong><span>${hint}</span>`;
    els.outputLinks.appendChild(link);
  });
}

async function renderPreview(files = {}) {
  const selected = files[state.previewKind] || files.tex || files.rules;
  if (!selected) {
    els.preview.textContent = "Output preview will appear here.";
    return;
  }
  try {
    const response = await fetch(fileUrl(selected));
    els.preview.textContent = await response.text();
  } catch (error) {
    els.preview.textContent = error.message;
  }
}

function renderJob(job) {
  state.latestJob = job;
  const isBusy = job.status === "running" || job.status === "queued";
  els.globalStatus.textContent = job.status || "Idle";
  els.jobIdLabel.textContent = job.id ? `Run ${job.id}` : "No active run";
  els.runMessage.textContent = job.message || "Ready.";
  setStage(job.stage, job.status);
  renderSteps(job.steps || []);
  renderOutputs(job.files || {});
  renderPreview(job.files || {});
  setBusy(isBusy);
}

async function copyLatex() {
  const texPath = state.latestJob?.files?.tex;
  if (!texPath) return;
  const original = els.copyLatexBtn.textContent;
  try {
    const response = await fetch(fileUrl(texPath));
    const latex = await response.text();
    await navigator.clipboard.writeText(latex);
    els.copyLatexBtn.textContent = "Copied";
    window.setTimeout(() => {
      els.copyLatexBtn.textContent = original;
    }, 1400);
  } catch (error) {
    els.copyLatexBtn.textContent = "Copy failed";
    els.runMessage.textContent = `Could not copy LaTeX: ${error.message}`;
    window.setTimeout(() => {
      els.copyLatexBtn.textContent = original;
    }, 1800);
  }
}

async function pollJob() {
  if (!state.jobId) return;
  try {
    const job = await api(`/api/jobs/${state.jobId}`);
    renderJob(job);
    if (job.status === "running" || job.status === "queued") {
      state.pollTimer = window.setTimeout(pollJob, 2500);
    }
  } catch (error) {
    els.runMessage.textContent = error.message;
    setBusy(false);
  }
}

function startPolling(job) {
  state.jobId = job.id;
  renderJob(job);
  if (state.pollTimer) window.clearTimeout(state.pollTimer);
  state.pollTimer = window.setTimeout(pollJob, 800);
}

els.generateBtn.addEventListener("click", async () => {
  try {
    setBusy(true);
    const job = await api("/api/jobs", {
      method: "POST",
      body: JSON.stringify({
        job_description: els.jobDescription.value,
        compile_pdf: els.compilePdf.checked,
        revision_attempts: Number(els.revisionAttempts.value || 2),
      }),
    });
    startPolling(job);
  } catch (error) {
    els.runMessage.textContent = error.message;
    setBusy(false);
  }
});

els.feedbackBtn.addEventListener("click", async () => {
  if (!state.jobId) return;
  try {
    setBusy(true);
    const job = await api(`/api/jobs/${state.jobId}/feedback`, {
      method: "POST",
      body: JSON.stringify({
        feedback: els.feedback.value,
        revision_attempts: Number(els.revisionAttempts.value || 2),
      }),
    });
    startPolling(job);
  } catch (error) {
    els.runMessage.textContent = error.message;
    setBusy(false);
  }
});

els.refreshBtn.addEventListener("click", pollJob);
els.copyLatexBtn.addEventListener("click", copyLatex);

els.tabs.forEach((tab) => {
  tab.addEventListener("click", () => {
    els.tabs.forEach((item) => item.classList.remove("active"));
    tab.classList.add("active");
    state.previewKind = tab.dataset.preview;
    renderPreview(state.latestJob?.files || {});
  });
});

setBusy(false);
