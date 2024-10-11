from envpong import PongLogic
import random

class BotRight:
    def __init__(self, env):
        self.env = env
        
        # This bot doesn't require an initial observation
        self.obs = [0]*len(env.observation_space.sample())
    
    def act(self):
        p1y = self.obs[5]   # player 1 vertical position
        bally = self.obs[9] # ball vertical position
        
        if p1y < bally:
            action = PongLogic.PaddleMove.UP
        else:
            action = PongLogic.PaddleMove.DOWN
            
        return action
    
    def observe(self, obs):
        self.obs = obs
        
       
class BotLeft:
    def __init__(self, env):
        self.env = env
        
        # This bot requires an initial observation, set everything to zero
        self.obs = [0]*len(env.observation_space.sample())
    
    def act(self):
        # ball tracking strategy
        p1y = self.obs[1]   # player 1 vertical position
        ballx = self.obs[8] # ball horizontal position
        bally = self.obs[9] # ball vertical position
        ballvx = self.obs[10] # ball horizontal velocity
        ballvy = self.obs[11] # ball vertical velocity
        
        if ballvx >= 0:
            #return self.returnCenter(p1y)
            return self.followBall(p1y, bally)
        
        target = bally - ( (ballvy/ballvx) * ( ballx - 0.15))

        if p1y < target:
            action = PongLogic.PaddleMove.UP
        else:
            action = PongLogic.PaddleMove.DOWN
            
        return action
    
    def observe(self, obs):
        self.obs = obs

    def returnCenter(self, p1y):
        if p1y < 0.5:
            return PongLogic.PaddleMove.UP
        else:
            return PongLogic.PaddleMove.DOWN

    def followBall(self, p1y, bally):
        if  p1y < bally:
            return PongLogic.PaddleMove.UP
        else:
            return PongLogic.PaddleMove.DOWN

        
