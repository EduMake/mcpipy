import mcpi.minecraft as minecraft
import mcpi.block as block
from edumake.mcpi_sprite import *

mc = minecraft.Minecraft.create()

sprite = Sprite(mc, [\
          0b00000111, 0b00000011,\
          0b00000001, 0b00000000,\
          0b00000000, 0b00000000,\
          0b00000000, 0b10000000
          ])

sprite.drawnear()

print sprite.pattern
