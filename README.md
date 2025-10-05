# Asteroids Game (Pygame)

## 📌 Overview
This is a simple **Asteroids** game built using **Pygame**. The player controls a spaceship, moves around the screen, and shoots asteroids while avoiding collisions. If the spaceship collides with an asteroid, the game ends.

## 🎮 Gameplay
- Control the spaceship using **W, A, S, Z** keys.
- Shoot bullets using the **SPACE** key.
- Destroy asteroids by shooting them.
- If an asteroid collides with the player, the game is over.

## 🚀 Features
✅ Player spaceship with rotation and movement
✅ Shooting bullets
✅ Randomly spawning asteroids
✅ Asteroids split when shot
✅ Collision detection (Player vs Asteroid, Bullet vs Asteroid)
✅ Frame rate controlled at 60 FPS

## 🛠️ Installation & Setup
### 1️⃣ Install Dependencies
Make sure you have Python and Pygame installed. If not, install them using:
```sh
pip install pygame
```

### 2️⃣ Clone or Download the Project
```sh
git clone https://github.com/orignlkartik1/asteroids-game.git
cd asteroids-game
```

### 3️⃣ Run the Game
```sh
python main.py
```

## 🎮 Controls
| Key | Action |
|----|---------|
| `A` | Move forward |
| `S` | Move backward |
| `W` | Rotate left |
| `Z` | Rotate right |
| `SPACE` | Shoot bullets |

## 📁 Project Structure
```
📂 asteroids-game
│-- main.py               # Main game loop
│-- constants.py          # Game settings and constants
│-- player.py             # Player (spaceship) class
│-- asteroid.py           # Asteroid class
│-- asteroidfield.py      # Spawning and managing asteroids
│-- shot.py               # Bullet (shot) mechanics
│-- circleshape.py        # Base class for circular objects
│-- README.md             # This file
```

## 🔥 Future Improvements
- **Add sound effects** (shooting, explosions, background music)
- **Better graphics** (use images instead of simple shapes)
- **Game restart screen** instead of immediate exit
- **More asteroid variations** (different sizes and speeds)
- **Add power-ups or enemies (UFOs shooting back at the player)**

## 🎯 Contributing
If you want to improve the game, feel free to submit a pull request! 🚀

## 📜 License
This project is open-source and available under the **MIT License**.

