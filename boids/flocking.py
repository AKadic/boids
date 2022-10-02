import config
import numpy as np


def cohesion(boid):
    """
    Cohesion

    For the average position (i.e. center) of all nearby 
    boids, calculate steering vector towards that position
    """
    neighbordist = 0.2
    # Start with empty vector to accumulate all positions
    sum = np.array([0, 0])
    count = 0

    for other in config.boids:
        v = boid.position - other.position
        d = np.linalg.norm(v)

        if d > 0 and d < neighbordist:
            sum = np.add(sum, other.position)
            count += 1

    if count > 0:
        sum /= count
        return boid.seek(sum)

    return np.array([0, 0])


def align(boid):
    """
    Alignment

    For every nearby boid in the system, calculate the 
    average velocity
    """
    neighbordist = 0.2
    # Start with empty vector to accumulate all positions
    sum = np.array([0, 0])
    count = 0

    for other in config.boids:
        v = boid.position - other.position
        d = np.linalg.norm(v)

        if d > 0 and d < neighbordist:
            sum = np.add(sum, other.velocity)
            count += 1

    if count > 0:
        sum = np.divide(sum, count)

        # Scale to maximum speed
        normalized = sum / np.sqrt(np.sum(sum**2))
        desired = normalized * boid.maxSpeed
        # Steering = Desired minus Velocity
        steering = desired - boid.velocity
        steering = np.clip(steering, -boid.maxForce, boid.maxForce)

        return steering

    return np.array([0, 0])


def seperate(boid):
    """
    Separation

    Method checks for nearby boids and steers away
    """
    desiredseparation = 25

    steer = np.array([0, 0])
    count = 0
    # For every boid in the system, check if it's too close
    for other in config.boids:
        v = boid.position - other.position
        d = np.linalg.norm(v)

        # If the distance is greater than 0 and less than an
        # arbitrary amount(0 when you are yourself)
        if d > 0 and d < desiredseparation:
            # Calculate vector pointing away from neighbor
            normalized = v / np.sqrt(np.sum(v**2))
            difference = normalized / d  # Weight by distance
            steer = np.add(steer, difference)
            count += 1

    # Average
    if count > 0:
        steer /= count

    # As long as the vector is greater than 0
    length = np.linalg.norm(v)
    if length > 0:
        # Scale to maximum speed
        normalized = steer / np.sqrt(np.sum(steer**2))
        desired = normalized * boid.maxSpeed
        # Steering = Desired minus Velocity
        steering = desired - boid.velocity
        steering = np.clip(steering, -boid.maxForce, boid.maxForce)
        steer = steering

    return steer
