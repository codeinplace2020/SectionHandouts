.. section1:

=================
Section Handout 1
=================

********************
United Nations Karel
********************

As part of its plans to help reconstruct infrastructure worldwide, the United Nations - that's right, the UN is using Karel - established a new program with the mission of dispatching house-building robots to repair flood-damaged areas.

Your job is to program those robots.

Each robot begins at the west end of a street that might look like this:

.. image:: img/initial.png
    :alt: Initial World Layout for United Nations Karel
    :align: center
    :width: 100%

Each beeper in the figure represents a pile of debris. Karel's job is to walk along the street and build a new house in the places marked by each beeper. Those houses, moreover, need to be raised on stilts to avoid damage from the next flood. Each house, in fact, should look exactly like the picture below:

.. image:: img/house.png
    :alt: A House made out of Beepers
    :align: center
    :width: 20%

The new house should be centered at the point at which the bit of debris was left, which means that the first house in the diagram above will be constructed with its left edge along 2nd Avenue. At the end of the run, Karel should be at the east end of the street having created a set of houses that look like this for the initial conditions shown:

.. image:: img/final.png
    :alt: Final world layout for United Nations Karel
    :align: center
    :width: 100%

Keep in mind the following information about the world:

* Karel starts facing east at (1, 1) with an infinite number of beepers in its beeper bag.
* The beepers indicating the positions at which houses should be built will be spaced so that there is room to build the houses without overlapping or hitting walls.
* Karel must end up facing east at the southeast corner of the world. Moreover, Karel should not run into a wall if it builds a house that extends into that final corner.

Write a program to implement the United Nations Karel project. Remember that your program should work for any world that meets the above conditions.
