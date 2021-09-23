from robot import SkidBot

# bot simulation for problem 1
bot_1 = SkidBot()
bot_1.path_1()
bot_1.pyplot_plot()
# You can see it animated in turtle but you have to comment out the pyplot method
# bot_1.turtlefy()

# bot simulation for problem 2
bot_2 = SkidBot()
bot_2.path_2()
bot_2.pyplot_plot()
bot_2.plot_stats()

# bot simulation for problem 3
bot_3 = SkidBot()
bot_3.path_3()
bot_3.pyplot_plot()
bot_3.plot_stats()
