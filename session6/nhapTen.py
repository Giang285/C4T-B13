# while True:
#     name = input("Nhap vao ten: ")
#     if name.isalpha() == True:
#         break


# while True:
#     mk = input("Nhap mat khau: ")
#     if mk.isalpha() == False and len(mk)>8:
#         break

#--------------------------------------------------------------------

# ask = input("Nhap vao so: ")
# print("So ban nhap vao ", len(ask), "digits")

#--------------------------------------------------------------------

import pyglet

music = pyglet.resource.media('viDu.mp3')
music.play()

pyglet.app.run()
