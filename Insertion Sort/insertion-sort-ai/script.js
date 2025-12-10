const inputEl = document.getElementById('array-input');
const runBtn = document.getElementById('run-btn');
const statusText = document.getElementById('status-text');
const errorText = document.getElementById('error-text');
const stepsList = document.getElementById('steps-list');
const sortedPill = document.getElementById('sorted-pill');
const resultCard = document.getElementById('result-card');
const infoCard = document.getElementById('info-card');
const layout = document.getElementById('layout');
const stepsContent = document.getElementById('steps-content');
const infoContent = document.getElementById('info-content');
const stepsToggle = document.getElementById('steps-toggle');
const infoToggle = document.getElementById('info-toggle');

const MOBILE_BREAKPOINT = 960;

function setCollapsed(targetEl, toggleEl, collapsed) {
  if (!targetEl || !toggleEl) return;
  if (collapsed) {
    targetEl.classList.add('collapsed');
    toggleEl.textContent = 'Show';
    toggleEl.setAttribute('aria-expanded', 'false');
  } else {
    targetEl.classList.remove('collapsed');
    toggleEl.textContent = 'Hide';
    toggleEl.setAttribute('aria-expanded', 'true');
  }
}

function isMobile() {
  return window.innerWidth <= MOBILE_BREAKPOINT;
}

function ensureDesktopExpanded() {
  if (!isMobile()) {
    setCollapsed(stepsContent, stepsToggle, false);
    setCollapsed(infoContent, infoToggle, false);
  }
}

function parseArray(text) {
  const parts = text.split(',').map(s => s.trim()).filter(Boolean);
  if (!parts.length) throw new Error('Enter at least one number.');
  const nums = parts.map(n => Number(n));
  if (nums.some(n => Number.isNaN(n))) throw new Error('Use only numbers separated by commas.');
  return nums;
}

function insertionSortWithSteps(arr) {
  const steps = [];
  const a = [...arr];

  for (let i = 1; i < a.length; i++) {
    const key = a[i];
    let j = i - 1;

    steps.push({
      type: 'pick',
      message: `Pick element ${key} at index ${i}.`,
      array: [...a]
    });

    while (j >= 0 && a[j] > key) {
      steps.push({
        type: 'compare',
        message: `Compare ${a[j]} > ${key} ⇒ shift ${a[j]} right.`,
        array: [...a],
      });
      a[j + 1] = a[j];
      steps.push({
        type: 'shift',
        message: `Shifted ${a[j]} to position ${j + 1}.`,
        array: [...a],
      });
      j--;
    }

    a[j + 1] = key;
    steps.push({
      type: 'insert',
      message: `Insert ${key} at position ${j + 1}.`,
      array: [...a],
    });
  }
  return { sorted: a, steps };
}

function renderSteps(steps) {
  stepsList.innerHTML = '';
  steps.forEach((step, idx) => {
    const div = document.createElement('div');
    div.className = 'step';
    div.innerHTML = `<div class="muted">Step ${idx + 1} — ${step.type}</div>
      <div>${step.message}</div>
      <div class="muted">State: [${step.array.join(', ')}]</div>`;
    stepsList.appendChild(div);
  });
}

function handleSort() {
  errorText.textContent = '';
  statusText.textContent = 'Running insertion sort…';

  try {
    const arr = parseArray(inputEl.value);
    const { sorted, steps } = insertionSortWithSteps(arr);
    sortedPill.textContent = `[ ${sorted.join(', ')} ]`;
    renderSteps(steps);
    if (resultCard) resultCard.classList.remove('hidden');
    if (infoCard) infoCard.classList.remove('hidden');
    if (layout) layout.classList.remove('single');
    ensureDesktopExpanded();
    statusText.textContent = 'Sorted successfully. See each step below.';
  } catch (err) {
    errorText.textContent = err.message;
    statusText.textContent = `Error: ${err.message}`;
  }
}

runBtn.addEventListener('click', handleSort);

inputEl.addEventListener('keydown', (e) => {
  if (e.key === 'Enter') {
    e.preventDefault();
    handleSort();
  }
});

function setupToggles() {
  if (stepsToggle) {
    stepsToggle.addEventListener('click', () => {
      if (!isMobile()) return ensureDesktopExpanded();
      const shouldCollapse = stepsContent && !stepsContent.classList.contains('collapsed');
      setCollapsed(stepsContent, stepsToggle, shouldCollapse);
    });
  }
  if (infoToggle) {
    infoToggle.addEventListener('click', () => {
      if (!isMobile()) return ensureDesktopExpanded();
      const shouldCollapse = infoContent && !infoContent.classList.contains('collapsed');
      setCollapsed(infoContent, infoToggle, shouldCollapse);
    });
  }
  window.addEventListener('resize', ensureDesktopExpanded);
  ensureDesktopExpanded();
}

setupToggles();
