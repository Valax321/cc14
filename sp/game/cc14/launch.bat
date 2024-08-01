@echo off
set GAMEBIN="%STEAMDIR%\steamapps\common\Source SDK Base 2013 Singleplayer\hl2.exe"
echo Locating Source SDK at %GAMEBIN%
%GAMEBIN% -game %~dp0 -force_vendor_id 0x10DE -force_device_id 0x1180 -windowed -width 1600 -height 900 -nop4 +developer 2 +sv_cheats 1