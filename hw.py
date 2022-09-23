import matplotlib.pyplot as plt
from cmath import cos, sin, sqrt, pi


def dist(x1, y1, x2=0, y2=0):
    return sqrt(abs(x1-x2)**2 + abs(y1-y2)**2).real


def plot(x, y, xName = 'x - axis', yName = 'y - axis', plotName = 'plot'):
    # plot points
    plt.plot(x,y)

    # rename axises
    plt.xlabel(xName)
    plt.ylabel(yName)

    # set graph title
    plt.title(plotName)

    # show graph
    plt.show()


def f_kinematics(vLeft, vRight, x0, y0, theta0, w, dt=0.1):
    xNow = x0 - 1.0/2.0 * (vRight + vLeft) * sin(theta0).real * dt
    yNow = y0 + 1.0/2.0 * (vRight + vLeft) * cos(theta0).real * dt
    thetaNow = theta0 + 1/w * (vRight - vLeft) * dt
    return(xNow, yNow, thetaNow)


def doInstruction(duration, lwv, rwv, currXPos, currYPos, currTheta, x, y, time=[0], theta=[0], width=.3, dt=.1):
    for i in range(int(duration * 10)):
        xNow, yNow, thetaNow = f_kinematics(lwv, rwv, currXPos, currYPos, currTheta, width, dt)
        theta.append((thetaNow - currTheta) / dt)
        currXPos = xNow
        currYPos = yNow
        currTheta = thetaNow
        x.append(xNow)
        y.append(yNow)
        time.append(time[-1] + dt)

    return currXPos, currYPos, currTheta, x, y, theta, time


def problem1():
    print("starting problem 1")
    x = [0]
    y = [0]

    currXPos = 0
    currYPos = 0
    currTheta = 0
    width = .3
    dt = .1

    # section 1
    duration = 5
    lwv = 1
    rwv = 2
    currXPos, currYPos, currTheta, x, y, theta, time = doInstruction(duration, lwv, rwv, currXPos, currYPos, currTheta, x, y)

    # section 2
    duration = 3
    lwv = -1
    rwv = -1.5
    currXPos, currYPos, currTheta, x, y, theta, time = doInstruction(duration, lwv, rwv, currXPos, currYPos, currTheta, x, y)
        
    # section 3
    duration = 8
    lwv = .8
    rwv = -2
    currXPos, currYPos, currTheta, x, y, theta, time = doInstruction(duration, lwv, rwv, currXPos, currYPos, currTheta, x, y)

    # section 4
    duration = 10
    lwv = 2
    rwv = 2
    currXPos, currYPos, currTheta, x, y, theta, time = doInstruction(duration, lwv, rwv, currXPos, currYPos, currTheta, x, y)

    plot(x, y)

problem1()

def turnRight():
    return(1, .235, -.235)

def turnLeft():
    return(1, -.235, .235)

def forward30():
    return(1, .3, .3)

def forward500():
    return(2.5, 2, 2)

