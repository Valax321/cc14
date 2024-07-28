@echo off
set GAMEBIN="%STEAMDIR%\steamapps\common\Source SDK Base 2013 Singleplayer\hl2.exe"
echo Locating Source SDK at %GAMEBIN%
%GAMEBIN% -game %~dp0 -windowed -noborder -width 1920 -height 1080 -nop4 +developer 2 +sv_cheats 1