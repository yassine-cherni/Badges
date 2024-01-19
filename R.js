class AutonomousRobot {
  constructor() {
    this.position = { x: 0, y: 0 };
  }

  moveRandomly() {
    const randomDirection = Math.random() * 360; // Random angle in degrees
    const distance = Math.random() * 10; // Random distance to move

    // Convert polar coordinates to Cartesian coordinates
    const deltaX = distance * Math.cos(randomDirection);
    const deltaY = distance * Math.sin(randomDirection);

    // Update the robot's position
    this.position.x += deltaX;
    this.position.y += deltaY;

    console.log(`Moved to: (${this.position.x.toFixed(2)}, ${this.position.y.toFixed(2)})`);
  }
}

// Example usage
const robot = new AutonomousRobot();

// Move the robot randomly multiple times
for (let i = 0; i < 5; i++) {
  robot.moveRandomly();
}
