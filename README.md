
- 《外星人入侵》

- alien_invasion.py
   
   玩这个游戏只需要运行该程序

- settings.py
   
   包含setting类，这个类只包含方法__init__(),初始化控制游戏外观和飞船速度的属性

- game_functions.py
  
   包含一系列的函数，游戏的大部分工作都是由他们完成的。
   如函数check_events()检测相关的事件，按键和松开，使用辅助函数check_keydown_events()和check_keyup_events()处理相关的事情。

- ship.py
    这个类包含方法__init__()、管理飞船位置的方法update()以及在屏幕上绘制飞船的方法blitme().表示飞船的图像存储在文件夹images下的文件ship.bmp中。