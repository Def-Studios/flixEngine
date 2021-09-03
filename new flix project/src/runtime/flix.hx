package;
// set up some annoying stuff

include py;
py.init();

py.game.init(0,0,0, 234,253);
py.state.create("src/main.py", (game));
py.sys.quit();
