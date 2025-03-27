# NCHU_DNN_HW1
# Gridworld Environment and Value Evaluation

[![專案封面](https://example.com/cover.png)](https://example.com)

# Flask Gridworld Reinforcement Learning Environment

**Overview**  
This Flask application implements a grid-based reinforcement learning environment that demonstrates value iteration for finding optimal paths.

## Features

### Grid Generation
- Users can create grids of size 3×3 to 9×9.

### Map Editing
- **Start position** (green) – only 1 allowed.  
- **End position** (red) – only 1 allowed.  
- **Obstacles** (gray) – up to N-2 allowed.

### Reward Settings
- End position: `+20`  
- Obstacles: `-5`  
- Other cells: `-0.1`

### Optimal Path Calculation
- Uses **Value Iteration** algorithm.  
- Displays **Value Function Map**.  
- Shows **Optimal Policy** with directional arrows.

### Visualization
- Animated robot movement along the optimal path.  
- Color-coded value map.  
- Directional arrows for policy.

---

## Environment Setup
- **Python**: 3.12(64-bit)

### Step 1. Clone This Folder with Sparse-Checkout
```bash
git clone --depth 1 --no-checkout [https://github.com/devilhyt/nchu-stuff.git](https://github.com/enid0101/NCHU_DNN_HW1)

### Step 2. Check the Python Version
