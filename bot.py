from envpong import PongLogic
import random

class BotRight:
    def __init__(self, env):
        self.env = env
        
        # This bot doesn't require an initial observation
        self.obs = [0]*len(env.observation_space.sample())
    
    def act(self):
        # ball tracking strategy
        p2y = self.obs[5]   # player 2 vertical position
        ballx = self.obs[8] # ball horizontal position
        bally = self.obs[9] # ball vertical position
        ballvx = self.obs[10] # ball horizontal velocity
        ballvy = self.obs[11] # ball vertical velocity
        
        if ballvx <= 0:
            return self.returnCenter(p2y)
            #return self.followBall(p2y, bally)
        
        hitLocation = self.getHitLocation(ballx, bally, ballvx, ballvy)

        if p2y < hitLocation - 0.02:
            return PongLogic.PaddleMove.UP
        if p2y > hitLocation + 0.02:
            return PongLogic.PaddleMove.DOWN
            
        return PongLogic.PaddleMove.STILL
    
    def observe(self, obs):
        self.obs = obs

    def returnCenter(self, p2y):
        if p2y < 0.5:
            return PongLogic.PaddleMove.UP
        else:
            return PongLogic.PaddleMove.DOWN

    def followBall(self, p2y, bally):
        if  p2y < bally:
            return PongLogic.PaddleMove.UP
        else:
            return PongLogic.PaddleMove.DOWN

    def getHitLocation(self, ballx, bally, ballvx, ballvy): 
        repetitions = 0
        while ( repetitions < 5 ):
            target = bally + ( (ballvy/ballvx) * ( 0.85 - ballx ))
            if target < 0:
                ballx = ballx - bally*(ballvx/ballvy)
                bally = 0
                ballvy = -ballvy
            if target > 1:
                ballx = ballx - (1-bally)*(ballvx/ballvy)
                bally = 1
                ballvy = -ballvy
            repetitions += 1
        return target
        
       
class BotLeft:
    def __init__(self, env):
        self.env = env
        
        # This bot requires an initial observation, set everything to zero
        self.obs = [0]*len(env.observation_space.sample())
    
    def act(self):
        # ball tracking strategy
        p1y = self.obs[1]   # player 1 vertical position
        p2y = self.obs[5]   # player 2 vertical position
        ballx = self.obs[8] # ball horizontal position
        bally = self.obs[9] # ball vertical position
        ballvx = self.obs[10] # ball horizontal velocity
        ballvy = self.obs[11] # ball vertical velocity
        
        if ballvx >= 0:
            return self.followPlayer(p1y, p2y)
            #return self.returnCenter(p1y)
            #return self.followBall(p1y, bally)
        
        hitLocation = self.getHitLocation(ballx, bally, ballvx, ballvy)

        if p1y < hitLocation - 0.02:
            return PongLogic.PaddleMove.UP
        if p1y > hitLocation + 0.02:
            return PongLogic.PaddleMove.DOWN
            
        return PongLogic.PaddleMove.STILL
    
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

    def followPlayer(self, p1y, p2y):
        if  p1y < p2y:
            return PongLogic.PaddleMove.UP
        else:
            return PongLogic.PaddleMove.DOWN

    def getHitLocation(self, ballx, bally, ballvx, ballvy): 
        repetitions = 0
        while ( repetitions < 5 ):
            target = bally - ( (ballvy/ballvx) * ( ballx - 0.15))
            if target < 0:
                ballx = ballx - bally*(ballvx/ballvy)
                bally = 0
                ballvy = -ballvy
            if target > 1:
                ballx = ballx - (1-bally)*(ballvx/ballvy)
                bally = 1
                ballvy = -ballvy
            repetitions += 1
        return target
