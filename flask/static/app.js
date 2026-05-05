document.getElementById('bookingForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const payload = {
    origin: document.getElementById('origin').value,
    destination: document.getElementById('destination').value,
    depart_date: document.getElementById('depart_date').value,
    return_date: document.getElementById('return_date').value,
    passengers: parseInt(document.getElementById('passengers').value, 10),
    class: document.getElementById('class').value,
    names: document.getElementById('names').value
  };

  const resultEl = document.getElementById('result');
  resultEl.innerHTML = 'Processing...';

  try {
    const res = await fetch('/book', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.error || 'Booking failed');

    resultEl.innerHTML = `<div class="alert alert-success">Booking confirmed: <strong>${data.booking_id}</strong><div class="booking-summary mt-2">${JSON.stringify(data.summary, null, 2)}</div></div>`;
  } catch (err) {
    resultEl.innerHTML = `<div class="alert alert-danger">${err.message}</div>`;
  }
});
