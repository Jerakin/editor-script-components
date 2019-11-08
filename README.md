# Components

## Install
You can use the these editor scripts in your own project by adding this project as a [Defold library dependency](https://www.defold.com/manuals/libraries/). Open your game.project file and in the dependencies field under project add:  
https://github.com/Jerakin/editor-script-components/archive/master.zip

## Editor Script
This script adds a few menu items, which shows up depends on the type of file selected. They all create a new resource depending on your selection. A wav or ogg creates a sound component, a json will create a spine scene and a spine scene a spine model.  
If you want to create atlases I recommend using https://github.com/Jerakin/editor-script-atlas
```
$.wav               => $.sound  
$.ogg               => $.sound  
$.json and $.atlas  => $.spinescene
$.spinescene        => $.spinemodel  
```
