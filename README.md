# Keyboard Sight-Reading Trainer

Practice app for *Pappa's Easy Way Electronic Keyboard Method, Book 1* (treble clef, Ta / ti / Ra counting, single-finger chords).

**Live:** https://nbsmani.github.io/keyboard-trainer/

- **Cards**: spaced-repetition flashcards (notes on the staff, note values & rests, signs & terms)
- **Notes**: timed note-naming rounds, adaptive to weak notes
- **Rhythm**: generated rhythms with counts; tap along and get timing feedback
- **Sight-read**: 4-bar melodies with chord signs; count-in, playback, and scoring

## MIDI (Yamaha PSR-E383 via USB-C MIDI)
Web MIDI isn't available in Safari or any iPad browser. On iPad, open the live URL in **MIDIWeb Browser**.
With a keyboard connected, real key presses answer cards and notes, drive rhythm taps, and are scored in sight-reading.
Without MIDI everything works by touch.

## Layout
- `index.html`: built, self-contained page served by GitHub Pages (abcjs + samples inlined, ES2017)
- `src/trainer.html`: readable source
- `src/sounds/`: instrument samples (tonejs-instruments, MIT)
- `src/build.py`: rebuilds `index.html` (`cd src && npm i abcjs@6.7.2 esbuild && python3 build.py`)

Notation rendering: [abcjs](https://github.com/paulrosen/abcjs) (MIT).
