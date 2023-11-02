function playSound(soundFile) {
    var audio = new Audio('sounds/' + soundFile);
    audio.play();
}

// Get the button container element
var buttonContainer = document.getElementById('buttonContainer');

// Fetch sound files from the GitHub API
fetch('https://api.github.com/repos/YourUsername/YourRepository/contents/sounds')
    .then(response => response.json())
    .then(files => {
        // Filter only audio files (adjust if needed)
        const soundFiles = files
            .filter(file => file.type === 'file' && file.name.endsWith('.mp3'))
            .map(file => file.name);

        // Dynamically create buttons for each sound file
        soundFiles.forEach(function(soundFile) {
            var button = document.createElement('button');
            button.className = 'sound-button';
            button.textContent = getFileNameWithoutExtension(soundFile);
            button.onclick = function() {
                playSound(soundFile);
            };
            buttonContainer.appendChild(button);
        });
    })
    .catch(error => console.error('Error fetching sound files:', error));

// Function to get the file name without the extension
function getFileNameWithoutExtension(fileName) {
    return fileName.split('.').slice(0, -1).join('.');
}
