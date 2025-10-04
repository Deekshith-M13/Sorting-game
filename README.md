# Sorting Visualizer Game

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-2.x-orange)](https://www.pygame.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A interactive sorting algorithm visualizer built with Pygame. Watch Bubble, Insertion, Merge, and Quick Sort algorithms in action on a colorful bar graph! Toggle ascending/descending order, adjust speed, and reset for endless fun. Optimized for web play via PyGBag—perfect for learning algorithms through gameplay.

<img width="893" height="478" alt="Screenshot 2025-10-04 183439" src="https://github.com/user-attachments/assets/69119207-4c3e-4ced-b8c9-1d76b69bbfe1" />


## Features

- **Four Classic Algorithms**: Bubble Sort, Insertion Sort, Merge Sort, and Quick Sort.
- **Interactive Controls**: Start/stop sorting, switch ascending/descending, speed up/slow down, and reset the list.
- **Visual Feedback**: Real-time bar animations with color-coded comparisons (green for swaps, red for pivots, etc.).
- **Web-Friendly**: Deployable to browsers using PyGBag for instant play—no downloads needed.
- **Customizable**: Generate random lists of varying sizes (default: 100 elements, 0-100 range).
- **Performance Tweaks**: Reduced drawing frequency for smooth animation, even on lower-end devices.

<img width="865" height="489" alt="Screenshot 2025-10-04 183928" src="https://github.com/user-attachments/assets/19cb2ed6-61dd-4021-a923-940eb80f5782" />


## Live Demo

Play it live in your browser: [Sorting Visualizer Demo]([https://your-live-link-here.com](https://my-sorting-game.vercel.app/)) 

## Architecture Overview

The app uses Pygame for rendering and event handling, with asyncio for non-blocking sort animations. Key components:
- **DrawInformation**: Manages the window, list scaling, and gradient colors for bars.
- **Sorting Functions**: Async implementations of algorithms with visual pauses for step-by-step viewing.
- **Main Loop**: Handles keyboard inputs and clock-based FPS control.

*(Add your architecture diagram if available, or a simple flowchart: ![Flowchart](screenshots/flowchart.png).)*

## Prerequisites

- Python 3.8+ (tested on 3.12).
- Pygame: `pip install pygame`.
- For web deployment: PyGBag (`pip install pygbag`)—build with `pygbag .` in the project root.

No additional setup needed for local runs!

## Installation & Running Locally

1. **Clone the Repository**:
   ```
   git clone https://github.com/yourusername/sorting-visualizer-game.git
   cd sorting-visualizer-game
   ```

2. **Install Dependencies**:
   ```
   pip install pygame
   ```

3. **Run the App**:
   ```
   python main.py
   ```
   - A window (800x600) opens with controls at the top.
   - Use keyboard shortcuts (see below) to start sorting!

4. **For Web Deployment** (Optional):
   - Install PyGBag: `pip install pygbag`.
   - Build: `pygbag .` (outputs to `dist/` folder).
   - Host the `dist/index.html` on itch.io, GitHub Pages, or your server for browser play.

## Controls

Use these keyboard shortcuts during gameplay:

| Key | Action |
|-----|--------|
| **R** | Reset: Generate a new random list. |
| **SPACE** | Start/Stop: Begin sorting the current algorithm. |
| **A** | Ascending: Sort from low to high. |
| **D** | Descending: Sort from high to low. |
| **B** | Bubble Sort: Select Bubble algorithm. |
| **I** | Insertion Sort: Select Insertion algorithm. |
| **M** | Merge Sort: Select Merge algorithm. |
| **Q** | Quick Sort: Select Quick algorithm. |
| **UP Arrow** | Faster: Increase animation speed (up to 120 FPS). |
| **DOWN Arrow** | Slower: Decrease animation speed (down to 10 FPS). |
| **ESC/Quit** | Close the window. |

<img width="424" height="103" alt="Screenshot 2025-10-04 184941" src="https://github.com/user-attachments/assets/9d698b61-2cb7-472a-a7e8-41aa03835759" />


## Algorithms Explained

Each sort visualizes comparisons and swaps:
- **Bubble Sort**: Repeatedly swaps adjacent elements if out of order—simple but O(n²).
- **Insertion Sort**: Builds a sorted list by inserting elements one by one—efficient for small lists.
- **Merge Sort**: Divide-and-conquer: splits, sorts halves, merges—stable and O(n log n).
- **Quick Sort**: Pivot-based partitioning—fast average O(n log n), but worst-case O(n²).

Watch the bars "dance" as they sort! Colors highlight active elements for better understanding.

<img width="832" height="489" alt="Screenshot 2025-10-04 184026" src="https://github.com/user-attachments/assets/6c61bc23-3b24-4480-9399-9494aa6efa81" />
<img width="865" height="489" alt="Screenshot 2025-10-04 183928" src="https://github.com/user-attachments/assets/1883c5f3-b6ab-4f4c-a7e6-758d67034306" />
<img width="876" height="491" alt="Screenshot 2025-10-04 183841" src="https://github.com/user-attachments/assets/6b1c1df6-a6da-403b-88fc-35badb0f2c13" />




## Customization

- **List Size**: Edit `n = 100` in `main()` for more/fewer bars (e.g., 50 for faster, 200 for detailed).
- **Value Range**: Change `min_val, max_val = 0, 100` for taller/shorter bars.
- **Colors/Fonts**: Tweak `DrawInformation` class (e.g., add more gradients).
- **Speed**: Default FPS is 60; async sleeps control sort pace.

For contributions, fork and PR with your tweaks!

## Troubleshooting

- **No Window Opens**: Ensure Pygame is installed and run in a graphical environment (not headless server).
- **Slow Performance**: Reduce `n` or increase drawing intervals (e.g., `if j % 10 == 0` in sorts).
- **Web Issues**: PyGBag limits resources—keep list size under 150 for smooth browser play.
- **Errors**: Check console; common fix: `pygame.init()` if fonts fail.

## Contributing

Love sorting algos? Contribute by adding more sorts (e.g., Heap Sort), themes, or sound effects!
1. Fork the repo.
2. Create a feature branch (`git checkout -b feature/new-sort`).
3. Commit changes (`git commit -m 'Add Heap Sort'`).
4. Push and open a PR.

Yourusername (@yourgithub) – Main Developer.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. *(Add a LICENSE file with MIT boilerplate.)*

---

*Built with ❤️ for algorithm enthusiasts. Questions? Open an issue!*
