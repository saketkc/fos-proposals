Python Software Foundation 2016
================================

Google Summer of Code Application
--------------------------------

###Sub-Organization:

Kivy

###Mentors:

Jacob Kovak, Gabriel Pettier

###Personal Details:

 - **Name:** Meet Udeshi
 - **IRC:** [*udiboy1209@irc.freenode.net*](mailto:udiboy1209@irc.freenode.net)
 - **Github:** [*https://github.com/udiboy1209*](https://github.com/udiboy1209)
 - **Email:** [*mudeshi1209@gmail.com*](mailto:mudeshi1209@gmail.com)
 - **Telephone:** +91-9619221240
 - **Time Zone:** Mumbai, IST, UTC+0530
 - **GSoC Blog:** [*https://udiboy1209.github.io/blog*](https://udiboy1209.github.io/blog)

###Code Contributions:

I have been actively contributing to open source projects in Python, JavaScript, and Android. I have also been contributing to Kivy for a while now. Here is a list of some of my Pull Requests:

To kivy/kivent:

-   Pull Request \#124: Implement gameview camera rotation
-   Pull Request \#121: Support passing moment for a body as an init argument

To kivy/kivy:

-   Pull Request \#4055: Implement wrapping of continuous long text in TextInput
-   Pull Request \#4024: Always show cursor at the moment of touch
-   Pull Request \#4009: hint\_text in TextInput shows when focused and no text entered
-   Pull Request \#3963: Show disabled\_color when disabled=True for markup label
-   Pull Request \#3914: Implement underline and strikethrough styling for Label and MarkupLabel
-   Pull Request \#3698: Fix audio example not including sound files on Android

You can see a complete list [*here*](https://github.com/search?utf8=%E2%9C%93&q=author%3Audiboy1209++repo%3Akivy%2Fkivy+repo%3Akivy%2Fkivent+repo%3Akivy%2Fbuildozer&type=Issues&ref=searchresults).

I also maintain a few of my own open source projects. You can find a list on my website here: [*https://udiboy1209.github.io/projects*](https://udiboy1209.github.io/projects)

Project Abstract:
----------------

-   **Title:** Tiled Integration with KivEnt

-   **Description:** Tiled is a general-purpose tile map editor. It supports various tile shapes like square, hexagonal, and isometric square. Tiled support in KivEnt will be a very useful tool, given that Tiled is already a well known and feature-rich platform for creating game worlds and maps. A game developer would appreciate getting to use Tiled to create worlds with Kivy than some custom platform in-built into KivEnt. This will also make it easier (at least the map creation part) for people to port their existing games to KivEnt, from other platforms which use Tiled. The aim of this project is to create a fully-functional Tiled module which supports almost all features which Tiled currently supports, i.e. various types of tile shapes, tile animations, multiple layers, shape definitions in tiles, custom data etc. The project will also require a TMX file format loader/parser.

Timeline and List of Deliverables:
--------------------------------

**Community Bonding Period: Work on Animation Module**

Here, I plan to work on and complete the animation module required later for the Tiled module. This should help me get a concrete grip on how the internals of kivent i.e. models, components and game systems function together. In addition to that, I will study [*this PR*](https://github.com/kivy/kivent/pull/117), where an attempt towards integrating Tiled has been started. I will contact the author, and also run the code myself to see if any of it can be used for my project. Also, I hope this period will further help me bond with the Kivy community and its members !

**23<sup>rd</sup> May - 5<sup>th</sup> June: TileSystem Boilerplate code**

To start with, I will write boilerplate for a TileSystem module which renders tiles for a map (Single layer implementation). This will be the basis of the map integration module. I will code keeping in mind the features which are further planned, so that adding them later will be easier. Things planned in these two weeks are:

1.  Starting with putting the TileSystem from the [*13\_tilemap example*](https://github.com/kivy/kivent/blob/2.2-dev/examples/13_tilemap/main.py) in a separate module (with a few changes like using model pointers for adding tiles instead of texture ids). Initialise tiles and textures here.

2.  Creating a template data-holder class for tiles and tile textures. The tile texture template would hold data for the model to be loaded for the tile. Tile template will hold data relevant for the entity, and also a TileTexture field.

3.  Adding API methods for fetching/adding/removing tiles and tile instances in TileSystem. The fetching method will return the tile entity under a coordinate point.

4.  Writing a test example to generate a single-layer map (help in debugging and final demo). This should also test performance, using a performance metric of time for the update method to run.

<!-- -->

**6<sup>th</sup> June - 12<sup>th</sup> June: Animated tiles (Animation System integration)**

I will integrate an animation system which I plan to finish in the community bonding period with this project. This is required to support tile animations feature in Tiled. Breaking down into discrete milestones:

1.  Create a field in the TileTexture template to hold animation frame list. The data stored will be a list of frame, time pairs with frame being a pointer to the model to be displayed, and time being the time period for that frame.

2.  Add the animation system as a renderer for those tile entities. I will ensure that the data stored in TileTexture is compliant with the format the animation renderer works with.

3.  Create another test example to demonstrate this. Test the performance of this feature using the above metric.

<!-- -->

**13<sup>th</sup> June - 26<sup>th</sup> June: TMX Parser module**

*(Points* \[a\] *and* \[b\] *are hoped to be finished when midterm evaluations start)*

I will implement a TMX parser, which will automate the task of loading tiles into the tile template and adding tile sprites to the TileSystem by integrating with the templates defined above. Features to be implemented are:

1.  Load all tile textures specified in tmx in the &lt;tileset&gt; in the TileTexture template.

2.  Parse information about each tile to add to the tile entity template and the TileSystem as a renderer, with pointer to a TileTexture. Support the types of compressions TMX uses, which are base64+zlib, base64+gzip, base64 and csv.

3.  Parse &lt;frame&gt; tags in the tile textures and map that data to the kivent supported animation format required by the animation system in TileTexture.

4.  Create unit-test TMX files to check each component of the parser separately. Do a basic time and memory performance test for this parser, and improve some code if necessary.

<!-- -->

**27<sup>th</sup> June - 10<sup>th</sup> July: Multilayer Support**

Implement a method for multilayer support in the module.

1.  Create a LayerSystem which handles rendering all properties related to a layer in TMX correctly, like position, opacity. Each layer will have its own renderer.

2.  Store the TileTexture for each layer on a single tile position in the tile entity. Add the relevant LayerSystems as renderers for this tile.

3.  Add support to the TMX parser. Parser should be able to merge the tiles on multiple layers but same position into single tile entity. Create unit-test TMX files.

4.  Test using a multi-layer TMX file. Check performance for this system, and the TMX parser with this feature, to see if improvements are necessary.

<!-- -->

**11<sup>th</sup> July - 24<sup>th</sup> July: Isometric and Hexagonal tiles support**

Extend the above defined classes to support other map types like isometric and hexagonal. Most changes will be in the touch interactions of the TileSystem and conversion of world coordinates to map coordinates. Positioning and rendering, along with layers implementation, stays the same. The layer merging part for the parser will differ for isometric. Details:

1.  Create two subclasses of TileSystem which override methods relevant to converting position of tile in the tile grid to its position in the world, i.e. those responsible for loading the position component. This, I believe is all that both tile types would require for rendering, except for some other minor changes.

2.  Loading the textures from the tileset image for both tile types will require different logic, because of the difference in geometry. Thus, the TMX parser will require extra methods to load individual tiles in the tileset from the tileset image.

<!-- -->

**25<sup>th</sup> July - 7<sup>th</sup> July: Miscellaneous Features of Tiled**

Tiled support will be nearly complete with this task. I will add support for miscellaneous features of Tiled such as shape drawing in &lt;objectgroup&gt; and in tile textures, adding &lt;image&gt;s and &lt;imagelayer&gt;s. Some of these features will only be a part of the TMX parser, because they have no relevance to a tile system. A list of these features are :

1.  &lt;objectgroup&gt; and &lt;object&gt;. These allow you to define arbitrary shapes to be placed on your map, not necessarily aligned with the grid or contained within a single Tile. Types will include &lt;ellipse&gt;, &lt;polygon&gt; and &lt;polyline&gt;

2.  &lt;imagelayer&gt; and &lt;image&gt;. These work similar to &lt;objectgroup&gt; when it comes to the positioning of objects. Loading textures for these kind of tags will have to be handled at init time.

3.  Support custom properties for every object which are defined in the &lt;property&gt; tag. Create callbacks use this data, after it's been loaded, but before any other rendering takes place.

<!-- -->

**7<sup>th</sup> August - 15<sup>th</sup> August: Ensure Completion of previous Deliverables**

I am keeping one week as a buffer period to account for delays in previous week’s tasks. I intend to use this period not only to finish off some pending work but also to improve on code finished hastily to keep up with the timeline (use the unit tests to check for performance and make improvements). If there are no such delays, I will start with the next task of documentation.

**16<sup>th</sup> August - 23<sup>rd</sup> August: Documentation, and an Example App**

I am keeping this week solely for the purpose of putting together all individual comments for each method/class together as documentation for this module. I plan on using Sphinx for compiling this documentation, and so I will write the comments and docstrings while coding each task in the format supported by it. Even though I promise to document each week’s code in a blog post as GSoC requires, and also put in appropriate comments and docstrings as and when I create them, I believe they will be made in a much better way if I focus on improving them separately in this week.

I will also write an example app to display this module’s features and capabilities in this week.

Motivation for GSoC:
--------------------

I've always felt the need for a multi-platform system which would make it easier to develop for all platforms, while maintaining uniformity in the application. Kivy meets those expectations brilliantly. I specifically chose to work on the game engine KivEnt because I have been interested in game development since I started coding. I had also created a game of my own (with animated sprites, collisions, physics and everything) when I didn’t know something like game engines even existed! After that, I have tried a few other game engines for small projects. I especially like KivEnt because it is open source, written in Python (a language I am most comfortable with) and also because it can be used to deploy games to multiple platforms using Kivy’s capabilities. I hope to continue contributing to KivEnt and other Kivy projects after GSoC.

Other Commitments:
------------------

My next academic semester starts in the last week of July. I will not be able to work full time except for weekends in the the last 4 weeks ( ~25<sup>th</sup> July to 23<sup>rd</sup> August). I have planned my timeline accordingly, spreading out work to be done in these weeks over a larger time interval.

- **Extra Details:**
- **University:** IIT Bombay
- **Major:** Electrical Engg.
- **Year:** 2<sup>nd</sup>, expected to graduate in 2019
- **Degree:** B.Tech + M.Tech Dual
- **Alternate Contacts:**
- **Facebook:** [*facebook.com/udiboy1209*](https://facebook.com/udiboy1209)
- **Hangouts:** [*plus.google.com/u/0/108170871312475118507*](https://plus.google.com/u/0/108170871312475118507)
