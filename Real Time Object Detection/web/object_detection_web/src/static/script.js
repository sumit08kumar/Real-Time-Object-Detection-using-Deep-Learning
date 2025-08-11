document.addEventListener("DOMContentLoaded", () => {
    const imageUpload = document.getElementById("imageUpload");
    const detectButton = document.getElementById("detectButton");
    const imageCanvas = document.getElementById("imageCanvas");
    const resultsPre = document.getElementById("results");
    const ctx = imageCanvas.getContext("2d");

    let uploadedImage = null;

    imageUpload.addEventListener("change", (event) => {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = (e) => {
                uploadedImage = new Image();
                uploadedImage.onload = () => {
                    // Clear previous drawings
                    ctx.clearRect(0, 0, imageCanvas.width, imageCanvas.height);

                    // Set canvas dimensions to image dimensions
                    imageCanvas.width = uploadedImage.width;
                    imageCanvas.height = uploadedImage.height;

                    // Draw the image on the canvas
                    ctx.drawImage(uploadedImage, 0, 0);
                    resultsPre.textContent = ""; // Clear previous results
                };
                uploadedImage.src = e.target.result;
            };
            reader.readAsDataURL(file);
        }
    });

    detectButton.addEventListener("click", async () => {
        if (uploadedImage) {
            // Convert canvas content to base64 image
            const imageDataUrl = imageCanvas.toDataURL("image/jpeg");

            try {
                const response = await fetch("/api/detect", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({ image: imageDataUrl }),
                });

                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }

                const data = await response.json();
                resultsPre.textContent = JSON.stringify(data.detections, null, 2);

                // Draw bounding boxes on the image
                ctx.drawImage(uploadedImage, 0, 0); // Redraw original image
                data.detections.forEach(detection => {
                    const [x1, y1, x2, y2] = detection.bbox;
                    const label = detection.class;
                    const confidence = detection.confidence.toFixed(2);

                    ctx.beginPath();
                    ctx.rect(x1, y1, x2 - x1, y2 - y1);
                    ctx.lineWidth = 2;
                    ctx.strokeStyle = "red";
                    ctx.fillStyle = "red";
                    ctx.stroke();

                    ctx.font = "18px Arial";
                    ctx.fillText(`${label} (${confidence})`, x1, y1 > 10 ? y1 - 5 : y1 + 20);
                });

            } catch (error) {
                console.error("Error during detection:", error);
                resultsPre.textContent = `Error: ${error.message}`;
            }
        } else {
            alert("Please upload an image first.");
        }
    });
});