# problem 2
def problem2():
    print("starting problem 2")
    width = .3
    x = [0]
    y = [0]
    theta=[0]
    time=[0]

    currXPos = 0
    currYPos = 0
    currTheta = 0
    dt = .1

    for i in range(17):
        if i % 2 == 0:
            duration, lwv, rwv = forward500()
            currXPos, currYPos, currTheta, x, y, theta, time = doInstruction(duration, lwv, rwv, currXPos, currYPos, currTheta, x, y, theta=theta, time=time)
            # turn 90 degrees
            duration, lwv, rwv = turnRight()
            currXPos, currYPos, currTheta, x, y, theta, time = doInstruction(duration, lwv, rwv, currXPos, currYPos, currTheta, x, y, theta=theta, time=time)
            # go forward 30 cm
            duration, lwv, rwv = forward30()
            currXPos, currYPos, currTheta, x, y, theta, time = doInstruction(duration, lwv, rwv, currXPos, currYPos, currTheta, x, y, theta=theta, time=time)
            # turn again 90 degrees
            duration, lwv, rwv = turnRight()
            currXPos, currYPos, currTheta, x, y, theta, time = doInstruction(duration, lwv, rwv, currXPos, currYPos, currTheta, x, y, theta=theta, time=time)
        else:
            duration, lwv, rwv = forward500()
            currXPos, currYPos, currTheta, x, y, theta, time = doInstruction(duration, lwv, rwv, currXPos, currYPos, currTheta, x, y, theta=theta, time=time)
            # turn 90 degrees
            duration, lwv, rwv = turnLeft()
            currXPos, currYPos, currTheta, x, y, theta, time = doInstruction(duration, lwv, rwv, currXPos, currYPos, currTheta, x, y, theta=theta, time=time)
            # go forward 30 cm
            duration, lwv, rwv = forward30()
            currXPos, currYPos, currTheta, x, y, theta, time = doInstruction(duration, lwv, rwv, currXPos, currYPos, currTheta, x, y, theta=theta, time=time)
            # turn again 90 degrees
            duration, lwv, rwv = turnLeft()
            currXPos, currYPos, currTheta, x, y, theta, time = doInstruction(duration, lwv, rwv, currXPos, currYPos, currTheta, x, y, theta=theta, time=time)

    plot(x, y, "x position", "y position", "Position")

    # Trajectories of x, y
    dx = [(x[i+1]-x[i])/dt for i in range(len(x)-1)]
    dy = [(y[i+1]-y[i])/dt for i in range(len(y)-1)]
    plot(time[:len(time)-1], dx, "time", "trajectory", "X Trajectory")
    plot(time[:len(time)-1], dy, "time", "trajectory", "Y Trajectory")
    plot(time, theta, "time", "angular velocity", "Theta")


problem2()


def problem3():
    print("starting problem 3")
    width = .3
    x = [0]
    y = [0]
    time = [0]

    currXPos = 0
    currYPos = 0
    dt = .1

    for i in range(9):
        # Go up
        time, x, y = goDir(5, 2, 0, currXPos, currYPos, time, x, y, dt)
        currXPos = x[-1]
        currYPos = y[-1]
        # Go right
        time, x, y = goDir(.3, .5, 90, currXPos, currYPos, time, x, y, dt)
        currXPos = x[-1]
        currYPos = y[-1]
        # Go down
        time, x, y = goDir(5, 2, 180, currXPos, currYPos, time, x, y, dt)
        currXPos = x[-1]
        currYPos = y[-1]
        # Go right
        time, x, y = goDir(.3, .5, 90, currXPos, currYPos, time, x, y, dt)
        currXPos = x[-1]
        currYPos = y[-1]

    plot(x, y, "x position", "y position", "Position")
    # Trajectories of x, y
    dx = [(x[i + 1] - x[i]) / dt for i in range(len(x) - 1)]
    dy = [(y[i + 1] - y[i]) / dt for i in range(len(y) - 1)]
    plot(time[:len(time) - 1], dx, "time", "trajectory", "X Trajectory")
    plot(time[:len(time) - 1], dy, "time", "trajectory", "Y Trajectory")


def goDir(length, speed, theta, x, y, time, xs=[0], ys=[0], dt=.1):
    theta = theta * pi / 180
    remaining = length
    xPrev = x
    yPrev = y
    while (remaining - dist((speed * sin(theta).real * dt), (speed * cos(theta).real * dt))) > 0:
        xNew = xPrev + (speed * sin(theta).real * dt)
        yNew = yPrev + (speed * cos(theta).real * dt)
        xs.append(xNew)
        ys.append(yNew)
        remaining = remaining - dist(xNew, yNew, xPrev, yPrev)
        xPrev = xNew
        yPrev = yNew
        time.append(time[-1] + dt)
    return time, xs, ys


problem3()
