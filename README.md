# 🎮 Catch the Diamonds!

A fun and simple 2D game built using Python and PyOpenGL. In this game, diamonds fall from the top of the screen, and your goal is to catch them using a catcher controlled by the keyboard. The game uses the **Midpoint Line Drawing Algorithm** with zone conversions to render all shapes, making it a great educational project for learning computer graphics fundamentals.

---

## 🚀 Features

- 🎯 Midpoint Line Drawing Algorithm with zone conversion for all graphics
- 💎 Falling diamond mechanic with increasing speed
- 🕹️ Player-controlled catcher (keyboard & arrow keys)
- ⏸️ Pause/Resume functionality
- 🔁 Restart button
- ❌ Exit button
- 📈 Score tracking
- 🎨 All game objects rendered using `GL_POINTS` and manual line drawing

---

## 📷 Gameplay Preview

![screenshot-placeholder](https://via.placeholder.com/800x600.png?text=Catch+the+Diamonds+Game+Screenshot)

---

## 🧠 Concepts Used

- **OpenGL (PyOpenGL + GLUT)**
- **Midpoint Line Drawing Algorithm**
- **Zone transformation for accurate line rendering**
- **Basic 2D game logic**
- **Keyboard and Mouse Interaction**

---

## 🎮 Controls

| Action             | Key            |
|--------------------|----------------|
| Move Left          | `A` or `←`     |
| Move Right         | `D` or `→`     |
| Pause/Resume       | Click Yellow Button (Top Center) |
| Restart Game       | Click Blue Button (Top Left)     |
| Exit Game          | Click Red Button (Top Right)     |

---

## 🛠️ Installation & Run

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Anzal-abir/catch-the-diamonds.git
   cd catch-the-diamonds
Install Dependencies: Make sure Python is installed. Then install PyOpenGL:

bash
pip install PyOpenGL PyOpenGL_accelerate

Run the Game:

bash
python catch_the_diamonds.py

