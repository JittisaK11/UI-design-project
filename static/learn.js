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
                '<div class="instr">Click here to learn about the common tempos:</div> <button class="btn-newpage" > <a href="' + tempoURL + '"  style="color: white" >Common Tempo</a></button> </div>'
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
    const formattedText = '<ul>' + points.map(point => `<li>${point}</li>`).join('') + '</ul>';
    displayArea.innerHTML = formattedText;
}