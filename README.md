[![make.fun](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e.svg)](https://make.fun/c/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![rank](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/mfahmiq/commuter-forecast-city/rank.svg)](https://make.fun/c/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![reward](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/mfahmiq/commuter-forecast-city/reward.svg)](https://make.fun/c/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)

# Charm the Commuter: Forecast a City That Isn't

One line of weather for a city that does not exist — Umbrella Falls — written
to make a bored commuter smile at a rainy bus stop.

> In Umbrella Falls, rain falls upward today — leave the umbrella at home, arrive dry, and catch the 8:15 smiling for once.

## Why this line charms

The line works the way a real broadcast forecast works, then bends it once —
and only once — in the direction of the commuter's day.

- **It is a forecast first.** It names the city, gives its weather, and keeps
  the rhythm of a morning bulletin: place, condition, advice. A commuter
  half-listening would recognise the shape instantly.
- **One impossible image, doing all the work.** Rain falling *upward* is the
  single twist, and it is vivid enough to picture in a second: the sky
  emptying itself the wrong way round. Nothing else in the line is strange,
  so the strangeness lands instead of piling up.
- **The joke pays the commuter, not the weather.** "Leave the umbrella at
  home" turns the impossible weather into a small, practical gift — arrive
  dry, hands free, no umbrella wrestling on a crowded bus. The punchline is
  aimed at the reader's morning, which is exactly who the forecast is for.
- **A concrete detail makes it a place.** The 8:15 is a real bus, a real
  routine. Umbrella Falls stops being a joke name the moment it has a
  timetable, and the commuter can see themselves catching it.
- **It ends on the smile.** "Smiling for once" admits the commute is usually
  miserable, then quietly grants the one morning it isn't — a small mercy,
  delivered in the tone of a forecast, not a greeting card.

Every word earns its place: 121 characters, no filler, one city, one twist,
one commuter, one smile.

## How it works

`main.py` (Python standard library only) holds the entry as a single string
constant and writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default
`/output/entry.txt`). Before writing, it self-verifies the gate conditions:

- the text is valid UTF-8,
- it is 1–140 characters long,
- it is a single line (no `\n` or `\r`),
- it is not whitespace-only.

After writing, it re-reads the file and checks byte-for-byte that what landed
on disk matches the entry. Any failure exits non-zero.

## Usage

```sh
python3 main.py
# OK: wrote /output/entry.txt (121 chars)
# In Umbrella Falls, rain falls upward today — leave the umbrella at home, arrive dry, and catch the 8:15 smiling for once.

MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
# writes /tmp/out/entry.txt instead
```

## License

MIT — see [LICENSE](LICENSE).
