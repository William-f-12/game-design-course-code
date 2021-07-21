import random as r
PI = 3.14

class Circle:

    def __init__(self, center: list, radius: int, color: tuple):
        self.center = center
        self.radius = radius
        self.color = color
        self.velocity = [r.randint(-10, 10), r.randint(-10, 10)]
        self.speed = (self.velocity[0] ** 2 + self.velocity[1] ** 2) ** 0.5
        self.mass = PI * self.radius ** 2 #4/3*PI*self.radius**3 # density = 1
        self.momentum = self.speed * self.mass


    def get_distance(self, another_circle):
        return (self.center[0]-another_circle.center[0])**2 + (self.center[1]-another_circle.center[1])**2


    def is_collided(self, another_circle):
        if self.get_distance(another_circle) <= (self.radius + another_circle.radius)**2:
            return True
        return False

    
    def bounce_the_ball(self, another_ball):
        if self.is_collided(another_ball):
            changed_velocity = [0, 0]
            changed_velocity[0] = self.center[0] - another_ball.center[0]
            changed_velocity[1] = self.center[1] - another_ball.center[1]
            changed_direction = (changed_velocity[0]**2 + changed_velocity[1]**2)**0.5
            changed_velocity[0], changed_velocity[1] = (changed_velocity[0] / changed_direction), (changed_velocity[1] / changed_direction)
            changed_speed = another_ball.momentum / self.mass
            self.velocity[0], self.velocity[1] = changed_speed * changed_velocity[0], changed_speed * changed_velocity[1]

            # s = 2*(self.velocity[0]*(self.center[0]-another_ball.center[0])+self.velocity[1]*(self.center[1]-another_ball.center[1]))
            # s /= (self.center[0]-another_ball.center[0])**2+(self.center[1]-another_ball.center[1])**2
            # self.velocity[0] = self.velocity[0] - s * (self.center[0] - another_ball.center[0])
            # self.velocity[1] = self.velocity[1] - s * (self.center[1] - another_ball.center[1])

    
    # def bounce_the_wall(self):
    #     if self.center[0] <= self.radius or self.center[0] >= RESOLUTION[0]-self.radius-5:
    #         self.velocity[0] *= -1
        
    #     if self.center[1] <= self.radius or self.center[1] >= RESOLUTION[1]-self.radius-5:
    #         self.velocity[1] *= -1


    def move(self):
        self.center[0] += self.velocity[0]
        self.center[1] += self.velocity[1]

    
    # def draw(self):
    #     pygame.draw.circle(DISPLAYSURF, self.color, self.center, self.radius)