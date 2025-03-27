# NCHU_DNN_HW1
# Gridworld Environment and Value Evaluation

<img src="[https://github.com/enid0101/0/blob/main/gif/DRL/DRL.gif?raw=true](https://github.com/enid0101/NCHU_DNN_HW1/blob/main/image/DRL.gif?raw=true)" width=550" height="500" alt="Yu-chun Lin">
([https://example.com/cover.png](https://github.com/enid0101/NCHU_DNN_HW1/blob/main/image/DRL.gif?raw=true))]([https://example.com](https://github.com/enid0101/NCHU_DNN_HW1/blob/main/image/DRL.gif?raw=true))

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
### Step 1. Clone This Folder with Sparse-Checkout
```bash
git clone --depth 1 --no-checkout [https://github.com/devilhyt/nchu-stuff.git](https://github.com/enid0101/NCHU_DNN_HW1)
```
### Step 2. Python Version
- **Python**: 3.12(64-bit)

### Step 3. Python Version
- Install All Dependencies
- flask==3.1.0
- numpy==2.2.3

### Step 4. Run Flask Server
```bash
flask run
```
This server is running on http://127.0.0.1:5000

## How to Use
Generate the Grid
- Select a size between 3 and 9, then click Generate.
- Mark the Start, End, and Obstacles
- First cell clicked: Start position
- Second cell clicked: End position
- Next N–2 clicks: Obstacles
- Calculate and Visualize
-- Click CALC to compute the optimal policy.

## Random and Reset
- Click Random to create a random grid and compute its path.
- Click RESET to clear the board and start fresh.

# Appendix
If you have anything want to know, feel free to let me know, thx.
