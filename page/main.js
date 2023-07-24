const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
const pixelSize = 10;
const paintBoard = 28;
const pixel_w = canvas.width / paintBoard;
const pixel_h = canvas.height / paintBoard;
let img = new Array(paintBoard).fill(0).map(() => new Array(paintBoard).fill(0));
let isDrawing = false;

function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    img = new Array(paintBoard).fill(0).map(() => new Array(paintBoard).fill(0));
}

function saveImage() {
    let img_saved = new Array(paintBoard).fill(0).map(() => new Array(paintBoard).fill(0));
    for (let i = 0; i < paintBoard; i++) {
        for (let j = 0; j < paintBoard; j++) {
            img_saved[i][j] = img[i][j];
        }
    }
    const dataURL = canvas.toDataURL('image/png');
    const link = document.createElement('a');
    link.href = dataURL;
    link.download = 'image.png';
    link.click();
}

function drawPixel(x, y) {
    img[x][y] = 255;
    ctx.fillStyle = 'black';
    ctx.fillRect(x * pixel_w, y * pixel_h, pixelSize, pixelSize);
}

canvas.addEventListener('mousedown', function (e) {
    isDrawing = true;
    const x = Math.floor(e.offsetX / pixel_w);
    const y = Math.floor(e.offsetY / pixel_h);
    drawPixel(x, y);
});

canvas.addEventListener('mousemove', function (e) {
    if (isDrawing) {
        const x = Math.floor(e.offsetX / pixel_w);
        const y = Math.floor(e.offsetY / pixel_h);
        drawPixel(x, y);
    }
});

canvas.addEventListener('mouseup', function (e) {
    isDrawing = false;
});

const clearBtn = document.getElementById('clearBtn');
clearBtn.addEventListener('click', clearCanvas);

const saveBtn = document.getElementById('saveBtn');
saveBtn.addEventListener('click', saveImage);
