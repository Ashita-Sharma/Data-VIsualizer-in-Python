# 📊 Sorting Algorithm Visualizer

A real-time sorting algorithm visualizer built with Python and Pygame. Watch different sorting algorithms in action with color-coded comparisons and swaps!

## ✨ Features

- **5 Sorting Algorithms**: Bubble Sort, Insertion Sort, Selection Sort, Quick Sort, and Heap Sort
- **Visual Feedback**: Color-coded bars show comparisons (red/green) and operations in real-time
- **Dual Sorting Modes**: Sort in ascending or descending order
- **Interactive Controls**: Switch algorithms, reset data, and control sorting on the fly
- **Customizable**: Easy to adjust list size, value range, and visualization speed

## 🎯 Supported Algorithms

| Algorithm | Best Case | Average Case | Worst Case | Space |
|-----------|-----------|--------------|------------|-------|
| **Bubble Sort** | O(n) | O(n²) | O(n²) | O(1) |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | O(1) |
| **Selection Sort** | O(n²) | O(n²) | O(n²) | O(1) |
| **Quick Sort** | O(n log n) | O(n log n) | O(n²) | O(log n) |
| **Heap Sort** | O(n log n) | O(n log n) | O(n log n) | O(1) |

## 🚀 Installation & Usage

```bash
# Clone the repository
git clone https://github.com/Ashita-Sharma/Data-VIsualizer-in-Python.git
cd Data-VIsualizer-in-Python

# Install pygame
pip install pygame

# Run the visualizer
python main.py
```

**Requirements**: Python 3.7+, pygame

## 🎮 Controls

| Key | Action |
|-----|--------|
| **SPACE/ENTER** | Start sorting |
| **R** | Reset with new random data |
| **A** | Set to Ascending order |
| **D** | Set to Descending order |
| **B** | Select Bubble Sort |
| **I** | Select Insertion Sort |
| **S** | Select Selection Sort |
| **Q** | Select Quick Sort |
| **H** | Select Heap Sort |

## 🎨 Color Coding

- **Gray bars**: Unsorted elements
- **Green bar**: Current minimum/maximum or pivot element
- **Red bar**: Element being compared
- **Black bar**: Pivot indicator (Quick Sort)

## ⚙️ Customization

Modify these variables in `main()` function:

```python
n = 50          # Number of elements to sort
min_val = 1     # Minimum value
max_val = 100   # Maximum value
clock.tick(60)  # Visualization speed (FPS)
```

Adjust window size in `DrawInformation` initialization:
```python
draw_info = DrawInformation(800, 600, lst)  # width, height
```

## 🏗️ Project Structure

```
Data-Visualizer-in-Python/
├── main.py                    # Main application file
└── README.md                  # This file
```

## 🔧 How It Works

1. **Initialization**: Generates random list of integers
2. **Visualization**: Each element is drawn as a bar with height proportional to its value
3. **Algorithm Execution**: Uses Python generators (`yield`) to pause and update display at each step
4. **Color Updates**: Highlights elements being compared/swapped in real-time
5. **Continuous Loop**: Pygame event loop handles user input and rendering

### Generator Pattern
The visualizer uses Python generators to pause algorithm execution at each comparison/swap:

```python
def bubble_sort(draw_info, ascending=True):
    # ... sorting logic ...
    draw_list(draw_info, {j: GREEN, j+1: RED}, True)
    yield True  # Pause here, show visualization
    # Continue on next iteration
```

## 🎯 Future Ideas

- Add more algorithms (Merge Sort, Radix Sort, Shell Sort)
- Algorithm comparison mode (side-by-side)
- Step-by-step mode with pause/resume
- Export sorting animation as video
- Sound effects for comparisons
- Adjustable speed slider

## 📚 Learning Resources

- [Sorting Algorithms Overview](https://www.geeksforgeeks.org/sorting-algorithms/)
- [Big O Notation](https://www.bigocheatsheet.com/)
- [Pygame Documentation](https://www.pygame.org/docs/)

## 🐛 Troubleshooting

- **Window doesn't open**: Ensure pygame is installed correctly
- **Sorting doesn't start**: Press SPACE or ENTER after selecting algorithm
- **Performance issues**: Reduce `n` (number of elements) or increase `clock.tick()` value

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👏 Acknowledgments

- Built with [Pygame](https://www.pygame.org/)
- Inspired by various algorithm visualization tools

## 📧 Contact

**Ashita Sharma**
- GitHub: [@Ashita-Sharma](https://github.com/Ashita-Sharma)

---

⭐ **Star this repo if you find it useful!** ⭐

**Happy Sorting! 🎨📊**
