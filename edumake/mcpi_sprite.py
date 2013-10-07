import mcpi.minecraft as minecraft
import mcpi.block as block
from mcpi.vec3 import *

class Sprite:
        """Methods for drawing sprites"""
        def __init__(self, mc, pattern):
                self.mc = mc
                self.pattern = pattern
                
        def draw(self, foreground = block.STONE, background = block.AIR , start = Vec3(0,0,0)):
                y = start.y + 7
                self.mc.setBlocks(start.x, start.y, start.z, start.x+7, y, start.z, background) 
                for line in self.pattern:
                        compare_bit = 0b1
                        for x in list(range(start.x + 7, start.x - 1, -1)):
                                if compare_bit & line: 
                                        self.mc.setBlock(x, y, start.z, foreground)                                             
                                compare_bit = compare_bit << 1
                        y = y - 1


        def drawrelative(self, foreground = block.STONE, background = block.AIR, start = Vec3(0,0,0)):
                playerpos = self.mc.player.getTilePos()
                pos = start + playerpos
                self.draw(foreground, background, pos)


        def drawnear(self, foreground = block.STONE, background = block.AIR, offset = Vec3(0,0,0)):
                pos = Vec3(-4, 0, -10) + offset
                self.drawrelative(foreground, background, pos)
