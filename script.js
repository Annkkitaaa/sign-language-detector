const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
const startButton = document.getElementById('startButton');
const detectedGestureSpan = document.getElementById('detectedGesture');

let isRunning = false;

startButton.addEventListener('click', toggleDetection);

function toggleDetection() {
    if (isRunning) {
        stopDetection();
    } else {
        startDetection();
    }
}

async function startDetection() {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        video.srcObject = stream;
        isRunning = true;
        startButton.textContent = 'Stop Detection';
        detectGestures();
    } catch (err) {
        console.error("Error accessing the camera:", err);
    }
}

function stopDetection() {
    const stream = video.srcObject;
    const tracks = stream.getTracks();
    tracks.forEach(track => track.stop());
    isRunning = false;
    startButton.textContent = 'Start Detection';
    detectedGestureSpan.textContent = 'None';
}

function detectGestures() {
    if (!isRunning) return;

    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
    
    // Send the canvas image data to the server
    const imageData = canvas.toDataURL('image/jpeg');
    
    fetch('http://localhost:5000/detect', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ image: imageData }),
    })
    .then(response => response.json())
    .then(data => {
        detectedGestureSpan.textContent = data.gesture;
    })
    .catch(error => {
        console.error('Error:', error);
    });

    requestAnimationFrame(detectGestures);
}