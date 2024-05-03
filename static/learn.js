document.addEventListener('DOMContentLoaded', () => {
    console.log('DOM fully loaded and parsed');

    const button1 = document.getElementById('button1');
    const button2 = document.getElementById('button2');
    const button3 = document.getElementById('button3');

    if (button1 && button2 && button3) {
        button1.addEventListener('click', () => displayText([
            'The <strong>beat</strong> is the basic unit of time in music, providing the steady pulse that underpins the rhythm.',
            'You can think of it as the music\'s <strong>heartbeat</strong>, regularly spaced to provide the foundation for the patterns that are built on top.',
            'When you tap your feet to a song, you are most likely tapping to the <strong>beat</strong>.'
        ]));
        button2.addEventListener('click', () => {
            displayText([
            '<strong>Tempo</strong> refers to the speed or pace of a given piece of music, essentially determining how fast or slow the beat is.',
            'It is typically measured in <strong>beats per minute (BPM)</strong>, with a higher BPM indicating a faster tempo.',
            'The tempo sets the overall <strong>energy level</strong> of the music and can significantly affect the mood and feel of a piece.',

            '<br><br><button class="learn-more" id="commonTemposButton">Learn about Common Tempos</button>'

            ]);
        });
        button3.addEventListener('click', () => displayText([
            '<strong>Rhythm</strong> is the pattern of sounds and silences in time.',
            'It involves the arrangement of musical events (notes, chords, and rests) in time, creating patterns within the flow of the music.'
        ]));
    } else {
        console.log('One or more buttons are undefined');
    }
});

function displayText(points) {
    const displayArea = document.getElementById('display-area');
    let formattedText = '<ul>';
    
    points.forEach(point => {
        // Check if the point is the button element
        if (point.includes('button class="learn-more"')) {
            formattedText += point; // Append without wrapping in <li>
        } else {
            formattedText += `<li>${point}</li>`; // Wrap normal points in <li>
        }
    });

    formattedText += '</ul>';
    displayArea.innerHTML = formattedText;

    const commonTemposButton = document.getElementById('commonTemposButton');
    if (commonTemposButton) {
        commonTemposButton.addEventListener('click', displayCommonTempos);
    }
}

function displayCommonTempos() {
    const htmlContent = `
        <div class="container">
            <h1>Common Tempos</h1>
            <p>There are standard tempo terms that are used in music. They let us know the general pace of the piece of music.
            Tempo terms are typically conveyed through Italian words, and can be specified by a certain beats per minute (BPM) range.
            Learn some common ones here:</p>
            <div class="grid-container">
            <div class="grid-item" style="color: black;">Adagio 55–65 BPM
                <audio controls src="/static/adagio_56bpm.m4a">
                    Your browser does not support the audio element.
                </audio>
            </div>
            <div class="grid-item" style="color: black;">Andante 73-77 BPM
                <audio controls src="/static/andante_86bpm.m4a">
                    Your browser does not support the audio element.
                </audio>
            </div>
            <div class="grid-item" style="color: black;">Allegro 120–156 BPM
                <audio controls src="/static/allegro_120bpm.m4a">
                Your browser does not support the audio element.
                </audio>
            </div>
    `;
    const displayArea = document.getElementById('display-area');
    displayArea.innerHTML += htmlContent;
}


document.addEventListener("DOMContentLoaded", function() {
    const currentLocation = location.href;
    const menuItems = document.querySelectorAll('.navbar .item');
    const menuLength = menuItems.length;

    for (let i = 0; i < menuLength; i++) {
        // This checks if the link is part of the current URL
        if (currentLocation.includes(menuItems[i].href)) {
            menuItems[i].classList.add("active");
        }
    }
});